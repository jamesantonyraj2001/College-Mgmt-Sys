# Generated by Django 4.0.8 on 2023-10-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_notification_alter_attendance_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
