from django.urls import path, re_path
from medicine import views

urlpatterns = [
    re_path('$', views.index, name='index'),
    re_path(r'(?P<medicine_type>\w+)/$', views.medicine, name='medicine'),
    re_path(r'add_medicine_type$', views.add_medicine_type, name='add_medicine_type'),
    re_path(r'(?P<medicine_type>\w+)/add_medicine_detail$', views.add_medicine_detail,
            name='add_medicine_detail'),
]