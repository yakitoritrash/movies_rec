from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from .forms import *


# Register your models here.
class CustomAdminSite(admin.AdminSite):
    site_header = 'Administration'

admin_site = CustomAdminSite(name='myadmin')

class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

admin.site.unregister(Group)
admin.site.unregister(User)

admin_site.register(Group)
admin_site.register(User)

admin_site.register(Genre)
admin_site.register(Movie, MovieAdmin)
