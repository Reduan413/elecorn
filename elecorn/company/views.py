from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from company.forms import *
from company.models import *


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if username == 'admin' and password == 'admin':
            return redirect('admin_dashboard')
        else:
            messages.info(request, 'Login Failed')
            return redirect('admin_login')

    return render(request, 'company/admin_login.html')


# Company Modules
def admin_dashboard(request):
    return render(request, 'company/admin_dashboard.html')

class company_manager:
    def company_list(request):
        return render(request, 'company/company_list.html')


    def create_company(request):
        return render(request, 'company/create_company.html')


    def edit_company(request):
        return render(request, 'company/create_company.html')


class costcenter_manager:
    def create_cost_center(request):
        return render(request, 'company/create_cost_center.html')

    def edit_cost_center(request):
        return render(request, 'company/create_cost_center.html')

    def delete_cost_center(request):
        return render(request, 'company/delete_cost_center.html')


class department_manager:
    def create_department(request):
        return render(request, 'company/create_department.html')

    def edit_department(request):
        return render(request, 'company/cost_center_department.html')

    def delete_department(request):
        return render(request, 'company/cost_center_department.html')


def unit_manager(request):
    return render(request, 'company/unit_manager.html')
