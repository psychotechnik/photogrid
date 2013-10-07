# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chessboard'
        db.create_table(u'core_chessboard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Chessboard'])

        # Adding model 'Photo'
        db.create_table(u'core_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chessboard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Chessboard'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('column', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Chessboard'
        db.delete_table(u'core_chessboard')

        # Deleting model 'Photo'
        db.delete_table(u'core_photo')


    models = {
        u'core.chessboard': {
            'Meta': {'object_name': 'Chessboard'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.photo': {
            'Meta': {'object_name': 'Photo'},
            'chessboard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Chessboard']"}),
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']