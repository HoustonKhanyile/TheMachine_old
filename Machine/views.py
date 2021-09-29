from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AppsForm, Perform, Public_R
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'Profile.html')

def Appearence(request):
    form = AppsForm()
    if request.method == 'POST':
        form = AppsForm(request.POST)
        if form.is_valid():
            form.save()
            Show = form.cleaned_data.get('Show')
            Media = form.cleaned_data.get('Media')
            Episode = form.cleaned_data.get('Episode')
            Date = form.cleaned_data.get('Date')
            Time = form.cleaned_data.get('Time')
            Producer = form.cleaned_data.get('Producer')
            to_email = form.cleaned_data.get('Producer_Email')
            template = render_to_string('Apps_email_template.html', {'Show': Show, 'Media': Media, 'Episode': Episode, 'Date': Date, 'Time': Time, 'Producer': Producer})
            email = EmailMessage(
                "Confirmation of Appearence Booking",
                template,
                settings,
                [to_email], 
                )
            fail_silently=False
            email.send()
            return HttpResponse('Thank you for filling in your Appearence Form')

    return render(request, 'AppsForm.html', {'form': form})


def Performs(request):
    form = Perform()
    if request.method == 'POST':
        form = Perform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    return render(request, 'Performance.html', {'form': form})

def Publicity(request):
    form = Public_R()
    if request.method == 'POST':
        form = Public_R(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    return render(request, 'PR-Form.html', {'form': form})

def results(request):
    form = AppsForm()
    return render(request, 'Results.html', {'form': form})