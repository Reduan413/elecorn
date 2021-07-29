from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_login/', admin_login , name="admin_login"),
    path('logout/', user_logout , name="logout"),
    path('create_user/', user_manage.create_view, name="create_user_view"),
    path('create_user_post/', user_manage.create, name="create_user"),
    path('list/', user_manage.list, name="user_list"),
    path('edit/<int:pk>', user_manage.edit, name="user_edit"),
]
