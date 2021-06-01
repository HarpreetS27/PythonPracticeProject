from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name='ShopHome'),
   path('products/',views.product,name='products'),
   path('contact/',views.contact,name='contact'),
   path('index/',views.index,name='index'),
   path('products/<int:pid>',views.ppage,name='ppage'),
   path('about/',views.about,name='about'),
   path('checkout/',views.checkout,name='checkout'),
   path('search/',views.search,name='search')
]
