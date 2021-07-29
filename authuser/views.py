from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from .managers import *

from .models import User


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        return render(request, 'login.html')

    #  # if request.POST:  #     username = request.POST.get('username')  #     password = request.POST.get('password')  #  #     if username and password:  #         user = authenticate(username=username, password=password)  #  #         if user is not None:  #             print("Logged")  #             return redirect('admin_dashboard')  #         else:  #             print("Not Looged")  # else:  #     return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('admin_login')


class user_manage:
    def create_view(request):
        return render(request, 'create_user.html')

    def list(request):
        display_data = User.objects.all()
        context = {'display_data': display_data}
        return render(request, 'user_list.html', context)

    def create(request):
        if request.is_ajax and request.method == 'POST':
            if request.POST.get("edit_id"):
                get_data = User.objects.get(id=request.POST.get("edit_id"))
                get_data.first_name = request.POST.get("first_name")
                get_data.last_name = request.POST.get("last_name")
                get_data.username = request.POST.get("username")
                get_data.email = request.POST.get("email")
                get_data.contact_no = request.POST.get("contact_no")
                get_data.is_staff = True
                get_data.is_admin = True
                get_data.is_superuser = True
                get_data.set_password(request.POST.get("password"))
                get_data.save()
                context = {'status': 2}
                return JsonResponse(context)
            else:
                User.objects.create_user( first_name=request.POST.get("first_name"), last_name=request.POST.get("last_name"), username=request.POST.get("username"), password = request.POST.get("password"), email=request.POST.get("email"), contact_no=request.POST.get("contact_no"), is_staff=True, is_admin=True, is_superuser=True)
                context = {'status': 1}
                return JsonResponse(context)
        else:
            pass

    def edit(request, pk):
        display_data = User.objects.get(id=pk)
        context = {'display_data': display_data}
        return render(request, 'edit_user.html', context)
