from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.homeView , name='home' ),
    path('ebayfeescaclulatore/', views.fesscalc , name='feescalc' ),
    path('signup/', views.SignupVeiw , name='signup' ),
    path('Login/', views.LoginVeiw , name='login' ),
    path('Logout/', views.LogOutVeiw , name='logout' ),
]