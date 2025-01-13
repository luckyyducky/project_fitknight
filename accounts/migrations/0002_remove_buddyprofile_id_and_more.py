import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buddyprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='activity_type',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='schedule',
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='activity_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cardio', 'Cardio'), ('Strength Training', 'Strength Training'), ('Meditation', 'Meditation'), ('Team Sports', 'Team Sports')], max_length=47),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='locations',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Gym A', 'Gym A'), ('Gym B', 'Gym B'), ('Park', 'Park'), ('Community Center', 'Community Center')], max_length=33),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='schedules',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Biweekly', 'Biweekly')], max_length=21),
        ),
        migrations.AlterField(
            model_name='buddyprofile',
            name='availability',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('weekends', 'Weekends')], max_length=34),
        ),
        migrations.AlterField(
            model_name='buddyprofile',
            name='fitness_goals',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Weight Loss', 'Weight Loss'), ('Muscle Gain', 'Muscle Gain'), ('General Fitness', 'General Fitness'), ('Cardio', 'Cardio'), ('Flexibility', 'Flexibility')], max_length=58),
        ),
        migrations.AlterField(
            model_name='buddyprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='buddyprofile',
            name='workout_preferences',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('gym', 'Gym'), ('yoga', 'Yoga'), ('running', 'Running'), ('cycling', 'Cycling'), ('swimming', 'Swimming')], max_length=33),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
