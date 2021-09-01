from django.contrib import admin
from django.urls import path
from . import views #.은 현재 같은 디렉토리를 의미. 같은 디렉토리에서 views.py를 가져와라

urlpatterns = [
    path('index/', views.index) #foods 앱 안의 views.py파일에서 index 함수를 가져와라
]