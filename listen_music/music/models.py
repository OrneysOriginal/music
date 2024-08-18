from django.core.validators import validate_slug
from django.db import models
from django.utils.safestring import mark_safe


class Music(models.Model):
    name = models.CharField(max_length=255, validators=[validate_slug])
    music = models.FileField(upload_to="music/%Y/%m/%d/", help_text="Музыка")
    like = models.IntegerField(default=0, null=True)
    dislike = models.IntegerField(default=0, null=True)

    def get_music(self):
        return mark_safe(
            f'<audio controls="controls" preload="auto"'
            f' src="media/{self.music}" id="myaudio"></audio>'
        )

    class Meta:
        ordering = ["-id"]
