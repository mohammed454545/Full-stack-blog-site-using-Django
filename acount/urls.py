from django.urls import path
from . import views
urlpatterns=[
    path('',views.profile,name= 'profile'),
    path('/sign in',views.sign_in,name= 'sign_in'),
    path('/logout',views.logout,name= 'logout'),
    path('/sign up',views.sign_up,name= 'sign_up'),
]