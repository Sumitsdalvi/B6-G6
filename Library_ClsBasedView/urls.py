"""Library_ClsBasedView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Book_app import views
from Book_app.views import EmployeeCreate,EmployeeRetrieve,EmployeeDetail,EmployeeUpdate,EmployeeDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form-home/',views.form_home , name="FormHome_FBV"),
    path('form-home-cbv/',views.Home_CBV.as_view() , name="FormHome_CBV"),
    path('',EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('FormHome-template-CBV/',views.CBV_TemplateView_form_home.as_view() , name="FormHome_template_CBV"),
    path('create/',EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/',EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('retrieve/<int:pk>/',EmployeeDetail.as_view(), name = 'EmployeeDetails'),
    path('update/<int:pk>/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'), 
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name = 'EmployeeDelete'),  


]
