from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('hello/', views.hello, name='hello'),
    path('callback/', views.oauth_callback, name='oauth_callback'),
    path('create_channel/', views.create_channel, name='create_channel'),
    path('check_token/', views.check_token, name='check_token'),

]
