# Generated by Django 2.2.6 on 2019-10-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testparcer', '0002_parceline_dtimefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceline',
            name='bytesread',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parceline',
            name='httpmethod',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='parceline',
            name='responsecode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='parceline',
            name='urlrequest',
            field=models.TextField(blank=True),
        ),
    ]
