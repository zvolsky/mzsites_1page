from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4fw3q5g0aqn$ip-#@4l+nq=@z^g9#fiiwd$fh%km-3hiosi&ou'

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
