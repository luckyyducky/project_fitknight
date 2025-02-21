# Generated by Django 5.1.4 on 2025-01-16 10:12

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_portal', '0008_remove_buddyprofile_show_in_buddy_finder'),
    ]

    operations = [
        migrations.AddField(
            model_name='buddyprofile',
            name='location',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('park', 'Park'), ('gym', 'Gym'), ('community center', 'Community Center'), ('beach', 'Beach'), ('indoor', 'Indoor Facility'), ('outdoor', 'Outdoor Location')], max_length=46),
        ),
    ]
