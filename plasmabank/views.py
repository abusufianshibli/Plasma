from django.shortcuts import render, HttpResponseRedirect,redirect
from .models import Account,PlasmaDonor
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def home(request):

    allDonor = PlasmaDonor.objects.all
    
    context = {
        'allDonor': allDonor
    }
    return render(request,'index.html',context)
def singin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = authenticate(phone=phone,password=password)

        if user is not None:
            auth_login(request,user)
            print("login")
            return redirect('profile')
        else:
            print("User invalid")
            return redirect('singin')    

    else:
        return render(request,'singin.html')           

def loginCheck(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'singin.html')

def register(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        if Account.objects.filter(phone = phone).exists():
            message = 'Account with this number Exists'
            messages.info(request,message)
            return render(request,'register.html')    
        else:
            if password == con_password:
                create = Account(
                phone = phone,
                password = password,
                con_password = con_password
                )
                create.save()
                message = 'Account Create'
                messages.success(request, message)
                return render(request,'singin.html') 
            else:
                message = 'Password are not same '
                messages.success(request, message)
                return render(request,'singin.html')       
    else:
        return render(request,'register.html')


def profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('blood_group')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        donor = PlasmaDonor(
            name=name,
            blood_group=blood_group,
            phone=phone,
            address = address,
            status = True,
            created_date = datetime.now()
        )
        donor.save()
        print("data save")
        return redirect('home')
    else:
        return render(request,'profile.html')