# saas_rbac/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import HttpResponse

# Root view for friendly landing page
def index(request):
    return HttpResponse(
        '<h1>SaaS RBAC API</h1>'
        '<p>Visit <a href="/api/docs/">API Docs</a> or <a href="/admin/">Admin Panel</a>.</p>',
        content_type="text/html",
        status=200
    )

urlpatterns = [
    path('', index, name='home'),  # ← Friendly root page
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/auth/', include('accounts.urls')),
    path('api/orgs/', include('organizations.urls')),
    path('api/', include('roles.urls')),
    path('api/audit-logs/', include('auditlogs.urls')),
    path('api/', include('invitations.urls')),
]