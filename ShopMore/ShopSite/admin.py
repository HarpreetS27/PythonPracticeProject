from django.contrib import admin

# Register your models here.


from .models import Product,Contact,Order # our class created has to be registered here in order to view it in admin panel
admin.site.register(Product)

admin.site.register(Contact)
admin.site.register(Order)