# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemenus', '0004_menuitem_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='show',
            field=models.BooleanField(default=True, verbose_name='show'),
            preserve_default=True,
        ),
    ]
