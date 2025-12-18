
from django.db import models
from common.models import BaseModel
from accounts.models import User

class AuditLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_id = models.PositiveIntegerField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'Anonymous'} - {self.action}"