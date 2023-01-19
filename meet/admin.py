from django.contrib import admin
from .models import Profile,Request_To_Chat,Room,Message,Block


# Register your models here.
# class ProfileTable(MultiTableMixin, TemplateView):
#     model = Profile
#     template_name = "modprofile.html"
#     table_class = ProfileTable

class ProfieAdmin(admin.ModelAdmin):
    list_display= ('name', 'likes')


admin.site.register(Block)
admin.site.register(Profile,ProfieAdmin)
admin.site.register(Request_To_Chat)
admin.site.register(Room)
admin.site.register(Message)
