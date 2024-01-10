# Generated by Django 4.2.7 on 2023-11-27 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messdeck', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messdeck.date')),
            ],
        ),
        migrations.CreateModel(
            name='lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messdeck.date')),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
        migrations.AddField(
            model_name='breakfast',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messdeck.date'),
        ),
    ]
