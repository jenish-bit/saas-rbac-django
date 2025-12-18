
from django.db import models
from common.models import BaseModel
from accounts.models import User
from organizations.models import Organization
import secrets

class Invitation(BaseModel):
    email = models.EmailField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=255, unique=True, default=secrets.token_urlsafe)

    def __str__(self):
        return f"Invitation to {self.email} for {self.organization.name}"