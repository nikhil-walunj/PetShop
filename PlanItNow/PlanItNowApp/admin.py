from django.contrib import admin
from .models import petFood,petFoodDetails,pet,petVaccine,customer,petProduct,petProdCategory,cart,custForm,ordersdetail

# Register your models here.

class petFoodAdmin(admin.ModelAdmin):
    list_display=['petFoodId', 'petFoodName','petFoodPrice','petFoodDesc','price']
admin.site.register(petFood,petFoodAdmin)

class petFoodDetailsadmin(admin.ModelAdmin):
    list_display=['petFood','company','expiryDate']
admin.site.register(petFoodDetails,petFoodDetailsadmin)

class petAdmin(admin.ModelAdmin):
    list_display=['petName','petCat']
admin.site.register(pet,petAdmin)

class petvaccineAdmin(admin.ModelAdmin):
    list_display=['vaccineName']
admin.site.register(petVaccine,petvaccineAdmin)

class customer_Admin(admin.ModelAdmin):
    list_display = ['customerId','customerName','customerEmail','customerContact']
admin.site.register(customer,customer_Admin)


class productAdmin(admin.ModelAdmin):
    list_display = ['prodName','proDesc','proPrice','prodImage','prodRating','prodCategory','is_deleted' ,'delete_details']
admin.site.register(petProduct,productAdmin)

class productCategoryAdmin(admin.ModelAdmin):
    list_display=['categroyName','categroyDesc']
admin.site.register(petProdCategory,productCategoryAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display=['uid','pid','qty']
admin.site.register(cart,cartAdmin)

class customerDetailsFormAdmin(admin.ModelAdmin):
    list_display=['user','custfullName','custemailId','custphoneNo','custAddress','custcity','pinCode','countryName','additionalNotes']
admin.site.register(custForm,customerDetailsFormAdmin)


class ordersdetailAdmin(admin.ModelAdmin):
    list_display=['customerName','pet','quantity','orderDate','productstatus','totalPrice']
admin.site.register(ordersdetail,ordersdetailAdmin)