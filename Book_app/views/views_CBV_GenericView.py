#  Class Based View
from django.views.generic.edit import CreateView  
from django.views.generic.list import ListView  
from django.views.generic.detail import DetailView  
from django.views.generic import UpdateView  
from django.views.generic.edit import DeleteView  
from Book_app.models import Employee

class EmployeeCreate(CreateView):
    """This is createview which creates new employee with given details"""
    model = Employee
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/create/"

class EmployeeRetrieve(ListView):
    """This is ListView which retrieves all employee """
    model = Employee
    paginate_by = 6

    
class EmployeeDetail(DetailView):  
    """This is DetailView which retrieves an employee for given ID or PK"""
    model = Employee 

class EmployeeUpdate(UpdateView):  
    """This is UpdateView which updates an employee details for given ID or PK"""
    model = Employee 
    fields = '__all__'
    success_url = "http://127.0.0.1:8000/retrieve/"

  
class EmployeeDelete(DeleteView):  
    """This is DeleteView which deletes an employee for given ID or PK"""
    model = Employee 
    success_url = "http://127.0.0.1:8000/retrieve/"
    