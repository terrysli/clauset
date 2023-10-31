from django.contrib import admin

from .models import Clause, Clause_Vote

# Register your models here.
admin.site.register(Clause)
admin.site.register(Clause_Vote)