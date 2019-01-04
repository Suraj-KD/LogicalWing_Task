from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('', views.employee_list),
    path('<int:pk>', views.employee_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)