# cvapp/urls.py
from django.urls import path
from .views import cv_list
from .views import create_cv
from .views import cv_detail
from .views import delete_cv
#from .views import signup_or_login

urlpatterns = [
    path('cv_list/', cv_list, name='cv_list'),
    path('create_cv/', create_cv, name='create_cv'),
    path('cv_detail/<int:cv_id>/', cv_detail, name='cv_detail'),
    path('delete_cv/<int:cv_id>/', delete_cv, name='delete_cv'),
    #path('signup_or_login/', signup_or_login, name='signup_or_login'),
    # Add more patterns as needed
]
