# Generated by Django 2.2.12 on 2020-05-20 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picarticles', '0004_auto_20200520_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='homearticle',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
