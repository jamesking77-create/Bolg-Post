from django.urls import path

from blogger import views

urlpatterns = [

    path('welcome/', views.welcome, name='welcome_page'),
    path('about/', views.about, name='blog_about'),
    path('say_hello/', views.say_hello, name='blog_say_hello')
]