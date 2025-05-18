from django.db import models
from user.models import CustomUser
from .store import Store

class StoreOwnerProfile(models.Model):
    # Изменили related_name на 'store_profile' для связи с CustomUser
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='store_onwer_profile')  
    # Изменили related_name на 'owner_profile' для связи с Store
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='store_owner_profile')  

    def __str__(self):
        return f"{self.user.username}'s Profile"
