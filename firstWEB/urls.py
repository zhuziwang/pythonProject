from django.urls import path

from . import views

app_name = 'firstWEB'          # 这行不能少

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.CalList, name='CalList'),
]