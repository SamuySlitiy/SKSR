import os
import django
from django.contrib import admin
from schedule.models import Subject, Teacher, Class, Student

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_management.settings")
django.setup()

from schedule.models import *

# I will add a bunch of examples to all the classes later because I dont have much time