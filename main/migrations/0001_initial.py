# Generated by Django 4.2.6 on 2023-12-19 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('bookformat', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('img', models.URLField(blank=True, null=True)),
                ('genre', models.TextField(choices=[('NOM', 'Nonfiction'), ('HIS', 'History'), ('GAM', 'Games'), ('ESO', 'Esoterica'), ('POE', 'Poetry'), ('CUL', 'Cultural'), ('REL', 'Religion'), ('ROM', 'Romance'), ('PRA', 'Prayer'), ('HTY', 'History'), ('CHE', 'Chess'), ('ATG', 'Astrology'), ('CAN', 'Canada'), ('SEQ', 'Sequential'), ('THE', 'Theology'), ('CTN', 'Christian'), ('EVG', 'Evangelism'), ('CTY', 'Christianity'), ('SCE', 'Science'), ('BFY', 'Biography'), ('MLT', 'Military')], default='NOM', max_length=3)),
                ('isbn', models.TextField(blank=True, null=True)),
                ('isbn13', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('reviews', models.IntegerField(blank=True, null=True)),
                ('totalratings', models.IntegerField(blank=True, null=True)),
                ('user_avg_rating', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
