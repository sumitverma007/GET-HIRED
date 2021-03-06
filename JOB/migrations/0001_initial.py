# Generated by Django 3.1.4 on 2021-01-03 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EMPLOYER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=100)),
                ('job_desc', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('x_req', models.DecimalField(decimal_places=2, max_digits=5)),
                ('xii_req', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grad_req', models.DecimalField(decimal_places=2, max_digits=5)),
                ('employer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPLOYER.employer')),
            ],
        ),
    ]
