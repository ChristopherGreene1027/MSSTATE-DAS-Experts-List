import django_on_heroku
from decouple import config

from .settings import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'expertslist.herokuapp.com'
    
]