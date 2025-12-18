from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import HasOrgPermission
from .serializers import RoleSerializer
from .models import Role
from organizations.models import Organization

class RoleCreateView(APIView):
    permission_classes = [IsAuthenticated, HasOrgPermission]
    required_permission = "can_manage_roles"

    def post(self, request, org_id):
        try:
            org = Organization.objects.get(id=org_id, is_deleted=False)
        except Organization.DoesNotExist:
            return Response({"error": "Organization not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=org)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
