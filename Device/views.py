import json

from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import DeviceForm
from .models import Device
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def homepage(request):
    devices = Device.objects.all()
    devices_json = [{"value": x.deviceName, "data":x.id} for x in devices]
    return render(request, 'Device/index.html/',{'devices':json.dumps(devices_json)})


def devices(request):
    if request.user.is_authenticated:
            devices = Device.objects.all()
            return render(request , "Device/devices.html", { 'username' : User.username, 'devices':devices})
    else: 
            return redirect("loginuser")

@login_required
def form(request):
    return render(request, 'Device/form.html')
    
def loginuser(request):
    if (request.method == 'GET'):
        return render(request, 'Device/loginuser.html', {'form': AuthenticationForm() })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'Device/loginuser.html', {'form': AuthenticationForm(), "errMsg": "User doesn't exist"})
        else :
            login(request, user)
            return redirect('devices')

@login_required
def createNewDevice(request):
    if request.method == 'GET':
        form = DeviceForm()
        return render(request, 'Device/form.html', {'form': form, 'action': '/create/'})
    else:
        try:
            form = DeviceForm(request.POST)
            print(form.is_valid())
            form.save()
            return redirect('devices')
        except ValueError:
            return render(request, 'Device/form.html', {'form': DeviceForm(), 'errMsg': 'Data mismatch'})

@login_required
def editDevice(request, device_id):
    device = Device.objects.get(id=device_id)
    print(device)
    print(device_id)
    if request.method == 'GET':
        print("2222222")
        return render(request, 'Device/form.html', {'form': DeviceForm(instance=device), 'action': '/devices/edit/{}'.format(device_id)})
    else:
        try:
            form = DeviceForm(request.POST, instance=device)
            print(form.is_valid())
            form.save()
            return redirect('devices')
        except ValueError:
            return render(request, 'Device/form.html', {'form': DeviceForm(), 'errMsg': 'Data mismatch'})


@login_required()
def deleteDevice(request, device_id):
    device = Device.objects.get(id=device_id)
    device.delete()
    return redirect('devices')
        #return render(request, 'Device/devices.html', {'form': DeviceForm(instance=device)})
