
from south.db import db
from django.db import models
from linkslist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'LinksListItem'
        db.create_table('linkslist_linkslistitem', (
            ('id', orm['linkslist.LinksListItem:id']),
            ('links_list', orm['linkslist.LinksListItem:links_list']),
            ('photo', orm['linkslist.LinksListItem:photo']),
            ('link', orm['linkslist.LinksListItem:link']),
            ('description', orm['linkslist.LinksListItem:description']),
            ('order', orm['linkslist.LinksListItem:order']),
        ))
        db.send_create_signal('linkslist', ['LinksListItem'])
        
        # Adding model 'LinksList'
        db.create_table('linkslist_linkslist', (
            ('id', orm['linkslist.LinksList:id']),
            ('key', orm['linkslist.LinksList:key']),
            ('title', orm['linkslist.LinksList:title']),
            ('site', orm['linkslist.LinksList:site']),
        ))
        db.send_create_signal('linkslist', ['LinksList'])
        
        # Creating unique_together for [title, site] on LinksList.
        db.create_unique('linkslist_linkslist', ['title', 'site_id'])
        
        # Creating unique_together for [key, site] on LinksList.
        db.create_unique('linkslist_linkslist', ['key', 'site_id'])
        
        # Creating unique_together for [links_list, order] on LinksListItem.
        db.create_unique('linkslist_linkslistitem', ['links_list_id', 'order'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [links_list, order] on LinksListItem.
        db.delete_unique('linkslist_linkslistitem', ['links_list_id', 'order'])
        
        # Deleting unique_together for [key, site] on LinksList.
        db.delete_unique('linkslist_linkslist', ['key', 'site_id'])
        
        # Deleting unique_together for [title, site] on LinksList.
        db.delete_unique('linkslist_linkslist', ['title', 'site_id'])
        
        # Deleting model 'LinksListItem'
        db.delete_table('linkslist_linkslistitem')
        
        # Deleting model 'LinksList'
        db.delete_table('linkslist_linkslist')
        
    
    
    models = {
        'linkslist.linkslist': {
            'Meta': {'unique_together': "(('title', 'site'), ('key', 'site'))"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'linkslist.linkslistitem': {
            'Meta': {'unique_together': "(('links_list', 'order'),)"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'links_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['linkslist.LinksList']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'})
        },
        'photologue.photo': {
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.59999999999999998'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['linkslist']
