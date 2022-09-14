from django.contrib import admin
from .models import JobApplication, JobAdvert

# Register your models here.
admin.site.register([JobApplication, JobAdvert])