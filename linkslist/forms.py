from django import forms
from django.conf import settings
from django.core.cache import cache


from linkslist.models import LinksListItem
from photologue.models import Photo
from tagging.models import TaggedItem


linkslist_photos = cache.get('linkslist_photos')
if not linkslist_photos:
    linklist_photos = TaggedItem.objects.get_by_model(Photo, 'linkslist')
    cache.set('linkslist_photos', linkslist_photos, 5)


class LinksListItemAdminForm(forms.ModelForm):
    photo = forms.ModelChoiceField(queryset=linklist_photos, required=False)
    
    class Meta:
        model = LinksListItem

    class Media:
        js = (settings.ADMIN_MEDIA_PREFIX + "js/SelectBox.js",
                 settings.ADMIN_MEDIA_PREFIX + "js/SelectFilter2.js",
                 "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js",
                 settings.STATIC_URL + "js/ajax_filtered_fields.js",)
