from django.urls import path
from company import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Company Modules > Company
    path('company_list/', views.company_manager.company_list, name='company_list'),
    path('create_company/', views.company_manager.create_company, name='create_company'),
    path('edit_company/', views.company_manager.edit_company, name='edit_company'),
    
    # Company Modules > Cost Center
    path('create_cost_center/', views.costcenter_manager.create_cost_center, name='create_cost_center'),
    path('edit_cost_center/', views.costcenter_manager.edit_cost_center, name='edit_cost_center'),
    
    # Company Modules > Cost Center
    path('create_department/', views.department_manager.create_department, name='create_department'),
    path('edit_department/', views.department_manager.edit_department, name='edit_department'),

    path('unit_manager/', views.unit_manager, name='unit_manager'),
]
