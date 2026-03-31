from .settings import *

DEBUG=True
#Crie a secret key para seu ambiente de teste
SECRET_KEY = 'Iw_jBMkoHt*h3on|^Q3_AU;O&DWc|6ue'
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ALLOWED_HOSTS = ['127.0.0.1']