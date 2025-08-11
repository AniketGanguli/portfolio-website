# portfolio_app/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Project, ContactSubmission

def homepage(request):
    projects = Project.objects.all()
    form = ContactForm()
    success_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save to database
            ContactSubmission.objects.create(name=name, email=email, message=message)

            # Send email notification
            send_mail(
                f'Portfolio Contact from {name}',
                message,
                email,
                ['your_email@example.com'], # Replace with your email
                fail_silently=False,
            )
            
            success_message = "Thank you for your message! I will get back to you as soon as possible."
            form = ContactForm() # Reset the form

    context = {
        'projects': projects,
        'form': form,
        'success_message': success_message,
    }
    # This line tells Django to look inside the `portfolio_app` folder within your templates directory.
    return render(request, 'portfolio_app/index.html', context)
