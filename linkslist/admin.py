from django.contrib import admin
from linkslist.models import LinksList, LinksListItem
from linkslist.forms import LinksListItemAdminForm

class LinksListItemInline(admin.StackedInline):
    model = LinksListItem
    form = LinksListItemAdminForm
    fieldsets = (
        (None, {
            'fields': ('link', 'description', 'order', 'photo',)
        }),
    )
    extra = 5
    max_num = 10
    
class LinksListAdmin(admin.ModelAdmin):
    inlines = [
        LinksListItemInline,
    ]
    
admin.site.register(LinksList, LinksListAdmin)
