# Generated by Django 2.0.2 on 2018-03-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180327_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='request_comments',
            field=models.TextField(help_text='Enter a brief description of the request', max_length=2000),
        ),
    ]