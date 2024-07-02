from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('hello/', views.hello, name='hello'),
    path('callback/', views.oauth_callback, name='oauth_callback'),
]
