# Generated by Django 4.2.7 on 2023-11-30 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messdeck', '0012_rename_attendance_attend'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='date',
            field=models.ForeignKey(default=datetime.date.today, on_delete=django.db.models.deletion.CASCADE, to='messdeck.date'),
        ),
    ]