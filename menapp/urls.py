from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns=[ 
    path('login/',LoginView.as_view(),name="login"),
    path('menu/',views.menu,name="menu"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('cuestionario/',views.cuestionario,name="cuestionario"),
    path('cronometro/',views.cronometro,name="cronometro"),
    path('cronometroactivo/<pk>/',views.cronometroactivo,name='cronometroactivo'),
]