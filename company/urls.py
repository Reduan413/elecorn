from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_dashboard', dashboard.admin, name="admin_dashboard"),
    path('company_list', company.list, name="company_list"),
    path('create_company', company.create, name="create_company"),

    path('cost_center_list', cost_center.list, name="cost_center_list"),
    path('cost_center_create', cost_center.create, name="cost_center_create"),
    # path('cost_center_edit', cost_center.create, name="cost_center_edit"),
    # path('cost_center_delete', cost_center.delete, name="cost_center_delete"),

    path('department_list', department.list, name="department_list"),
    path('user_information', user_information.create, name="user_information"),
    path('user_information/<int:id>/', user_information.update, name="update_user_information"),
    path('delete/<int:id>/', user_information.delete, name="delete_user_information"),

]
