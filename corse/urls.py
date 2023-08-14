from django.urls import path
from . import views
urlpatterns=[
    path('<str:cor_id>',views.corse,name= 'corse'),
    path('',views.allcorses,name= 'allcorses'),
    path('/<int:lec_id>',views.lectuer,name= 'lectuer'),
]