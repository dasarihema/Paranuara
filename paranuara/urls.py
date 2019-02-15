"""paranuara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/<int:company_id>', views.get_people_in_company, name='c1'),
    path('api/companies/<str:company_name>', views.get_company_id, name='c2'),
    path('api/people/<str:people1>&<str:people2>', views.get_people_info, name='p1'),
    path('api/people/<str:people1>', views.get_favourite_fruits_and_vegetables, name='f1')

]
