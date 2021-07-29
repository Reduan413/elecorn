from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('unit/', unit.list, name="inventory_unit"),
    path('unit/create/', unit.create, name="create_inventory_unit"),
    path('unit/edit/', unit.edit, name="edit_inventory_unit"),

    path('inventory_category/list/', category.list, name="inventory_category_list"),
    path('inventory_category/create/', category.create, name="inventory_category_create"),
    path('inventory_category/edit/', category.edit, name="inventory_category_edit"),

    path('inventory_sub_category/list/', sub_category.list, name="inventory_sub_category_list"),
    path('inventory_sub_category/create/', sub_category.create, name="create_inventory_sub_category"),
    path('inventory_sub_category/edit/', sub_category.edit, name="edit_inventory_sub_category"),

    path('inventory_brand/list/', brand.list, name="inventory_brand_list"),
    path('inventory_brand/code_checking/', brand.checking_code, name="code_checking_inventory_brand"),
    path('inventory_brand/create/', brand.create, name="create_inventory_brand"),
    path('inventory_brand/edit/', brand.edit, name="edit_inventory_brand"),

    path('inventory_locator_name/list/', locator_name.list, name="inventory_locator_name_list"),
    path('inventory_locator_name/create/', locator_name.create, name="inventory_locator_name_create"),
    path('inventory_locator_name/edit/', locator_name.edit, name="inventory_locator_name_edit"),

    path('inventory_segment/list/', segment.list, name="inventory_segment_list"),
    path('inventory_segment/create/', segment.create, name="inventory_segment_create"),
    path('inventory_segment/edit/', segment.edit, name="inventory_segment_edit"),

    path('inventory_product/list/', product.list, name="inventory_product_list"),
    path('inventory_product/create/', product.create, name="create_inventory_product"),

    # Warehouse URL
    path('warehouse_room/list/', warehouse_room.list, name="warehouse_room_list"),
    path('warehouse_room/create/', warehouse_room.create, name="warehouse_room_create"),
    path('warehouse_room/edit/', warehouse_room.edit, name="warehouse_room_edit"),

    path('warehouse_rack/list/', warehouse_rack.list, name="warehouse_rack_list"),
    path('warehouse_rack/create/', warehouse_rack.create, name="warehouse_rack_create"),
    path('warehouse_rack/edit/', warehouse_rack.edit, name="warehouse_rack_edit"),

    path('warehouse_bin/list/', warehouse_bin.list, name="warehouse_bin_list"),
    path('warehouse_bin/create/', warehouse_bin.create, name="warehouse_bin_create"),
    path('warehouse_bin/edit/', warehouse_bin.edit, name="warehouse_bin_edit"),

    path('warehouse_bin/list/', warehouse_bin.list, name="warehouse_bin_list"),
    path('warehouse_bin/create/', warehouse_bin.create, name="warehouse_bin_create"),
    path('warehouse_bin/edit/', warehouse_bin.edit, name="warehouse_bin_edit"),

    path('warehouse_box/list/', warehouse_box.list, name="warehouse_box_list"),
    path('warehouse_box/create/', warehouse_box.create, name="warehouse_box_create"),
    path('warehouse_box/edit/', warehouse_box.edit, name="warehouse_box_edit"),

    path('warehouse_type/list/', warehouse_type.list, name="warehouse_type_list"),
    path('warehouse_type/create/', warehouse_type.create, name="warehouse_type_create"),
    path('warehouse_type/edit/', warehouse_type.edit, name="warehouse_type_edit"),

    path('warehouse/list/', warehouse.list, name="warehouse_list"),
    path('warehouse/create/', warehouse.create, name="warehouse_create"),
    path('warehouse/edit/', warehouse.edit, name="warehouse_edit"),




]
