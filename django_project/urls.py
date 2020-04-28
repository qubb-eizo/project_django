"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from test_app.views import hello
from test_app.views import requirements
from test_app.views import get_customers
from test_app.views import get_city_and_state
from test_app.views import fake_user
from test_app.views import turnover
from test_app.views import students
from test_app.views import gen_password
from test_app.views import orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', admin.site.urls),
    path('req/', requirements),
    path('distinct-name/', get_customers),
    path('city-and-state/', get_city_and_state),
    path('fake/', fake_user),
    path('turnover/', turnover),
    path('students/', students),
    path('password/', gen_password),
    path('orders/', orders)
]
