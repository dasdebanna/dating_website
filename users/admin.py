from django.contrib import admin
from .models import Private_Profile
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('reported_by','reason','reported')

# Register your models here.
admin.site.register(Private_Profile)
admin.site.register(Report,ReportAdmin)