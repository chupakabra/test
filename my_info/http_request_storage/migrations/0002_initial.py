# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestStorage'
        db.create_table('http_request_storage_httprequeststorage', (
            ('id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('path',
             self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('http_request_storage', ['HttpRequestStorage'])

    def backwards(self, orm):
        # Deleting model 'HttpRequestStorage'
        db.delete_table('http_request_storage_httprequeststorage')

    models = {
        'http_request_storage.httprequeststorage': {
            'Meta': {'object_name': 'HttpRequestStorage'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [],
                   {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [],
                     {'max_length': '100'})
        }
    }

    complete_apps = ['http_request_storage']
