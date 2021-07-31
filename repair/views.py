import datetime

from authuser.models import *
from company.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from inventory.models import *

from .models import *

# Create your views here.

# Dashboard for Company (Admin)

class incident_category:
    def list(request):
        display_unit = Incident_Category.objects.all()

        context = {'display_unit': display_unit, }
        return render(request, 'incident_category.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                if Incident_Category.objects.filter(code=code).exists() or Incident_Category.objects.filter(name=name).exists():
                    return JsonResponse({'status': 3})
                else:
                    load_data = Incident_Category.objects.get(id=edit_id)
                    load_data.code = code
                    load_data.name = name
                    load_data.save()
                    unit_data = list(Incident_Category.objects.values())
                    context = {'status': 1, 'unit_data': unit_data, }
                    return JsonResponse(context)
            elif not edit_id:
                if Incident_Category.objects.filter(code=code).exists() or Incident_Category.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Incident_Category.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Incident_Category.objects.values())
                    context = {'status': 1, 'unit_data': unit_data, }
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Incident_Category.objects.get(pk=id)
            context = {"id": get_unit.id, "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class repair_request:
    def list(request):
        display_data = Repair_Request.objects.all()
        context = { 'display_data': display_data }
        return render(request, 'repair_request_list.html', context)

    def create(request):
        last_id = Repair_Request.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 10001

        display_incident_category = Incident_Category.objects.all()
        display_brand = Brand.objects.all()

        context = {'last_code': last_code, 'display_incident_category': display_incident_category, 'display_brand': display_brand}

        if request.is_ajax and request.method == 'POST':
            if request.POST.get('data_id'):
                brand_id = Brand.objects.only().get(id=request.POST.get('brand_id'))
                incident_category_id = Incident_Category.objects.only().get(id=request.POST.get('incident_category_id'))
                print(request.POST.get('narrition'))
                save_data = Repair_Request.objects.update(code=request.POST.get('code'), date=request.POST.get('date'), device_name=request.POST.get('device_name'), part_no=request.POST.get('part_no'), serial_no=request.POST.get('serial_no'), model_no=request.POST.get('model_no'), brand_id=brand_id, incident_category_id=incident_category_id, details=request.POST.get('details'),service_type=request.POST.get('serviceType'),price=request.POST.get('price'), person_name=request.POST.get('person_name'), primary_contact_no=request.POST.get('primary_contact_no'), email=request.POST.get('email'), address=request.POST.get('address'), narrition=request.POST.get('narration'), status="Hold")

                save_data.clean()
                save_data.save()
                context = {'status': 1}
                return JsonResponse(context)

            else:
                brand_id = request.POST.get('brand_id')
                incident_category_id = request.POST.get('incident_category_id')
                save_data = Repair_Request.objects.create(code=request.POST.get('code'), date=request.POST.get('date'), device_name=request.POST.get('device_name'), part_no=request.POST.get('part_no'), serial_no=request.POST.get('serial_no'), model_no=request.POST.get('model_no'), brand_id=brand_id, incident_category_id=incident_category_id, details=request.POST.get('details'),service_type=request.POST.get('serviceType'),price=request.POST.get('price'), person_name=request.POST.get('person_name'), primary_contact_no=request.POST.get('primary_contact_no'), email=request.POST.get('email'), address=request.POST.get('address'), narrition=request.POST.get('narrition'), status="Hold")

                save_data.clean()
                save_data.save()
                context = {'status': 1}
                return JsonResponse(context)
        else:
            return render(request, 'repair_request_create.html', context)

    def edit_view(request, pk):
        print(pk)
        edit_view = Repair_Request.objects.get(id=pk)
        display_brand = Brand.objects.all()
        incident_category = Incident_Category.objects.all()
        print(edit_view)
        context = {"edit_view": edit_view, 'incident_category': incident_category, 'display_brand': display_brand}
        return render(request, 'repair_request_edit.html', context)

    def assign_view(request, pk):
        repair_data = Repair_Request.objects.get(id=pk)
        user_data = User.objects.all()
        context = {'repair_data': repair_data, 'user_data': user_data}
        return render(request, 'repair_request_assign.html', context)

    def assign_post(request):
        if request.is_ajax and request.method == 'POST':
            print(request.POST.get("repair_request_id"))
            print(request.POST.get("engineer_id"))
            print(request.POST.get("remarks"))
            item_instance = Repair_Request.objects.only().get(id=request.POST.get("repair_request_id"))
            engineer = User.objects.only().get(id=request.POST.get("engineer_id"))
            if Repair.objects.filter(item=request.POST.get("repair_request_id")).exists():
                context = {'status': 2}
                return JsonResponse(context)
            else:
                save_data = Repair.objects.create(item=item_instance, engineer=engineer, remarks=request.POST.get("remarks"))
                save_data.clean_fields()
                save_data.save()
                status_change = Repair_Request.objects.get(id=request.POST.get("repair_request_id"))
                status_change.status = "Pending"
                status_change.save()
                context = {'status': 1}
                return JsonResponse(context)


# Engineer Section

# Engineer Pending List
class engineer_room:
    def list(request):
        display_data = Repair.objects.filter(engineer=request.user.id)
        context = {'display_data':display_data}
        return render(request, 'engineer_assigned_list.html', context)

    def work(request, pk):
        return render(request, 'device_reparing.html')

    def repair_report(request):
        return render(request, 'engineer_reapir_report.html')
