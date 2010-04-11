from django import template
from django.conf import settings
from linkslist.models import LinksList

register = template.Library()

@register.inclusion_tag('linkslist/slider.html')
def slider(key):
    try:
        slider = LinksList.on_site.get(key=key)
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
        simplelist = LinksList.on_site.get(key=key)
    except:
        simplelist = ''
        
    return {'simplelist': simplelist}