# Generated by Django 5.1.4 on 2025-01-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_portal', '0006_remove_buddyprofile_show_id_in_buddy_portal'),
    ]

    operations = [
        migrations.AddField(
            model_name='buddyprofile',
            name='show_in_buddy_finder',
            field=models.BooleanField(default=True),
        ),
    ]
