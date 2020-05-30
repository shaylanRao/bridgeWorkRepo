# Generated by Django 2.2.12 on 2020-05-25 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picarticles', '0006_homearticle_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]