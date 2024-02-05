from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ElectronicCardSumForm, ElectronicCardServiceForm, PhysicalCardSumForm, PhysicalCardServiceForm
from .models import ElectronicCardSum, ElectronicCardService, PhysicalCardService, PhysicalCardSum
from django.conf import settings
import qrcode
from PIL import Image
from io import BytesIO
from django.shortcuts import render
import os, io, base64
import random
import time
import string 
from django.template.loader import render_to_string



# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)



def home(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            electronic_gens_sum = ElectronicCardSum.objects.filter(spa=spa_admin)
            electronic_gens_service = ElectronicCardService.objects.filter(spa=spa_admin)
            context = {'electronic_cards_sum': electronic_gens_sum, 'electronic_cards_service': electronic_gens_service}
            return render(request, 'dashboard.html', context)
    return render(request, 'dashboard.html')




def electronic_card_service_records(request):
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            paper_gens_service = ElectronicCardService.objects.filter(spa=spa_admin)
            context = {'electronic_cards_service': paper_gens_service}
            return render(request, 'electronic_cards_service_records.html', context)
    return render(request, 'electronic_cards_service_records.html')







def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in")
            return redirect('dashboard')
        else:
            messages.success(request, "Error logging in")
            return redirect('login')
    else:
        return render(request, 'spa_admin_login.html')
    



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')






@login_required
def generate_physical_card_sum(request):
    datap= str(random.randint(99999, 999999))
    form = PhysicalCardSumForm(request.POST or None, initial={'uniquec': datap})
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                notekey = f"key is {form.cleaned_data['uniquec']}"
                messages.success(request, notekey)
                add_record = form.save()
                return redirect('generate_physical_card_sum')
        return render(request,'create_physical_card_sum.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('generate_physical_card_sum')






@login_required
def generate_physical_card_service(request):
    datap= str(random.randint(99999, 999999))
    form = PhysicalCardServiceForm(request.POST or None, initial={'uniquec': datap})
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                notekey = f"key is {form.cleaned_data['uniquec']}"
                messages.success(request, notekey)
                add_record = form.save()
                return redirect('generate_physical_card_service')
        return render(request,'create_physical_card_service.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('generate_physical_card_service')





    
@login_required
def generate_electronic_card_sum(request):
    if request.method == 'POST':
        form = ElectronicCardSumForm(request.POST)
        if form.is_valid():
            # Use the generated unique code from the form
            unique_code = form.cleaned_data['uniquec']
            form.save()  # This will save the unique code to the database
            return redirect('electronic_card_sum_display')
    else:
        # Generate a unique code only once for GET requests
        unique_code = str(random.randint(99999, 999999))
        while ElectronicCardSum.objects.filter(uniquec=unique_code).exists():  # Check for duplicates
            unique_code = str(random.randint(99999, 999999))  # Regenerate if duplicate found
        form = ElectronicCardSumForm(initial={'uniquec': unique_code})
    return render(request, 'create_electronic_card_sum.html', {'form': form})

@login_required
def electronic_card_sum_display(request):
    if request.method == 'GET':
        try:
            latest_entry = ElectronicCardSum.objects.latest('id')
            unique_code = latest_entry.uniquec  # Retrieve uniquec from the database

            card_image_path = "static/mysite/images/cards/cardd.jpg"
            card_image = Image.open(card_image_path)
            card_image = card_image.resize((350, 450))
            card_width, card_height = card_image.size
            combined_image = Image.new("RGB", (card_width, card_height))

            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
            qr.add_data(unique_code)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")

            center_x = card_width * 0.5
            center_y = card_height * 0.5
            right_offset = card_width * 0.25

            qr_size = min(card_width, card_height) * 0.2
            qr_x_offset = int(center_x + right_offset - qr_size / 2) + 13
            qr_y_offset = int(center_y - qr_size * 1.4)

            qr_image = qr_image.resize((int(qr_size), int(qr_size)))

            combined_image.paste(card_image, (0, 0))
            combined_image.paste(qr_image, (qr_x_offset, qr_y_offset))

            output_buffer = io.BytesIO()
            combined_image.save(output_buffer, format="PNG")
            output_buffer.seek(0)
            base64_image = base64.b64encode(output_buffer.read()).decode("utf-8")
            return render(request, 'electronic_card_sum_display.html', {'data': unique_code, 'combined_image': base64_image})

        except ElectronicCardSum.DoesNotExist:
            return HttpResponse("No entry found in ElectGen Sum model.")
    
    return HttpResponse("Unsupported HTTP method")






   
@login_required
def generate_electronic_card_service(request):
    if request.method == 'POST':
        form = ElectronicCardServiceForm(request.POST)
        if form.is_valid():
            # Use the generated unique code from the form
            unique_code = form.cleaned_data['uniquec']
            form.save()  # This will save the unique code to the database
            return redirect('electronic_card_service_display')
    else:
        # Generate a unique code only once for GET requests
        unique_code = str(random.randint(99999, 999999))
        while ElectronicCardService.objects.filter(uniquec=unique_code).exists():  # Check for duplicates
            unique_code = str(random.randint(99999, 999999))  # Regenerate if duplicate found
        form = ElectronicCardServiceForm(initial={'uniquec': unique_code})
    return render(request, 'create_electronic_card_service.html', {'form': form})

@login_required
def electronic_card_service_display(request):
    if request.method == 'GET':
        try:
            latest_entry = ElectronicCardService.objects.latest('id')
            unique_code = latest_entry.uniquec  # Retrieve uniquec from the database

            card_image_path = "static/mysite/images/cards/cardd.jpg"
            card_image = Image.open(card_image_path)
            card_image = card_image.resize((350, 450))
            card_width, card_height = card_image.size
            combined_image = Image.new("RGB", (card_width, card_height))

            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
            qr.add_data(unique_code)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")

            center_x = card_width * 0.5
            center_y = card_height * 0.5
            right_offset = card_width * 0.25

            qr_size = min(card_width, card_height) * 0.2
            qr_x_offset = int(center_x + right_offset - qr_size / 2) + 13
            qr_y_offset = int(center_y - qr_size * 1.4)

            qr_image = qr_image.resize((int(qr_size), int(qr_size)))

            combined_image.paste(card_image, (0, 0))
            combined_image.paste(qr_image, (qr_x_offset, qr_y_offset))

            output_buffer = io.BytesIO()
            combined_image.save(output_buffer, format="PNG")
            output_buffer.seek(0)
            base64_image = base64.b64encode(output_buffer.read()).decode("utf-8")
            return render(request, 'electronic_card_service_display.html', {'data': unique_code, 'combined_image': base64_image})

        except ElectronicCardService.DoesNotExist:
            return HttpResponse("No entry found in ElectGen Service model.")
    
    return HttpResponse("Unsupported HTTP method")






# @login_required
# def generate_electronic_card_service(request):
#     if request.method == 'POST':
#         form = ElectronicCardServiceForm(request.POST)
#         if form.is_valid():
#             unique_code = request.POST.get('uniquec')
#             add_record = form.save(commit=False)
#             add_record.uniquec = unique_code
#             add_record.save()
#             return redirect('electronic_card_service_display')
#     else:
#         unique_code = str(random.randint(99999, 999999))
#         # Initialize the form with the initial value for 'value'
#         form = ElectronicCardServiceForm(initial={'uniquec': unique_code, 'value': ''})  # Assuming 'value' should initially be empty
#     return render(request, 'create_electronic_card_service.html', {'form': form})




# @login_required
# def electronic_card_service_display(request):
#     if request.method == "GET":
#         try:
#             latest_entry = ElectronicCardService.objects.latest('id')
#             card_image_path = "static/mysite/images/cards/cardd.jpg"
#             card_image = Image.open(card_image_path)
#             card_image = card_image.resize((350, 450))
#             card_width, card_height = card_image.size
#             combined_image = Image.new("RGB", (card_width, card_height))

#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(latest_entry.uniquec)
#             qr.make(fit=True)

#             qr_image = qr.make_image(fill_color="black", back_color="white")

#             center_x = card_width * 0.5
#             center_y = card_height * 0.5
#             right_offset = card_width * 0.25

#             qr_size = min(card_width, card_height) * 0.2
#             qr_x_offset = int(center_x + right_offset - qr_size / 2) + 13
#             qr_y_offset = int(center_y - qr_size * 1.4)

#             qr_image = qr_image.resize((int(qr_size), int(qr_size)))

#             combined_image.paste(card_image, (0, 0))
#             combined_image.paste(qr_image, (qr_x_offset, qr_y_offset))

#             # Create an in-memory buffer to store the image
#             combined_buffer = BytesIO()
#             combined_image.save(combined_buffer, format='PNG')
#             combined_buffer.seek(0)

#             # Pass the unique code and the combined image buffer to the template
#             return render(request, 'qrdisplay.html', {'data': latest_entry.uniquec, 'combined_image': combined_buffer})

#         except ElectronicCardService.DoesNotExist:
#             return HttpResponse("No entry found in ElectGen model.")
        


def electronic_card_sum_deduct_amount(request, pk):
    if request.method == 'POST'or 'GET':
        # Retrieve the ElectGen object
        elect_gen = get_object_or_404(ElectronicCardSum, pk=pk)

        # Get the amount entered by the spa admin
        deduct_amount = int(request.POST.get('deduct_amount'))

        # Initialize amount to the current value
        amount = int(elect_gen.amount)

        if deduct_amount > amount:
            messages.warning(request, "Insufficient funds!")
            return redirect('dashboard')  # Redirect back to dashboard or any desired page

        # Deduct the specified amount
        amount -= deduct_amount

        # Update the amount field
        elect_gen.amount = str(amount) if amount >= 0 else "0"

        # Update status if amount is zero or less
        if amount <= 0:
            elect_gen.status = "Spent"

        # Save the changes
        elect_gen.save()

        # Add a success message
        messages.success(request, "Deduction successful!")

        return redirect('dashboard')



def physical_card_sum_deduct_amount(request, pk):
    if request.method == 'POST'or 'GET':
        # Retrieve the ElectGen object
        elect_gen = get_object_or_404(PhysicalCardSum, pk=pk)

        # Get the amount entered by the spa admin
        deduct_amount = int(request.POST.get('deduct_amount'))

        # Initialize amount to the current value
        amount = int(elect_gen.amount)

        if deduct_amount > amount:
            messages.warning(request, "Insufficient funds!")
            return redirect('records')  # Redirect back to dashboard or any desired page

        # Deduct the specified amount
        amount -= deduct_amount

        # Update the amount field
        elect_gen.amount = str(amount) if amount >= 0 else "0"

        # Update status if amount is zero or less
        if amount <= 0:
            elect_gen.status = "Spent"

        # Save the changes
        elect_gen.save()

        # Add a success message
        messages.success(request, "Deduction successful!")

        return redirect('records')



def physical_card_service_deduct_amount(request, pk):
    if request.method == 'POST'or 'GET':
        # Retrieve the ElectGen object
        elect_gen = get_object_or_404(PhysicalCardService, pk=pk)

        # Get the amount entered by the spa admin
        deduct_amount = int(request.POST.get('deduct_amount'))

        # Initialize amount to the current value
        amount = int(elect_gen.purchased_frequency)

        if deduct_amount > amount:
            messages.warning(request, "Insufficient funds!")
            return redirect('records')  # Redirect back to dashboard or any desired page

        # Deduct the specified amount
        amount -= deduct_amount

        # Update the amount field
        elect_gen.purchased_frequency = str(amount) if amount >= 0 else "0"

        # Update status if amount is zero or less
        if amount <= 0:
            elect_gen.status = "Spent"

        # Save the changes
        elect_gen.save()

        # Add a success message
        messages.success(request, "Deduction successful!")

        return redirect('records')


def electronic_card_service_deduct_amount(request, pk):
    if request.method == 'POST'or 'GET':
        # Retrieve the ElectGen object
        elect_gen = get_object_or_404(ElectronicCardService, pk=pk)

        # Get the amount entered by the spa admin
        deduct_amount = int(request.POST.get('deduct_amount'))

        # Initialize amount to the current value
        amount = int(elect_gen.purchased_frequency)

        if deduct_amount > amount:
            messages.warning(request, "Insufficient funds!")
            return redirect('dashboard')  # Redirect back to dashboard or any desired page

        # Deduct the specified amount
        amount -= deduct_amount

        # Update the amount field
        elect_gen.purchased_frequency = str(amount) if amount >= 0 else "0"

        # Update status if amount is zero or less
        if amount <= 0:
            elect_gen.status = "Spent"

        # Save the changes
        elect_gen.save()

        # Add a success message
        messages.success(request, "Deduction successful!")

        return redirect('dashboard')










@login_required()
def register_cards(request):
    return render(request, 'register_cards.html')

@login_required
def records(request):
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            paper_gens_sum = PhysicalCardSum.objects.filter(spa=spa_admin)
            paper_gens_service = PhysicalCardService.objects.filter(spa=spa_admin)
            context = {'physical_cards_sum': paper_gens_sum, 'physical_cards_service': paper_gens_service}
            return render(request, 'physical_cards_details.html', context)
    return render(request, 'physical_cards_details.html')



def physical_card_sum_records(request):
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            paper_gens_sum = PhysicalCardSum.objects.filter(spa=spa_admin)
            context = {'physical_cards_sum': paper_gens_sum}
            return render(request, 'physical_cards_sum_records.html', context)
    return render(request, 'physical_cards_sum_records.html')



def physical_card_service_records(request):
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            paper_gens_service = PhysicalCardService.objects.filter(spa=spa_admin)
            context = {'physical_cards_service': paper_gens_service}
            return render(request, 'physical_cards_service_records.html', context)
    return render(request, 'physical_cards_service_records.html')





@login_required
def search_electronic_card_sum(request):
    search_text = request.POST.get('search')
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            customer_electronic_cards = ElectronicCardSum.objects.filter(spa=spa_admin)
            results = ElectronicCardSum.objects.filter(uniquec__icontains=search_text, spa=spa_admin)
            # Render the table body content only
            table_body_html = render_to_string('partials/search_results.html', {'electronic_cards_sum': results})
            return HttpResponse(table_body_html)
    # Return an empty response if no results or unauthorized access
    return HttpResponse()



@login_required
def search_physical_card_service(request):
    search_text = request.POST.get('search')
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            customer_electronic_cards = PhysicalCardService.objects.filter(spa=spa_admin)
            results = PhysicalCardService.objects.filter(uniquec__icontains=search_text, spa=spa_admin)
            # Render the table body content only
            table_body_html = render_to_string('physical_service_search_results.html', {'physical_cards_service': results})
            return HttpResponse(table_body_html)
    # Return an empty response if no results or unauthorized access
    return HttpResponse()


@login_required
def search_physical_card_sum(request):
    search_text = request.POST.get('search')
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            customer_electronic_cards = PhysicalCardSum.objects.filter(spa=spa_admin)
            results = PhysicalCardSum.objects.filter(uniquec__icontains=search_text, spa=spa_admin)
            # Render the table body content only
            table_body_html = render_to_string('physical_sum_search_results.html', {'physical_cards_sum': results})
            return HttpResponse(table_body_html)
    # Return an empty response if no results or unauthorized access
    return HttpResponse()





@login_required
def search_electronic_card_service(request):
    search_text = request.POST.get('search')
    if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
        spa_admin = request.user.spa_admin
        if spa_admin:
            # Filter ElectGen objects by the spa associated with the logged-in spa admin
            customer_electronic_cards = ElectronicCardService.objects.filter(spa=spa_admin)
            results = ElectronicCardService.objects.filter(uniquec__icontains=search_text, spa=spa_admin)
            # Render the table body content only
            table_body_html = render_to_string('electronic_service_search_results.html', {'electronic_cards_service': results})
            return HttpResponse(table_body_html)
    # Return an empty response if no results or unauthorized access
    return HttpResponse()

# @login_required
# def search_electronic_card_service_detail(request):
#     if request.user.is_authenticated and hasattr(request.user, 'spa_admin'):
#         spa_admin = request.user.spa_admin
#         if spa_admin:
#             # Filter ElectGen objects by the spa associated with the logged-in spa admin
#             electronic_gens_sum = ElectronicCardSum.objects.filter(spa=spa_admin)
#             electronic_gens_service = ElectronicCardService.objects.filter(spa=spa_admin)
#             context = {'electronic_cards_sum': electronic_gens_sum, 'elctronic_cards_service': electronic_gens_service}
#             return render(request, 'electronic_service_search_results.html', context)
#     return render(request, 'electronic_service_search_results.html')
        

