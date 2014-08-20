# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.date'
        db.delete_column(u'brochure_project', 'date')

        # Adding field 'Project.description'
        db.add_column(u'brochure_project', 'description',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)

        # Adding field 'Project.website'
        db.add_column(u'brochure_project', 'website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Project.date_created'
        db.add_column(u'brochure_project', 'date_created',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 8, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.date'
        db.add_column(u'brochure_project', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 8, 0, 0)),
                      keep_default=False)

        # Deleting field 'Project.description'
        db.delete_column(u'brochure_project', 'description')

        # Deleting field 'Project.website'
        db.delete_column(u'brochure_project', 'website')

        # Deleting field 'Project.date_created'
        db.delete_column(u'brochure_project', 'date_created')


    models = {
        u'brochure.project': {
            'Meta': {'object_name': 'Project'},
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'Basic'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['brochure']