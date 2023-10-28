# Generated by Django 4.2.6 on 2023-10-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('catalog', '0002_userreview_userfavorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
