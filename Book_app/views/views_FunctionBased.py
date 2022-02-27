from msilib.schema import SelfReg
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Book_app.forms import BookMyForm
from django.contrib import messages
from django.views import View
from Book_app.models import Employee
# Create your views here.
def form_home(request):
    if request.method == "POST":
        Book_obj = BookMyForm(request.POST)
        if Book_obj.is_valid():
            Book_obj.save()
            print(Book_obj.cleaned_data["name"])
            messages.success(request, "Data Saved Successfully...!!!")
            return redirect("FormHome_FBV")
        else:
            return HttpResponse("Error...!!!")

    elif request.method == "GET":
        context1 = {"form" : BookMyForm()}
        return render(request, template_name="form_home.html", context=context1)

    else:
        return HttpResponse("Invalid response...!!!")


