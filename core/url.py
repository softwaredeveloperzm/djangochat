from chat.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('fetch_users/<str:key>/', views.fetch_users, name="fetch_users"),
    path('user/<str:user_username>/', views.user_detail, name='user_detail'),
    path('fetch_messages/', views.fetch_messages, name='fetch_messages'),
    path('send', views.send, name='send'),

]