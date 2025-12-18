from django.urls import path
from .views import InviteUserView

urlpatterns = [
    path('<int:org_id>/invite/', InviteUserView.as_view(), name='invite-user'),
]
