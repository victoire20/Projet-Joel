from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.core import mail
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .models import Configuration, Album, Guest
from .forms import ContactForm, GuestForm


def indexPage(request):
    config = Configuration.get_solo()
    album = Album.objects.all()
    return render(request, 'index.html', {'configuration': config, 'album': album})


def sendEmail(request):
    form = ContactForm(request.POST)

    if request.method != 'POST':
        return JsonResponse({'details': 'Method Not Allowed'}, status=405)

    if form.is_valid():
        guest = Guest.objects.filter(email=form.cleaned_data['email'])
        if guest is None:
            Guest.objects.create(email=form.cleaned_data['email'])

        mail_subject = form.cleaned_data['subject']
        to_email = form.cleaned_data['email']
        message = render_to_string('email.html', {
            'user': form.cleaned_data['name'],
            'message': form.cleaned_data['message'],
            'protocol': 'https' if request.is_secure() else 'http'
        })

        try:
            send_mail = mail.EmailMessage(mail_subject, message, to=[to_email])
            send_mail.send()
        except mail.BadHeaderError:
            return JsonResponse({'details': 'Email Not Send !'}, status=400)
        return JsonResponse({'message': 'The email successfully sent !'}, status=200)


@transaction.atomic
def guestAdded(request):
    form = GuestForm(request.POST)

    if request.method != 'POST':
        return JsonResponse({'details': 'Method Not Allowed'}, status=405)

    if form.is_valid():
        guest = Guest.objects.filter(email=form.cleaned_data['email'])
        if guest:
            return JsonResponse({'details': 'You\'re already on the guest list!'}, status=400)
        Guest.objects.create(email=form.cleaned_data['email'])
        message = {'message': _('Congrats! You are in list.<br>We will inform you as soon as we finish.')}
        return JsonResponse(message, status=200)
    return JsonResponse({'details': 'form.errors'}, status=400)
