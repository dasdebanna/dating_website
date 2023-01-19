import django_tables2 as tables
from .models import Profile
from users.models import Report

class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "likes",)

class ReportTable(tables.Table):
    class Meta:
        model = Report
        template_name = "django_tables2/bootstrap.html"
        fields = ("reported_by","reason","reported")