from django.urls import path
from student.views import data,req_sucess
urlpatterns = [
    path('req/',data,name='data'),
    path('success/',req_sucess,name='req_sucess'),
]