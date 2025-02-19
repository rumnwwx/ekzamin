from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.UserProfileListView.as_view(), name='profile'),
    path('catalog/', views.catalog, name='catalog')
]