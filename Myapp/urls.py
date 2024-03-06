from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='Upload'),
    path('details/', views.details, name='details'),
    path('users/', views.users, name='users'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.upload, name='upload'),
    path('showimage/', views.showimages, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
