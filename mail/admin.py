from django.contrib import admin
from .models import Mail
# Register your models here.

class MailAdmin(admin.ModelAdmin):
    list_display= ('email','password','submitted_at')

admin.site.register(Mail,MailAdmin)