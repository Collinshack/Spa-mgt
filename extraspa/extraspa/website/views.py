from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import GenerateKey, GenerateElect
from.models import PaperGen, ElectGen
from django.conf import settings
import random
import qrcode
import time

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)


def home(request):
    paper = PaperGen.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in")
            return redirect('home')
        else:
            messages.success(request, "Error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': paper})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = PaperGen.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You must be logged in')

def physical_generate(request):
    datap= str(random.randint(99999, 999999))
    form = GenerateKey(request.POST or None, initial={'unique': datap})
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                notekey = f"key is {form.cleaned_data['unique']}"
                messages.success(request, notekey)
                add_record = form.save()
                return redirect('phygenerate')
        return render(request,'phygenerate.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('phygenerate')


def electric_service(request):
    if request.user.is_authenticated:
        return render(request, 'electric_service.html')

def electric_sum(request):
    datat = str(random.randint(99999,999999))
    form = GenerateElect(request.POST or None, initial={'uniquec': datat})

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()  # Save the form data to the database
                return redirect('qrdisplay')  # Redirect to a success page
        return render(request, 'electric_sum.html', {'form': form})
    else:
        form = GenerateElect()
        return render(request, 'electric_sum.html', {'form': form})

def qrcode_sum(request):
    latest_entry = ElectGen.objects.latest('uniquec')  # Retrieve the latest entry from the database
    if request.user.is_authenticated:
        if request.method == "GET":

            qr.add_data(latest_entry.uniquec)
            qr.make(fit=True)

            # Generate the QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")
            path = 'static/mysite/images/qrcode.png'
            # Save the image
            qr_image.save(path)

            return render(request, 'qrdisplay.html', {'data': latest_entry.uniquec})
        #return render(request, 'qrdisplay.html', {'data': latest_entry.uniquec})
