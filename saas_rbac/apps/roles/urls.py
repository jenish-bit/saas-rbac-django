
from django.urls import path
from .views import RoleCreateView

urlpatterns = [
    path('<int:org_id>/roles/', RoleCreateView.as_view(), name='create-role'),
]