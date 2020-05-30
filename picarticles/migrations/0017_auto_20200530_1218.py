# Generated by Django 2.2.12 on 2020-05-30 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picarticles', '0016_auto_20200530_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homearticle',
            name='videofile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]