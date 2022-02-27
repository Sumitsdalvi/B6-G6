from django import forms
from Book_app.models import Books,Employee

class BookMyForm(forms.ModelForm):
    """ This class creates form from model :- 'BOOKS' """
    class Meta:
        model = Books
        fields = "__all__"
        # exclude = ("qty",)   # If you want to exclude particular field

class EmployeeForm(forms.ModelForm):
    """ This class creates form from model :- 'EMPLOYEE' """
    class Meta:
        model = Employee
        fields = "__all__"
