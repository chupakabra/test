# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('gen_info_person', (
            ('id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name',
             self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name',
             self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email',
             self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber',
             self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype',
             self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other',
             self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('gen_info', ['Person'])

    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('gen_info_person')

    models = {
        'gen_info.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [],
                      {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [],
                   {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [],
                       {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [],
                          {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '20'}),
            'other': ('django.db.models.fields.TextField', [],
                      {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [],
                      {'max_length': '50'})
        }
    }

    complete_apps = ['gen_info']
