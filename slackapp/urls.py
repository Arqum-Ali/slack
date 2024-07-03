from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('hello/', views.hello, name='hello'),
    path('callback/', views.oauth_callback, name='oauth_callback'),
    path('create_channel/', views.create_channel, name='create_channel'),
    path('list_channels/', views.list_channels, name='list_channels'),
    path('add_channel_member/', views.add_channel_member, name='add_channel_member'),
    path('remove_channel_member/', views.remove_channel_member, name='remove_channel_member'),
    path('get_channel_members/', views.get_channel_members, name='get_channel_members'),

]
