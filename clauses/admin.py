from django.contrib import admin

from .models import Clause, Rating

# Register your models here.
admin.site.register(Clause)
admin.site.register(Rating)