
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import HasOrgPermission
from .tasks import send_invitation_email
from .models import Invitation
from organizations.models import Organization
import secrets

class InviteUserView(APIView):
    permission_classes = [IsAuthenticated, HasOrgPermission]
    required_permission = "can_invite_user"

    def post(self, request, org_id):
        email = request.data.get('email')
        if not email:
            return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            org = Organization.objects.get(id=org_id, is_deleted=False)
        except Organization.DoesNotExist:
            return Response({"error": "Organization not found"}, status=status.HTTP_404_NOT_FOUND)

        if Invitation.objects.filter(email=email, organization=org, is_accepted=False).exists():
            return Response({"error": "Invitation already sent"}, status=status.HTTP_400_BAD_REQUEST)

        token = secrets.token_urlsafe(32)
        invite = Invitation.objects.create(
            email=email,
            organization=org,
            invited_by=request.user,
            token=token
        )

        link = f"http://localhost:3000/accept-invite?token={token}"
        send_invitation_email.delay(email, org.name, link)

        return Response({"message": "Invitation sent"}, status=status.HTTP_201_CREATED)