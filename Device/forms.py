from django import forms
from django.forms import ModelForm
from .models import Device, productMaintenanceAlerts_CATALOG
from splitjson.widgets import SplitJSONWidget

class DeviceForm(forms.ModelForm):
    deviceName = forms.CharField(widget= forms.TextInput())
    productMaintenanceAlerts= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                        choices=productMaintenanceAlerts_CATALOG)
    class Meta:
        model = Device
        fields = ['deviceName' , 'dateBought','ensuredBy' , 'insuranceEndDate' , 'productMaintenanceAlerts' ]

