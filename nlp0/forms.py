from django import forms
from django.db import models

class LangChoices(models.TextChoices):
    JAPANESE = 'japanese', '日本語'
    ENGLISH = 'english', 'English'


class LangForm(forms.Form):
    which_lang = forms.fields.ChoiceField(
        choices=LangChoices.choices,
        required=True,
        label='Language',
        # widget=forms.widgets.Select,
    )

class TextareaForm(forms.Form):
    original_text = forms.fields.CharField(
        required=True,
        widget=forms.Textarea,
    )
