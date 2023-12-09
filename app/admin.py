from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Capitals)
admin.site.register(Countries)