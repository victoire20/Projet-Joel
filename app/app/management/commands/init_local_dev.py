from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from landing.models import Configuration

UserModel = get_user_model()


CONFIGURATION = [
    {
        'website_name': 'Fashion Pro',
        'website_slogan': 'So Excited !!! Product Launch by Codedthemes. Top bar Time countdown - Chill your excitement.',
        'website_text_loading': 'So Excited ?',
        'website_phone': '(+33) 66-1254-611',
        'website_email': 'wave@example.com',
        'location': '66 Grand Central, NY 66564, USA',
        'about_title': 'Our great Story',
        'about_text': "Hi, I'm WAVE and I'm ready to boost your web project by my elegance, exclusive design and "
                      "animations. I'm ready-to-use, just upload me on your server, add your pictures and edit my "
                      "texts. Handmade, precisely built with the famous Bootstrap Framework. Salut, je suis WAVE et "
                      "je suis prêt à booster votre projet web par mon élégance, mon design et mes animations "
                      "exclusives. Je suis prêt à l'emploi, il suffit de me mettre sur votre serveur.",
        'gallery_title': 'Our latest works',
        'gallery_text': 'Showcase your work brillantly with this stunning gallery. Easy-to-use, you can add projects '
                        'as much as you want. Fully responsive, your portfolio page is ideal to give the best feeling '
                        'to your visitors and to catch their attention.',
        'contact_title': 'Get in touch',
        'contact_text': 'We are here to help you Tuesday through Saturday, from 9:00 AM to 10:00 PM. Fill the next '
                        'online form to get in touch with our friendly support team!',
    }
]

ADMIN_ID = 'admin-oc'
ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Configuration.objects.all().delete()
        UserModel.objects.all().delete()

        for data_configuration in CONFIGURATION:
            Configuration.objects.create(
                website_name=data_configuration['website_name'],
                website_slogan=data_configuration['website_slogan'],
                website_text_loading=data_configuration['website_text_loading'],
                website_phone=data_configuration['website_phone'],
                website_email=data_configuration['website_email'],
                location=data_configuration['location'],
                about_title=data_configuration['about_title'],
                about_text=data_configuration['about_text'],
                gallery_title=data_configuration['gallery_title'],
                gallery_text=data_configuration['gallery_text'],
                contact_title=data_configuration['contact_title'],
                contact_text=data_configuration['contact_text'],
            )

        UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))