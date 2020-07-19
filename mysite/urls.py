from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('delete',views.deleteacc,name='deleteaccount'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('handleSignup',views.handleSignup,name='handleSignup'),
    path('handleLogin',views.handleLogin,name='handleLogin'),
    path('handleLogout',views.handleLogout,name='handleLogout'),
    path('donateFood',views.donateFood,name='donateFood'),
    path('donateCloth',views.donateCloth,name='donateCloth'),
    path('chooseFoodCentre/<str:pk>/<str:no>/',views.chooseFoodCentre,name='chooseFoodCentre'),
    path('chooseClothCentre/<str:pk>/<str:no>/',views.chooseClothCentre,name='chooseClothCentre'),
]
