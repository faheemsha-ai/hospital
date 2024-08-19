from django.contrib import admin
from . models import Department, Doctor,Booking

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking)