from django.contrib import admin

from .models import User,Message,Formula,Topic

# Register your models here.

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Formula)
admin.site.register(Topic)