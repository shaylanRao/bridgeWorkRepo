# Generated by Django 2.2.12 on 2020-05-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picarticles', '0003_auto_20200520_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homearticle',
            name='videofile',
            field=models.FileField(null=True, upload_to='blog/static/images', verbose_name=''),
        ),
    ]
