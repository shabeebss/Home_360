# Generated by Django 3.2.25 on 2024-12-16 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20241216_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='camera_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_number', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='report_table',
            name='POLICE_STATION',
        ),
        migrations.AddField(
            model_name='report_table',
            name='CAM_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.camera_table'),
            preserve_default=False,
        ),
    ]
