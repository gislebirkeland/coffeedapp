# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151205_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
    ]
