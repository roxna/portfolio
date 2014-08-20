# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'brochure_image')

        # Adding field 'Project.image'
        db.add_column(u'brochure_project', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Project.level'
        db.alter_column(u'brochure_project', 'level', self.gf('django.db.models.fields.CharField')(max_length=12))
        # Adding field 'Blog.image'
        db.add_column(u'brochure_blog', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'brochure_image', (
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image', null=True, to=orm['brochure.Blog'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image', null=True, to=orm['brochure.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'brochure', ['Image'])

        # Deleting field 'Project.image'
        db.delete_column(u'brochure_project', 'image')


        # Changing field 'Project.level'
        db.alter_column(u'brochure_project', 'level', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Deleting field 'Blog.image'
        db.delete_column(u'brochure_blog', 'image')


    models = {
        u'brochure.blog': {
            'Meta': {'object_name': 'Blog'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'brochure.project': {
            'Meta': {'object_name': 'Project'},
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'Basic'", 'max_length': '12'}),
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