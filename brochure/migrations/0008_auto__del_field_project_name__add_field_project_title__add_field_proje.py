# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.name'
        db.delete_column(u'brochure_project', 'name')

        # Adding field 'Project.title'
        db.add_column(u'brochure_project', 'title',
                      self.gf('django.db.models.fields.CharField')(default='x', max_length=20),
                      keep_default=False)

        # Adding field 'Project.tag_line'
        db.add_column(u'brochure_project', 'tag_line',
                      self.gf('django.db.models.fields.CharField')(default='x', max_length=50),
                      keep_default=False)

        # Deleting field 'Blog.date_written'
        db.delete_column(u'brochure_blog', 'date_written')

        # Adding field 'Blog.date_created'
        db.add_column(u'brochure_blog', 'date_created',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.name'
        db.add_column(u'brochure_project', 'name',
                      self.gf('django.db.models.fields.CharField')(default='x', max_length=20),
                      keep_default=False)

        # Deleting field 'Project.title'
        db.delete_column(u'brochure_project', 'title')

        # Deleting field 'Project.tag_line'
        db.delete_column(u'brochure_project', 'tag_line')

        # Adding field 'Blog.date_written'
        db.add_column(u'brochure_blog', 'date_written',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Deleting field 'Blog.date_created'
        db.delete_column(u'brochure_blog', 'date_created')


    models = {
        u'brochure.blog': {
            'Meta': {'object_name': 'Blog'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_line': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'brochure.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'brochure.image': {
            'Meta': {'object_name': 'Image'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'null': 'True', 'to': u"orm['brochure.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'null': 'True', 'to': u"orm['brochure.Project']"})
        },
        u'brochure.project': {
            'Meta': {'object_name': 'Project'},
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'Basic'", 'max_length': '10'}),
            'tag_line': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'brochure.tag': {
            'Meta': {'object_name': 'Tag'},
            'blog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['brochure.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['brochure']