from django.urls import path,include
from floors.views import userapp


urlpatterns = [
    path('users/', userapp.as_view(), name='users'),

]