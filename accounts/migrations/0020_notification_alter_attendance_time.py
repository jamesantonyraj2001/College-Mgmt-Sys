# Generated by Django 4.0.8 on 2023-10-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_attendance_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=20, null=True)),
                ('content', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time',
            field=models.CharField(default=304, max_length=10),
            preserve_default=False,
        ),
    ]
