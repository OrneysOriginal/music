from django.contrib import admin

from music.models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        Music.music.field.name,
        Music.like.field.name,
        Music.dislike.field.name,
    )
