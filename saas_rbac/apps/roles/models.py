
from django.db import models
from common.models import BaseModel
from accounts.models import User
from organizations.models import Organization

class Role(BaseModel):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='roles')
    permissions = models.JSONField(default=list)

    class Meta:
        unique_together = ('name', 'organization')

    def __str__(self):
        return f"{self.name} ({self.organization.name})"

class Membership(BaseModel):
    class Status(models.TextChoices):
        INVITED = 'invited'
        ACTIVE = 'active'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.INVITED)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.email} in {self.organization.name}"