from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from photologue.models import Photo

class LinksList(models.Model):
    key = models.CharField(max_length=20)
    title = models.CharField(max_length=75)
    site = models.ForeignKey(Site)
    
    objects = models.Manager()
    on_site = CurrentSiteManager('site',) 
    
    class Meta:
        unique_together = (('title', 'site',), ('key', 'site',),)
        ordering = ('title',)
    
    def __unicode__(self):
        return '%s links list on %s' % (self.title, self.site.name)
        
class LinksListItem(models.Model):
    links_list = models.ForeignKey(LinksList)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    link = models.URLField(verify_exists=False)
    description = models.CharField(max_length=160, blank=True)
    order = models.PositiveSmallIntegerField()
    
    class Meta:
        unique_together = (('links_list', 'order',),)
        ordering = ['order']
    
    def __unicode__(self):
        return 'Links list item #%s for %s' % (self.order, self.links_list,)