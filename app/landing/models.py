from django.db import models
from tinymce.models import HTMLField
from solo.models import SingletonModel

from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils import timezone
import os
from django.http import JsonResponse

from django.template.loader import render_to_string
from django.core import mail


class Configuration(SingletonModel):
    def custom_photo_path(instance, filename):
        if filename:
            ext = os.path.splitext(filename)[1]
            timestamp = str(int(timezone.now().timestamp()))
            new_filename = f"{timestamp}{ext}"
            return os.path.join('configuration/', new_filename)
        return None
    website_name = models.CharField(null=True, blank=True, max_length=100, verbose_name=_('Website Name'))
    website_slogan = HTMLField(null=True, blank=True, max_length=200, verbose_name=_('Website Slogan'))
    website_favicon = models.FileField(null=True, blank=True, upload_to=custom_photo_path, verbose_name=_('Favicon'))
    website_logo = models.FileField(null=True, blank=True, upload_to=custom_photo_path, verbose_name=_('Logo'))
    website_text_loading = models.CharField(null=True, blank=True, max_length=100, default='So Excited ?', verbose_name=_('Website Text Load'))
    twitter_url = models.URLField(null=True, blank=True, verbose_name=_('Twitter Link'))
    facebook_url = models.URLField(null=True, blank=True, verbose_name=_('Facebook Link'))
    youtube_url = models.URLField(null=True, blank=True, verbose_name=_('Youtube Link'))
    dribbble_url = models.URLField(null=True, blank=True, verbose_name=_('Dribbble Link'))
    instagram_url = models.URLField(null=True, blank=True, verbose_name=_('Instagram Link'))
    linkedin_url = models.URLField(null=True, blank=True, verbose_name=_('Linkedin Link'))
    website_phone = models.CharField(null=True, blank=True, max_length=20, verbose_name=_('Phone'))
    website_email = models.EmailField(null=True, blank=True, verbose_name=_('Email'))
    location = models.CharField(null=True, blank=True, max_length=200, verbose_name=_('Location'))
    website_opening_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Opening Date'))
    about_title = models.CharField(null=True, blank=True, max_length=100, verbose_name=_('About Title'))
    about_text = HTMLField(null=True, blank=True, max_length=700, verbose_name=_('About Text'))
    gallery_title = models.CharField(null=True, blank=True, max_length=100, verbose_name=_('Gallery Title'))
    gallery_text = HTMLField(null=True, blank=True, max_length=700, verbose_name=_('Gallery Text'))
    contact_title = models.CharField(null=True, blank=True, max_length=100, verbose_name=_('Contact Title'))
    contact_text = HTMLField(null=True, blank=True, max_length=700, verbose_name=_('Contact Text'))
    meta_keyword = models.TextField(null=True, blank=True, verbose_name=_('Meta Keyword'))
    meta_description = models.TextField(null=True, blank=True, verbose_name=_('Meta Description'))

    def __str__(self):
        return 'Site Configuration'

    class Meta:
        verbose_name = _('Site Configuration')

    def favicon(self):
        return mark_safe("<img src='/media/%s' width='100' height='100' />" % self.website_favicon)

    def logo(self):
        return mark_safe("<img src='/media/%s' width='100' height='100' />" % self.website_logo)


class Album(models.Model):
    def custom_photo_path(instance, filename):
        if filename:
            ext = os.path.splitext(filename)[1]
            timestamp = str(int(timezone.now().timestamp()))
            new_filename = f"{timestamp}{ext}"
            return os.path.join('album/', new_filename)
        return None
    title = models.CharField(max_length=100, verbose_name=_('Album Title'))
    year = models.DateField(null=True, blank=True)
    picture = models.FileField(upload_to=custom_photo_path, verbose_name=_('Picture'))
    description = models.TextField(null=True, blank=True, verbose_name=_('picture description'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')

    def img(self):
        return mark_safe("<img src='/media/%s' width='100' height='100' />" % self.picture)


class Guest(models.Model):
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = _('Guest')
        verbose_name_plural = _('Guests')


class Message(models.Model):
    guests = models.ManyToManyField(Guest)
    subject = models.CharField(null=True, blank=True, max_length=200, verbose_name=_('Email Subject'))
    content = models.TextField(verbose_name=_('Email Content'))

    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
