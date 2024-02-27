from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('category/',category,name='category'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('savedata/',savedata,name='savedata'),
    path('dashlogin/',dashlogin,name='dashlogin'),
    path('query/',query,name='query'),
    # path('showdata/',showdata,name='showdata'),
    path('showdata/<str:pk>',showdata,name='showdata'),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update'),
    # path('search/<str:pk>',search,name='search')
]