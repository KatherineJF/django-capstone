# Generated by Django 2.0.3 on 2019-01-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterparse', '0002_auto_20190109_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterparse',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='twitterparse',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
