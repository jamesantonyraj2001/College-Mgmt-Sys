# Generated by Django 4.0.8 on 2023-10-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_class_student_roll_number_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='class_attended',
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
