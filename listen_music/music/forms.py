from django import forms

from music.models import Music


class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ["name", "music"]
        widgets = {
            "name": forms.TextInput(),
            "music": forms.FileInput(),
        }
        help_texts = {
            "name": "Название музыки",
        }
