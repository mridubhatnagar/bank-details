# Generated by Django 2.2.9 on 2020-01-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankdetails', '0002_auto_20200123_1511'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banks',
            new_name='Bank',
        ),
    ]
