# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_location_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='position',
        ),
    ]
