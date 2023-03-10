# Generated by Django 4.1.4 on 2023-01-12 16:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapui', '0006_alter_scrapitem_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapitem',
            name='city',
        ),
        migrations.RemoveField(
            model_name='scrapitem',
            name='state',
        ),
        migrations.AlterField(
            model_name='scrapitem',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scrapitem',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Invalid phone number ', regex='(0|91)?[6-9][0-9]{9}')]),
        ),
    ]
