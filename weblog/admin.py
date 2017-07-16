from django.contrib import admin
from weblog.models import Weblog
# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Weblog,blogAdmin)