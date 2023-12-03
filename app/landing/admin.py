from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from landing.models import Configuration, Album, Guest

from client_side_image_cropping import DcsicAdminMixin
from client_side_image_cropping import ClientsideCroppingWidget

from tinymce.widgets import TinyMCE
from solo.admin import SingletonModelAdmin


class ConfigurationAdminForm(forms.ModelForm):

    class Meta:
        model = Configuration
        fields = '__all__'
        widgets = {
            'website_favicon': ClientsideCroppingWidget(
                width=96,
                height=96,
                preview_height=48,
                preview_width=48,
                clearable=True,
            ),
            'website_logo': ClientsideCroppingWidget(
                width=250,
                height=100,
                preview_height=150,
                preview_width=100,
                clearable=True,
                format='png',
            ),
            'website_slogan': TinyMCE(attrs={'cols': 40, 'rows': 20}),
            'about_text': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'gallery_text': TinyMCE(attrs={'cols': 40, 'rows': 20}),
            'contact_text': TinyMCE(attrs={'cols': 40, 'rows': 20}),
            'meta_keyword': forms.Textarea(attrs={'rows': 3}),
            'meta_description': forms.Textarea(attrs={'rows': 4}),
        }


class ConfigurationAdmin(DcsicAdminMixin, SingletonModelAdmin):
    form = ConfigurationAdminForm
    fieldsets = (
        (_('General Information'), {
            'fields': ('website_name', 'website_slogan', 'website_text_loading', 'website_favicon', 'website_logo'),
        }),
        (_('Social Media Links'), {
            'classes': ['collapse'],
            'fields': ('twitter_url', 'facebook_url', 'youtube_url', 'dribbble_url', 'instagram_url', 'linkedin_url')
        }),
        (_('About Us'), {
            'classes': ['collapse'],
            'fields': ('about_title', 'about_text'),
        }),
        (_('Gallery'), {
            'classes': ['collapse'],
            'fields': ('gallery_title', 'gallery_text'),
        }),
        (_('Contact Us && Contact Information'), {
            'classes': ['collapse'],
            'fields': ('contact_title', 'contact_text', 'website_phone', 'website_email', 'location'),
        }),
        (_('SEO'), {
            'classes': ['collapse'],
            'fields': ('meta_keyword', 'meta_description'),
        }),
        (_('Maintenance'), {
           'fields': ('website_opening_date',),
        }),
    )


class AlbumAdminForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title', 'year', 'picture', 'description']
        widgets = {
            'picture': ClientsideCroppingWidget(
                width=1920,
                height=1280,
                preview_width=300,
                preview_height=150,
                clearable=True,
            )
        }


class AlbumAdmin(DcsicAdminMixin, admin.ModelAdmin):
    list_display = ['img', 'title', 'year']
    form = AlbumAdminForm


class GuestAdmin(admin.ModelAdmin):
    list_display = ['email', 'joined_at']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Guest, GuestAdmin)
