from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('incident_category/list/', incident_category.list, name="incident_category_list"),
    path('incident_category/create/', incident_category.create, name="incident_category_create"),
    path('incident_category/edit/', incident_category.edit, name="incident_category_edit"),

    path('repair_request/create/', repair_request.create, name="repair_request_create"),
    path('repair_request/list/', repair_request.list, name="repair_request_list"),
    path('repair_request/edit/<int:pk>/', repair_request.edit_view, name="repair_request_edit"),

    path('repair_request/assign/<int:pk>/', repair_request.assign_view, name="repair_request_assign"),
    path('repair_request/assign/post/', repair_request.assign_post, name="repair_request_assign_post"),

    #Engineer Section
    path('engineer/assigned/list/', engineer_room.list, name="engineer_assigned_list"),
    path('engineer/assigned/work/<int:pk>/', engineer_room.work, name="engineer_work"),
    path('engineer/repair_report', engineer_room.repair_report, name="engineer_repair_report"),


]
