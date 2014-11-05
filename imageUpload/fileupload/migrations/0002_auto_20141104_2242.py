# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
    ]
