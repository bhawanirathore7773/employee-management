from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('emp_details',views.emp_details),
    path('add_emp', views.add_emp),
    path('filter_emp', views.filter_emp),
    path('remove_emp', views.remove_emp),
    path('remove_emp/<int:emp_id>', views.remove)
]