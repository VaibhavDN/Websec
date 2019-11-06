from django.contrib import admin
from .models import UserDetails, AdminDetails, ModelsActiveStatus

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(AdminDetails)
admin.site.register(ModelsActiveStatus)
