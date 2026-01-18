from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Earning, mapPointers, myBooking1, Previous
from django.contrib.auth import authenticate, login
from django.urls import reverse


def landingPage(request):
    return render(request,'landingPage.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip().lower()
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                Earning.objects.create(user=user, earning=0)
                return redirect('login')
        else:
            messages.info(request, 'password not same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')
    



def login(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password']
        user = authenticate(request, username=username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('display')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

    
def logout(request):
    auth.logout(request)
    return redirect('login')


def display(request):
    user = request.user
    return render(request, 'display.html')


def provider(request):
    if request.method == 'POST':
        curr = mapPointers()
        curr.user = request.user
        curr.photo = request.FILES['photo']
        curr.latitude = request.POST['latitude']
        curr.longitude = request.POST['longitude']
        curr.rate = request.POST['rate']
        curr.status = False
        curr.email = request.user.email
        curr.save()
        return redirect('pdashboard')
    else:
        return render(request, 'provider.html')
    

def profileShow(request):
    lists = mapPointers.objects.filter(user = request.user)
    return render(request, 'profileShow.html',locals())

def pdashboard(request):
    lists = mapPointers.objects.filter(user = request.user)
    earn = Earning.objects.get(user = request.user)
    return render(request,'pdashboard.html',locals())


def delLocation(request, pk=None):
    hw = get_object_or_404(mapPointers, id=pk)
    current_url = request.META.get('HTTP_REFERER')

    hw.delete()

    if 'pdashboard' in current_url:
        redirect_url = reverse('pdashboard')
    elif 'profile' in current_url:
        redirect_url = reverse('profile')
    else:
        redirect_url = reverse('display')

    return redirect(redirect_url)



def show(request):
    lists = mapPointers.objects.filter(user = request.user)
    return render(request, 'show.html',locals())

def need(request):
    lists = mapPointers.objects.all()
    return render(request, 'need.html',locals())


def redirecting(request):
    return render(request, 'redirecting.html')

def confirmed(request):
    return render(request, 'confirmed.html')

def profile(request):
    booked = myBooking1.objects.filter(user = request.user)
    myBookings = mapPointers.objects.filter(user = request.user)
    earn = Earning.objects.get(user = request.user)
    user = request.user
    try:
        past = Previous.objects.filter(user=request.user)
    except Previous.DoesNotExist:
        past = None
    return render(request, 'profile.html',locals())