from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.employee_form,name = 'employee_insert'),    #get and post request for insert operations
    path('<int:id>/',views.employee_form,name='employee_update'),  # get and post request for UPDATE operations
    path('list',views.employee_list, name = 'employee_list')        # get request to retirive and display all records.
    
]