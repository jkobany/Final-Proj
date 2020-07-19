from django.db import models
from django.contrib.auth.models import User
from django import forms
from multiselectfield import MultiSelectField
from splitjson.widgets import SplitJSONWidget



productMaintenanceAlerts_CATALOG = [
    ('SMS', 'SMS'),
    ('Email', 'Email'),
    ('Notification', 'Notification'),
]

# Create your models here.
class Device(models.Model):
    deviceName = models.TextField(blank=True)
    dateBought = models.DateField(blank=True)
    warranty = models.ImageField(null=True)
    ensuredBy = models.CharField(max_length=1024 , null=True)
    insuranceEndDate = models.DateField(blank=True)
    productMaintenanceAlerts = MultiSelectField(choices=productMaintenanceAlerts_CATALOG,
                                                default='code',  max_choices=3, min_choices=0, blank=True, null=True)


class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    image = models.ImageField(upload_to='Users/Images', blank=True)

    def _str_(self):
        return self.user.__str__