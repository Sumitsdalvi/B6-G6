from django.http import HttpResponse
from django.views import View

class Home_CBV(View):
    def get(self, request):
        print("In GET mrthod...") 
        return HttpResponse("in GET method....")

    def post(self, request):
        print("In POST method...") 
        return HttpResponse("in POST method....", status = 201)

    def delete(self, request):
        print("In DELETE method...") 
        return HttpResponse("in DELETE method....", status = 204)

    def patch(self, request):
        print("In PUT method...") 
        return HttpResponse("in PUT method....")

from django.views.generic.base import TemplateView
class CBV_TemplateView_form_home(TemplateView):
    # extra_context = {"Value": "Sumit"}  # Pass single value
    # extra_context = {"form": BookMyForm()}   # pass form to page
    template_name = 'home_templateView.html'

