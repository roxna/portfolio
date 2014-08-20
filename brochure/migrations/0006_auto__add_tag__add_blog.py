# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'brochure_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'brochure', ['Tag'])

        # Adding M2M table for field blog on 'Tag'
        m2m_table_name = db.shorten_name(u'brochure_tag_blog')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'brochure.tag'], null=False)),
            ('blog', models.ForeignKey(orm[u'brochure.blog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'blog_id'])

        # Adding model 'Blog'
        db.create_table(u'brochure_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tag_line', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abstract', self.gf('django.db.models.fields.TextField')(null=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date_written', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'brochure', ['Blog'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'brochure_tag')

        # Removing M2M table for field blog on 'Tag'
        db.delete_table(db.shorten_name(u'brochure_tag_blog'))

        # Deleting model 'Blog'
        db.delete_table(u'brochure_blog')


    models = {
        u'brochure.blog': {
            'Meta': {'object_name': 'Blog'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_written': ('django.db.models.fields.DateField', [], {'null': 'True'}),
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
        u'brochure.project': {
            'Meta': {'object_name': 'Project'},
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'Basic'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'brochure.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'to': u"orm['brochure.Project']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        u'brochure.tag': {
            'Meta': {'object_name': 'Tag'},
            'blog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['brochure.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['brochure']