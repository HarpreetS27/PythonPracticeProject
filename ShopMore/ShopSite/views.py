from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
import math
# Create your views here.

def index(request):
    return render(request,'ShopSite/index.html')


def about(request):
    return render(request,'ShopSite/about.html')


def searchMatch(query,item):
    if query in item.prod_name.lower() or query in item.prod_desc.lower() or query in item.prod_categ.lower():
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    allproducts = []
    prod_categs = Product.objects.values('prod_categ', 'id')
    cats = {item['prod_categ'] for item in prod_categs}
    for cat in cats:
        products=Product.objects.filter(prod_categ=cat)
        prod=[item for item in products if searchMatch(query,item)]
        print(products)
        slide_no = math.ceil((len(products)) / 4)
        if len(prod)!=0:
            allproducts.append([prod,range(slide_no),slide_no])
        print(allproducts)

    params={'allproducts':allproducts}

    return render(request, 'ShopSite/search.html', params)


def product(request):
    # products=Product.objects.all() #fetch all products from database
    # print(products)
    # slide_no=math.ceil((len(products))/4)
    # print(slide_no)
    # # params={'slide_no':slide_no,'range':range(slide_no),'product':products}
    #
    # allproducts=[[products,range(slide_no),slide_no],[products,range(slide_no),slide_no]] # this will show two same products lists
    # params={'allproducts':allproducts}

    print("***********Testing product page code*********")
    allproducts=[]
    prod_categs=Product.objects.values('prod_categ','id')
    print(prod_categs)
    """ Returns a query set with product categaory with id
    <QuerySet [{'prod_categ': 'Electronics', 'id': 3}, {'prod_categ': 'Electronics', 'id': 4}, {'prod_categ': 'Electronics', 'id': 5}, {'prod_categ': 'Electronics', 'id': 7}, {'prod_categ': '
Electronics', 'id': 8}, {'prod_categ': 'Electronics', 'id': 2}, {'prod_categ': 'Electronics', 'id': 6}, {'prod_categ': "Men's Fashion", 'id': 9}, {'prod_categ': "Men's Fashion", 'id': 10}
, {'prod_categ': "Men's Fashion", 'id': 11}, {'prod_categ': "Men's Fashion", 'id': 12}]>

"""
    cats={item['prod_categ'] for item in prod_categs}
    print("cats")  #{'Electronics', "Men's Fashion"} set of categories

    print(cats)  # cats are set
    for cat in cats:
        products=Product.objects.filter(prod_categ=cat)
        print(products)        #<QuerySet [<Product: Mi Notebook Horizon Edition 14>,...
                               #<QuerySet [<Product: MENJESTIC Slim Fit Men's Blazer>,... Return query set for respective categories
        slide_no = math.ceil((len(products)) / 4)

        allproducts.append([products,range(slide_no),slide_no])  #creates a cummulative query set containting product details
        print(allproducts)

    params={'allproducts':allproducts}

    print("***********Testing product page code*********")
    return render(request,'ShopSite/products.html',params)


def contact(request):
    if request.method=='POST':
        dname=request.POST.get('name','')
        demail=request.POST.get('email','')
        dphone=request.POST.get('phone','')
        dmessage=request.POST.get('message','')

        contact_msg=Contact(dbname=dname,dbemail=demail,dbphone=dphone,dbmessage=dmessage)
        contact_msg.save()

        print(dname,demail,dphone,dmessage)
    return render(request,'ShopSite/contact.html')



def checkout(request):
    if request.method == 'POST':
        ditem_json=request.POST.get('itemsJson','')
        dcust_name = request.POST.get('name', '')
        dcust_email = request.POST.get('email', '')
        dcust_adr = request.POST.get('address1', '')+ " "+request.POST.get('address2','')
        dcust_city = request.POST.get('city', '')
        dcust_state = request.POST.get('state', '')
        dcust_zip = request.POST.get('zip', '')
        dcust_phone = request.POST.get('phone', '')


        order = Order(dbitem_json=ditem_json,dbcust_name=dcust_name, dbcust_email=dcust_email,dbcust_adr=dcust_adr,
                      dbcust_city=dcust_city,dbcust_state=dcust_state,dbcust_zip=dcust_zip,dbcust_phone=dcust_phone)
        order.save()
        flag=True
        id=order.dborder_id
        return render(request,"ShopSite/checkout.html",{'flag':flag,'id':id})
    return render(request,"ShopSite/checkout.html")

def ppage(request,pid):
 # Fetch the product from product id
    product = Product.objects.filter(id=pid)

    print(product)  #<QuerySet [<Product: Mi Notebook Horizon Edition 14>]>

    return render(request,'ShopSite/product-page.html',{'product':product[0]})