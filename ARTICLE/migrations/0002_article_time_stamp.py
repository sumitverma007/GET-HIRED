# Generated by Django 3.1.2 on 2021-01-13 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ARTICLE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
