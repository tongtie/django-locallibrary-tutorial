# Generated by Django 2.2.5 on 2019-10-22 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20181028_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]
