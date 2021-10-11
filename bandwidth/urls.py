
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('author/<name>', getauthor, name="author"),
    path('topic/<name>', getTopic, name="topic"),
    path('login/', getLogin, name="login"),
    path('logout/', getLogout, name="logout"),
    path('upgrade/', getUpgrade, name="upgrade"),
    path('downgrade/', getDowngrade, name="downgrade"),
    path('request/', getRequest, name="request"),
    path('profile/', getProfile, name="profile"),
    path('update/<int:id>', getUpdate, name="update")
]
