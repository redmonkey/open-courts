# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='status',
            field=models.CharField(default=b'PE', max_length=2, choices=[(b'AP', b'Approved'), (b'PE', b'Pending')]),
            preserve_default=True,
        ),
    ]
