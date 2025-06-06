from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from django.conf import settings

def home(request):
    return render(request,'home.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')   
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # Save to DB
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )


        # Compose full message
        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  # change to your recipient email
            fail_silently=False
        )

        return render(request, 'home.html', {'success': 'Message sent successfully!'})
    else:
        return render(request, 'home.html', {'error': 'All fields are required.'})

    return render(request, 'home.html')
