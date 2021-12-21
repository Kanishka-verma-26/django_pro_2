from django.urls import path
from AppTwo import views

urlpatterns=[
    path('',views.fir_func,name='fir_func'),
]

