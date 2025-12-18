
from django.db import models
from common.models import BaseModel
from accounts.models import User

class Organization(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_orgs')

    def __str__(self):
        return self.name