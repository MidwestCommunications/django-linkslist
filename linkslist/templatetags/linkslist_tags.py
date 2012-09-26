from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from linkslist.models import LinksList

register = template.Library()
current_site = Site.objects.get_current()

@register.inclusion_tag('linkslist/slider.html')
def slider(key):
    try:
        slider = LinksList.objects.get(site=current_site, key=key)
    except:
        slider = ''
    
    return {'slider': slider}

@register.simple_tag
def slider_js():
    js = """
    <script type='text/javascript' src='%sjs/easyslider1.7/easySlider1.7.js'></script>
    <script type='text/javascript'>
        $(document).ready(function(){   
            $('#slider').easySlider({
                auto: true, 
                continuous: true
            });
        }); 
    </script>
    """ % (settings.STATIC_URL,)
    
    return js
    
@register.inclusion_tag('linkslist/simplelist.html')
def simplelist(key):
    try:
        simplelist = LinksList.objects.get(site=current_site, key=key)
    except:
        simplelist = ''
        
    return {'simplelist': simplelist}