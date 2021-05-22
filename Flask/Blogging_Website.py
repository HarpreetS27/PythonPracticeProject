from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
import math

# open config.json file read params
with open("config.json", "r") as config:
    params = json.load(config)["params"]

local_server = True
app = Flask(__name__)
# assign session secret key
app.secret_key = 'secret-key'

# configuration for mail setup
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['email_user'],
    MAIL_PASSWORD=params['email_pwd']
)

mail = Mail(app)
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

db = SQLAlchemy(app)


# making parameter using SQLALCHEMY
class Post(db.Model):
    """
    sno,title,post_data,author,date,slug
    """
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    post_data = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)
    slug = db.Column(db.String(25), unique=False, nullable=False)
    print(sno, title, post_data, date, slug)


class Contact(db.Model):
    """
    cno,cname,email,msg,phn,cdate
    """
    cno = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    msg = db.Column(db.String(255), unique=False, nullable=False)
    phn = db.Column(db.String(12), unique=False, nullable=False)
    cdate = db.Column(db.String(12), unique=False, nullable=True)


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    # Get all the post first
    posts = Post.query.filter_by().all()
    # posts = Post.query.order_by(Post.date.desc()).all()       For Bringing latest post first
    total_pages = math.ceil(len(posts) / int(params['no_of_post']))
    # print(total_pages)

    # Pagination
    page = request.args.get('page')
    if not str(page).isnumeric():  # if page number is not numeric
        page = 1  # return to home page
    page=int(page)
    posts=posts[(page-1)*int(params['no_of_post']): (page-1)*int(params['no_of_post'])+int(params['no_of_post'])] # 0:2 posts
    #print(posts)
    # Home Page
    if page==1:
        prev='#'
        next="/?page="+str(page+1)
    # Last Page
    elif(page==total_pages):
        next="#"
        prev="/?page="+str(page-1)
    # Mid Page
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    # page=request.args.get('page',1,type=int)
    # posts=Post.query.paginate(page=page,per_page=int(params['no_of_post']))
    """ Here we will take posts from database and pass to our home page"""

    return render_template('index.html', params=params, posts=posts,prev=prev,next=next)


# For login page
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    # If the user is already logged in then don't show login page again

    if 'user' in session and session['user'] == params['admin_name']:
        posts = Post.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('upass')
        if username == params['admin_name'] and password == params['admin_pwd']:
            # assign session key to the user
            session['user'] = username
            posts = Post.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    return render_template('login.html', params=params)


# @app.route("/login",methods=['GET','POST'])
# def login():
#     return redirect("/dashboard")

# To add and Edit Posts
@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_name']:
        if request.method == 'POST':
            # Take input from html user Post request
            htitle = request.form.get('title')
            hdata = request.form.get('post_data')
            hauthor = request.form.get('author')
            hslug = request.form.get('slug')
            date = datetime.now()

            if sno == '0':
                post = Post(title=htitle, post_data=hdata, author=hauthor, slug=hslug, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Post.query.filter_by(sno=sno).first()
                post.title = htitle
                post.post_data = hdata
                post.author = hauthor
                post.slug = hslug
                post.date = date
                db.session.commit()
                return redirect('/edit/' + sno)
        post = Post.query.filter_by(sno=sno).first()

        return render_template("edit.html", params=params, post=post, sno=sno)


# To kill session and logout
@app.route("/logout")
def logout():
    # For debugging
    # username = request.form.get('uname')
    # password = request.form.get('upass')
    # print("printing key : "+str(session.get(username)))
    # print("printing key : "+str(session.get(password)))
    # print(session.keys())
    # print(len(session))

    session.pop('user')

    return redirect('/dashboard')


# To delete a file
@app.route("/delete/<string:sno>")
def delete(sno):
    if 'user' in session and session['user'] == params['admin_name']:
        post = Post.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect("/dashboard")


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        """ Add entries to the database"""

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        """ cno,cname,email,msg,phn,cdate 
            database var=our python var name
        """
        entry = Contact(cname=name, email=email, phn=phone, msg=message, cdate=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Message from The Coding Blog by ' + name,
                          sender=email,
                          recipients=[params['email_user']],
                          body=message + "\n" + "Phone Number:" + str(phone)
                          )

    return render_template('contact.html', params=params)


@app.route("/post", methods=['GET', 'POST'])
def postview():
    post = Post.query.all()
    return render_template('post.html', params=params, post=post)


# To fetch post and enter slug information
# whatever variable we give in app.route has to be given as a parameter to function as well
@app.route("/post/<string:post_slug>", methods=['GET'])
def posts_menu(post_slug):  # takes the input from the web link

    post = Post.query.filter_by(slug=post_slug).first()  # takes data from database by using filter by slug
    return render_template('post.html', params=params, post=post)  # gives data back to html


if __name__ == '__main__':
    app.run(debug=True)
