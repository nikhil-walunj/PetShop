from django.urls import path
from .import views
urlpatterns = [
    path('',views.show,name="home"),
    path('contact',views.contact),
    path('edit/<rid>',views.edit),
    path('SimpleView',views.SimpleView.as_view()),
    path('Crud',views.crud),
    path('showalldetails',views.showdetails),
    path('delete/<int:id>/',views.deletecust),
    path('edit/<int:id>/',views.edits),
    path('reg/',views.register,name='register'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logout/',views.signout,name='signout'),
    path('cat/<int:id>/',views.category,name='cat'),
    path('card/<int:id>/',views.viewCards,name='viewcards'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('deleteproductcrud/<int:id>/',views.deleteproductcrud,name='deleteproductcrud'),
    path('viewcart/',views.viewcart,name='viewcart'),
    path('updateqty/<qv>/<id>/',views.updateqty),
    path('searchanything/',views.searchanything,name='searchanything'),
    path('remove/<int:id>/',views.removeproduct,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkoutdetails/',views.checkoutdetail,name='checkoutdetail'),
    path('paypalsuccess',views.paypalsuccess,name='paypalsuccess'),
    path('paypalfailed',views.paypalfailed,name='paypalfailed'),
    path('orders/',views.orders,name='orders'),
    path('drf_crud/',views.crudapi.as_view()),
    path('forgotpass/',views.forgotpassword,name='forgotpassword'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
]




