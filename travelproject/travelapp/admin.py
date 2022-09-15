from django.contrib import admin

# Register your models here.
from .models import travel_des,travel_mate

admin.site.register(travel_des)
admin.site.register(travel_mate)