from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index,name='Index'),
    path('signup/',view=views.signup,name='signup'),
    path('signupSubmit/',view=views.signupSubmit,name='signupSubmit'),
    path('test/',view=views.testPage,name="test"),
    path('loginBtn',view=views.loginSubmit,name="loginBtn"),
    path('addProduct/',view=views.addProduct,name="addProduct"),
    path('viewItems/',view=views.viewItems,name="viewItems"),
    path('adminCart/',view=views.adminCart,name="adminCart"),
    path('logout/',view=views.logout,name='logout'),
    path('Checkout/',view=views.checkout,name="Checkout"),
    path('submit/',view=views.checkOutSubmit,name="submit"),
    path('UserHistory/',view=views.UserHistory,name="UserHistory"),
    path('profile/',view=views.profile,name="profile"),
    path('updateProfile/' ,view=views.updateProfile,name="updateProfile"),
    path('submitUpdate/',view=views.submitUpdate,name="submitUpdate"),
    path('updateqty/',view=views.updateQty,name="updateQty"),
    path('search/',view=views.searchOptions,name="search")
    ]
