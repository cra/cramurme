# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Article.is_draft'
        db.delete_column('content_article', 'is_draft')

        # Adding field 'Article.is_published'
        db.add_column('content_article', 'is_published', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Article.is_draft'
        db.add_column('content_article', 'is_draft', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Deleting field 'Article.is_published'
        db.delete_column('content_article', 'is_published')


    models = {
        'content.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'content.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['content.MediaEntry']},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mediaentry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.MediaEntry']", 'unique': 'True', 'primary_key': 'True'})
        },
        'content.mediaentry': {
            'Meta': {'object_name': 'MediaEntry'},
            'emotions': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '400'})
        }
    }

    complete_apps = ['content']
