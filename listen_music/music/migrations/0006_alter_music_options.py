# Generated by Django 5.1 on 2024-08-15 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0005_music_name_alter_music_music"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="music",
            options={"ordering": ["-id"]},
        ),
    ]
