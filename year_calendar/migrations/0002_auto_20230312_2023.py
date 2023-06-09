# Generated by Django 3.2.14 on 2023-03-12 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('year_calendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='EventCancellations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_date', models.DateTimeField(verbose_name='Original Date')),
            ],
        ),
        migrations.CreateModel(
            name='EventParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=50, verbose_name='Rule ')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='year_calendar.event', verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_date', models.DateTimeField(verbose_name='Original Date')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='year_calendar.event', verbose_name='Event')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='year_calendar.eventparent', verbose_name='Parent')),
            ],
        ),
        migrations.AddField(
            model_name='eventparent',
            name='exceptions',
            field=models.ManyToManyField(to='year_calendar.Exception', verbose_name='Exceptions'),
        ),
    ]
