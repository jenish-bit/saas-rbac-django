
from rest_framework import permissions
from django.core.cache import cache
from .models import Membership

class HasOrgPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        org_id = view.kwargs.get('org_id') or view.kwargs.get('pk') or request.data.get('organization')
        if not org_id:
            return False

        cache_key = f"user_perms_{request.user.id}_{org_id}"
        perms = cache.get(cache_key)

        if perms is None:
            try:
                membership = Membership.objects.get(
                    user=request.user,
                    organization_id=org_id,
                    status=Membership.Status.ACTIVE
                )
                perms = list(membership.role.permissions)
                cache.set(cache_key, perms, timeout=300)
            except Membership.DoesNotExist:
                return False

        required_perm = getattr(view, 'required_permission', None)
        if not required_perm:
            return True

        return required_perm in perms