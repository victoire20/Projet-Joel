from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

CSRF_COOKIE_SECURE = True  # Use csrf only in HTTPS connexion

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '********************' #'smtp.gmail.com'
EMAIL_FROM = '********************' #'gauisyaba@gmail.com'
EMAIL_HOST_USER = '********************' #'gauisyaba@gmail.com'
EMAIL_HOST_PASSWORD = '********************' #'dqzehywxddelzgje'
EMAIL_PORT = 587    # Juste pour Google
EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
