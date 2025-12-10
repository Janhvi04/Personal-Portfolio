from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Save to database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        contact.save()
        
        # Success message
        messages.success(request, 'Thank you! Your message has been sent successfully. I will get back to you soon!')
        return redirect('home')
    
    # If GET request, just render the page
    return render(request, 'home.html')