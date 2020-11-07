from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Key)
admin.site.register(models.Session)

