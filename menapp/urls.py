from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns=[ 
    path('login/',LoginView.as_view(),name="login"),
    path('menu/',views.menu,name="menu"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('cuestionario/',views.cuestionario,name="cuestionario"),
    path('pregunta2/',views.pregunta2,name='pregunta2'),
    path('pregunta3/',views.pregunta3,name='pregunta3'),
    path('pregunta4/',views.pregunta4,name='pregunta4'),
    path('pregunta5/',views.pregunta5,name='pregunta5'),
    path('pregunta6/',views.pregunta6,name='pregunta6'),
    path('pregunta7/',views.pregunta7,name='pregunta7'),
    path('deba/',views.deba,name='deba'),
    path('temporizador/',views.temporizador,name='temporizador'),
    path('imp/',views.imp,name='imp'),
    path('mapa/',views.mapa,name='mapa'),
    path('acti/',views.acti,name='acti'),
    path('resu/',views.resu,name='resu'),
    path('hoja/',views.hoja,name='hoja'),
    path('pomodoro/',views.pomodoro,name='pomodoro'),
    path('inv/',views.inv,name='inv'),
    path('pri/',views.pri,name='pri'),
    path('se/',views.se,name='se'),
    path('flas/',views.flas,name='flas'),
    path('resumen/',views.resumen,name='resumen'),
    path('nuevoresumen/',views.nuevoresumen,name='nuevoresumen'),
]