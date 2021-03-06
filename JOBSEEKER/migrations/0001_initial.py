# Generated by Django 3.1.4 on 2021-01-03 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QUALIFICATIONS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('xii_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grad_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('profile_pic', models.ImageField(blank=True, upload_to='JOBSEEKER/PROFILE/')),
                ('resume', models.FileField(blank=True, upload_to='JOBSEEKER/RESUME/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JOBSEEKER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField()),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
