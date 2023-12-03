from django import forms

from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label=_('Your Name*'), label_suffix='')
    email = forms.EmailField(max_length=200, label=_('Your Email*'), label_suffix='')
    subject = forms.CharField(max_length=100, label=_('Regarding...'), label_suffix='', required=False)
    message = forms.CharField(max_length=500, label=_('Your message here... 20 characters Min.*'), label_suffix='')


class GuestForm(forms.Form):
    email = forms.EmailField(max_length=200, label=_('Click here to write your email'), label_suffix='')
