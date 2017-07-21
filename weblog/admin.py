from django.contrib import admin
from weblog.models import Weblog
from weblog.models import User
# Register your models here.
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#

admin.site.register(User)

admin.site.register(Weblog)