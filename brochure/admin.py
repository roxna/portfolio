from django.contrib import admin
from brochure.models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'website', 'date_created', 'level')


admin.site.register(Project, ProjectAdmin)
# admin.site.register(Image)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Tag)