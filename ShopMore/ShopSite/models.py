from django.db import models


# Create your models here.


class Product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=500)
    prod_categ = models.CharField(max_length=50, default='')
    prod_subcateg = models.CharField(max_length=50, default='')
    prod_price = models.IntegerField(default=0)
    prod_pubdate = models.DateField()
    prod_img = models.ImageField(upload_to="ShopSite/images", default='')

    def __str__(self):
        return self.prod_name


class Contact(models.Model):
    dbmsg_id = models.AutoField(primary_key=True)
    dbname = models.CharField(max_length=50, default='')
    dbemail = models.CharField(max_length=50, default='')
    dbphone = models.CharField(max_length=40,default='')
    dbmessage = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.dbname


class Order(models.Model):
    dborder_id=models.AutoField(primary_key=True)
    dbitem_json=models.CharField(max_length=5000)
    dbcust_name=models.CharField(max_length=200)
    dbcust_email=models.CharField(max_length=200)
    dbcust_adr=models.CharField(max_length=200)
    dbcust_city=models.CharField(max_length=100)
    dbcust_state=models.CharField(max_length=100)
    dbcust_zip=models.IntegerField()
    dbcust_phone=models.IntegerField()
