# Generated by Django 4.2.6 on 2023-10-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_merge_20231029_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='totalratings',
        ),
    ]
