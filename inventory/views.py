from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import datetime
from django.contrib import messages
from .models import *
from company.models import *


# Create your views here.

# Dashboard for Company (Admin)
class unit:
    def list(request):
        display_unit = Unit.objects.all()

        context = {'display_unit': display_unit}
        return render(request, 'unit.html', context)

    def checking_code(request):
        if request.is_ajax and request.POST:
            code = request.POST.get('code')
            checking_data = Unit.objects.filter(code=code).exists()
            if checking_data:
                return JsonResponse({'status': 0})
            else:
                return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 'Failed'})

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Unit.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Unit.objects.values())
                context = {'status': 1, 'unit_data': unit_data}
                return JsonResponse(context)
            elif not edit_id:
                if Unit.objects.filter(code=code).exists() or Unit.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Unit.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Unit.objects.values())
                    context = {'status': 1, 'unit_data': unit_data}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Unit.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class category:
    def list(request):
        display_unit = Category.objects.all()

        last_id = Category.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 1001

        context = {'display_unit': display_unit, 'last_code': last_code}
        return render(request, 'inventory_category.html', context)

    def checking_code(request):
        if request.is_ajax and request.POST:
            code = request.POST.get('code')
            checking_data = Category.objects.filter(code=code).exists()
            if checking_data:
                return JsonResponse({'status': 0})
            else:
                return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 'Failed'})

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            last_id = Category.objects.all().order_by('id').last()
            last_code = None
            if last_id:
                last_code = int(last_id.code) + 1
            else:
                last_code = 1001

            if edit_id:
                load_data = Category.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Category.objects.values())
                context = {'status': 1, 'unit_data': unit_data,
                           'last_code': last_code}
                return JsonResponse(context)
            elif not edit_id:
                if Category.objects.filter(code=code).exists() or Category.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Category.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Category.objects.values())
                    context = {'status': 1, 'unit_data': unit_data,
                               'last_code': last_code}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Category.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class sub_category:
    def list(request):
        display_unit = Sub_Category.objects.all()

        last_id = Sub_Category.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 1001

        context = {'display_unit': display_unit, 'last_code': last_code}
        return render(request, 'inventory_sub_category.html', context)

    def checking_code(request):
        if request.is_ajax and request.POST:
            code = request.POST.get('code')
            checking_data = Sub_Category.objects.filter(code=code).exists()
            if checking_data:
                return JsonResponse({'status': 0})
            else:
                return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 'Failed'})

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            last_id = Sub_Category.objects.all().order_by('id').last()
            last_code = None
            if last_id:
                last_code = int(last_id.code) + 1
            else:
                last_code = 1001

            if edit_id:
                load_data = Sub_Category.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Sub_Category.objects.values())
                context = {'status': 1, 'unit_data': unit_data,
                           'last_code': last_code}
                return JsonResponse(context)
            elif not edit_id:
                if Sub_Category.objects.filter(code=code).exists() or Sub_Category.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Sub_Category.objects.create(
                        code=code, name=name)
                    load_data.save()
                    unit_data = list(Sub_Category.objects.values())
                    context = {'status': 1, 'unit_data': unit_data,
                               'last_code': last_code}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Sub_Category.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class brand:
    def list(request):
        display_unit = Brand.objects.all()

        last_id = Brand.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 1001

        context = {'display_unit': display_unit, 'last_code': last_code}
        return render(request, 'inventory_brand.html', context)

    def checking_code(request):
        if request.is_ajax and request.POST:
            code = request.POST.get('code')
            checking_data = Brand.objects.filter(code=code).exists()
            if checking_data:
                return JsonResponse({'status': 0})
            else:
                return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 'Failed'})

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            last_id = Brand.objects.all().order_by('id').last()
            last_code = None
            if last_id:
                last_code = int(last_id.code) + 1
            else:
                last_code = 1001

            if edit_id:
                load_data = Brand.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Brand.objects.values())
                context = {'status': 1, 'unit_data': unit_data, 'last_code': last_code}
                return JsonResponse(context)
            elif not edit_id:
                if Brand.objects.filter(code=code).exists() or Brand.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Brand.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Brand.objects.values())
                    context = {'status': 1, 'unit_data': unit_data,
                               'last_code': last_code}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Brand.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class type:
    def list(request):
        return render(request, 'type.html')


class locator_name:
    def list(request):
        display_data = Locator_Name.objects.all()

        context = {'display_data': display_data}
        return render(request, 'inventory_locator_name.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get('edit_id')
            name = request.POST.get('name')
            print(edit_id)
            if edit_id:
                save_data = Locator_Name.objects.get(id=edit_id)
                save_data.name = name
                save_data.save()
                display_data = list(Locator_Name.objects.values())
                context = {'status': 3, 'display_data': display_data}
                return JsonResponse(context)
            else:
                if Locator_Name.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Locator_Name.objects.create(name=name)
                    save_data.save()
                    display_data = list(Locator_Name.objects.values())

                    context = {'status': 1, 'display_data': display_data, }
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.is_ajax and request.method == "POST":
            id = request.POST.get("id")
            get_data = Locator_Name.objects.get(pk=id)

            context = {"id": get_data.id, "name": get_data.name}
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class segment:
    def list(request):
        display_data = Segment.objects.all()

        context = {'display_data': display_data}
        return render(request, 'inventory_segment.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get('edit_id')
            name = request.POST.get('name')
            print(edit_id)
            if edit_id:
                save_data = Segment.objects.get(id=edit_id)
                save_data.name = name
                save_data.save()
                display_data = list(Segment.objects.values())
                context = {'status': 3, 'display_data': display_data}
                return JsonResponse(context)
            else:
                if Segment.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Segment.objects.create(name=name)
                    save_data.save()
                    display_data = list(Segment.objects.values())

                    context = {'status': 1, 'display_data': display_data, }
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.is_ajax and request.method == "POST":
            id = request.POST.get("id")
            get_data = Segment.objects.get(pk=id)

            context = {"id": get_data.id, "name": get_data.name}
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


class product:
    def list(request):
        display_data = Product.objects.all()
        display_segment = Segment.objects.all()
        display_locator_name = Locator_Name.objects.all()
        context = {'display_data': display_data}
        return render(request, 'inventory_product_list.html', context)

    def create(request):
        last_id = Product.objects.all().order_by('id').last()
        last_code = None
        if last_id:
            last_code = int(last_id.code) + 1
        else:
            last_code = 10001

        display_unit = Unit.objects.all()
        display_category = Category.objects.all()
        display_sub_category = Sub_Category.objects.all()
        display_brand = Brand.objects.all()
        display_segment = Segment.objects.all()
        display_locator_name = Locator_Name.objects.all()
        display_company = Company.objects.all()

        context = {'last_code': last_code, 'display_unit': display_unit,
                   'display_category': display_category, 'display_sub_category': display_sub_category,
                   'display_brand': display_brand, 'display_segment': display_segment,
                   'display_locator_name': display_locator_name, 'display_company':display_company}

        if request.is_ajax and request.method == 'POST':
            unit_id = Unit.objects.only().get(id=request.POST.get('unit_id'))
            brand_id = Brand.objects.only().get(id=request.POST.get('brand_id'))
            segment_id = Segment.objects.only().get(id=request.POST.get('segment_id'))
            category_id = Category.objects.only().get(id=request.POST.get('category_id'))
            sub_category_id = Sub_Category.objects.only().get(id=request.POST.get('category_id'))
            company_id = Company.objects.only().get(id=request.POST.get('company_id'))
            save_data = Product.objects.create(code=request.POST.get('code'), part_no=request.POST.get('part_no'), market_name=request.POST.get('market_name'), model_no=request.POST.get('model_no'), unit_id=unit_id, brand_id=brand_id, segment_id=segment_id, category_id=category_id, sub_category_id=sub_category_id,
                                               description=request.POST.get('description'), barcode_type=request.POST.get('barcode_type'), sku_no=request.POST.get('sku_no'), alert_quantity=request.POST.get('alert_quantity'), narration=request.POST.get('narration'), selling_price=request.POST.get('selling_price'), purchase_price=request.POST.get('purchase_price'), company_id=company_id)

            save_data.clean()
            save_data.save()
            context = {'status': 1}
            return JsonResponse(context)

        else:
            return render(request, 'inventory_create_product.html', context)



# Warehouse Management

class warehouse_room:
    def list(request):
        display_data = Warehouse_Room.objects.all()

        context = {'display_data': display_data,}
        return render(request, 'warehouse_room.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse_Room.objects.get(id=edit_id)
                load_data.name = name
                load_data.save()
                load_data = list(Warehouse_Room.objects.values())
                context = {'status': 1, 'load_data': load_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse_Room.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Warehouse_Room.objects.create(name=name)
                    save_data.clean()
                    save_data.save()
                    load_data = list(Warehouse_Room.objects.values())
                    context = {'status': 1, 'load_data': load_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_data = Warehouse_Room.objects.get(pk=id)
            context = {"id": get_data.id, "name": get_data.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

class warehouse_rack:
    def list(request):
        display_data = Warehouse_Rack.objects.all()

        context = {'display_data': display_data,}
        return render(request, 'warehouse_rack.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse_Rack.objects.get(id=edit_id)
                load_data.name = name
                load_data.save()
                load_data = list(Warehouse_Rack.objects.values())
                context = {'status': 1, 'load_data': load_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse_Rack.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Warehouse_Rack.objects.create(name=name)
                    save_data.clean()
                    save_data.save()
                    load_data = list(Warehouse_Rack.objects.values())
                    context = {'status': 1, 'load_data': load_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_data = Warehouse_Rack.objects.get(pk=id)
            context = {"id": get_data.id, "name": get_data.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

class warehouse_bin:
    def list(request):
        display_data = Warehouse_Bin.objects.all()

        context = {'display_data': display_data,}
        return render(request, 'warehouse_bin.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse_Bin.objects.get(id=edit_id)
                load_data.name = name
                load_data.save()
                load_data = list(Warehouse_Bin.objects.values())
                context = {'status': 1, 'load_data': load_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse_Bin.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Warehouse_Bin.objects.create(name=name)
                    save_data.clean()
                    save_data.save()
                    load_data = list(Warehouse_Bin.objects.values())
                    context = {'status': 1, 'load_data': load_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_data = Warehouse_Bin.objects.get(pk=id)
            context = {"id": get_data.id, "name": get_data.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})



class warehouse_box:
    def list(request):
        display_data = Warehouse_Box.objects.all()

        context = {'display_data': display_data,}
        return render(request, 'warehouse_box.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse_Box.objects.get(id=edit_id)
                load_data.name = name
                load_data.save()
                load_data = list(Warehouse_Box.objects.values())
                context = {'status': 1, 'load_data': load_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse_Box.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    save_data = Warehouse_Box.objects.create(name=name)
                    save_data.clean()
                    save_data.save()
                    load_data = list(Warehouse_Box.objects.values())
                    context = {'status': 1, 'load_data': load_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_data = Warehouse_Box.objects.get(pk=id)
            context = {"id": get_data.id, "name": get_data.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

class warehouse_type:
    def list(request):
        display_unit = Warehouse_Type.objects.all()

        context = {'display_unit': display_unit,}
        return render(request, 'warehouse_type.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse_Type.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Warehouse_Type.objects.values())
                context = {'status': 1, 'unit_data': unit_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse_Type.objects.filter(code=code).exists() or Warehouse_Type.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Warehouse_Type.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Warehouse_Type.objects.values())
                    context = {'status': 1, 'unit_data': unit_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Warehouse_Type.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

class warehouse:
    def list(request):
        display_unit = Warehouse.objects.all()

        context = {'display_unit': display_unit,}
        return render(request, 'warehouse.html', context)

    def create(request):
        if request.is_ajax and request.method == "POST":
            edit_id = request.POST.get("pk")
            code = request.POST.get('code')
            name = request.POST.get('name')
            print(edit_id)

            if edit_id:
                load_data = Warehouse.objects.get(id=edit_id)
                load_data.code = code
                load_data.name = name
                load_data.save()
                unit_data = list(Warehouse.objects.values())
                context = {'status': 1, 'unit_data': unit_data,}
                return JsonResponse(context)
            elif not edit_id:
                if Warehouse.objects.filter(code=code).exists() or Warehouse.objects.filter(name=name).exists():
                    return JsonResponse({'status': 2})
                else:
                    load_data = Warehouse.objects.create(code=code, name=name)
                    load_data.save()
                    unit_data = list(Warehouse.objects.values())
                    context = {'status': 1, 'unit_data': unit_data,}
                    return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})

    def edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            get_unit = Warehouse.objects.get(pk=id)
            context = {"id": get_unit.id,
                       "code": get_unit.code, "name": get_unit.name}
            # stud = User.objects.values()
            # student_data = list(stud)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 0})


