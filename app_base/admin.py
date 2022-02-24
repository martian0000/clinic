from django.contrib import admin
from app_base.models import Reservation,Speciality,Doctor,Service

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Service)