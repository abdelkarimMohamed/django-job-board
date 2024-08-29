from django.urls import path
from . import views

urlpatterns=[
    path('',views.jon_list,name='jon_list'),
    path('<int:id>',views.job_detail,name='job_detail'),
]