from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

# Dashboard for Company (Admin)

class dashboard:

    @login_required
    def admin(request):
        return render(request, 'admin_dashboard.html')


class company:

    @login_required
    def list(request):
        display_data = Company.objects.all()
        context = {'display_data': display_data}
        return render(request, 'company_list.html', context)

    @login_required
    def create(request):
        last_id = Company.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 101

        if request.is_ajax and request.method == 'POST':
            save_data = Company.objects.create(code=request.POST.get('code'), name=request.POST.get('name'),
                                               email=request.POST.get('email'),
                                               contact_no=request.POST.get('contact_no'),
                                               address=request.POST.get('address'),
                                               license_no=request.POST.get('license_no'))
            save_data.clean()
            save_data.save()
            context = {'status': 1}
            return JsonResponse(context)
        else:
            context = {'last_code': last_code}
            return render(request, 'create_company.html', context)


class cost_center:

    @login_required
    def list(request):
        table_data = Cost_Center.objects.all()
        company_data = Company.objects.all()

        last_id = Company.objects.all().order_by('id').last()
        next_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            next_code = 101

        context = {'table_data':table_data, 'company_data':company_data,'next_code':next_code}
        return render(request, 'cost_center.html', context)

    def create(request):
        pass

class department:

    @login_required
    def list(request):
        return render(request, 'department_list.html')
    @login_required
    def create_cost_center(request):
        pass


class user_information:
    @login_required
    def create(request):
        if request.method == 'POST':
            if request.POST["firstName"] and request.POST["lastName"] and request.POST["email"] and request.POST["userName"] and request.POST["password"] and request.POST["company"]:
                userInformation = UserInformation()
                userInformation.firstName = request.POST["firstName"]
                userInformation.lastName = request.POST["lastName"]
                userInformation.email = request.POST["email"]
                userInformation.userName = request.POST["userName"]
                userInformation.password = request.POST["password"]
                userInformation.save()
                userInformation.company.set(request.POST["company"])
                return redirect('/company/user_information')
        else:
            userinformations = UserInformation.objects.order_by('-id')
            companys = Company.objects
            
            return render(request, 'user_information.html', {'userinformations' : userinformations, 'companys' : companys})


    @login_required
    def update(request ,id):
        userinformations = UserInformation.objects.get(id=id)
        if request.method == 'POST':
                ufirstName = request.POST["firstName"]
                ulastName = request.POST["lastName"]
                uemail = request.POST["email"]
                uuserName = request.POST["userName"]
                upassword = request.POST["password"]
                ucompany = request.POST["company"]
                userinformations.firstName = ufirstName
                userinformations.lastName = ulastName
                userinformations.email = uemail
                userinformations.userName = uuserName
                userinformations.password = upassword
                userinformations.company = ucompany
                userinformations.save()
                messages.success(request, 'Updated Successfully!')
                return redirect('/company/user_information')

        else:
            userinformations = UserInformation.objects.get(pk=id)
            return render(request, 'edit_information.html', {'userinformations': userinformations})

    @login_required
    def delete(request, id):
        if request.method == 'POST':
            uid = UserInformation.objects.get(pk=id)
            uid.delete()
            return redirect('/company/user_information')
