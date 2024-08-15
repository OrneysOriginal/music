# Generated by Django 5.1 on 2024-08-12 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0002_music_delete_musicmodel"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="music",
                related_query_name="music",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
