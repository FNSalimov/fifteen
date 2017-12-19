from django.contrib import admin
from django.contrib.auth.models import User
from .models import Word, Sphere, User_Word

#admin.site.register(User)
admin.site.register(Word)
admin.site.register(Sphere)
admin.site.register(User_Word)