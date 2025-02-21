# Generated by Django 5.1.4 on 2025-01-13 08:55

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, null=True, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='group_pics/')),
                ('description', models.TextField(blank=True, null=True)),
                ('activity_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('gym', 'Gym'), ('yoga', 'Yoga'), ('running', 'Running'), ('cycling', 'Cycling'), ('swimming', 'Swimming'), ('dance', 'Dance'), ('aerobics', 'Aerobics')], max_length=48)),
                ('schedule', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('weekends', 'Weekends'), ('weekday nights', 'Weekday Nights')], max_length=49)),
                ('location', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('park', 'Park'), ('gym', 'Gym'), ('community center', 'Community Center'), ('beach', 'Beach'), ('indoor', 'Indoor Facility'), ('outdoor', 'Outdoor Location')], max_length=46)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
