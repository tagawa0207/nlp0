from django.db import models
from django.utils import timezone

# Create your models here.
class OriginalText(models.Model):
    original_text = models.CharField(max_length=4096)
    date = models.DateTimeField(auto_now_add=True)


class SummaryText(models.Model):
    original_text = models.ForeignKey(OriginalText, on_delete=models.CASCADE)
    summary_text = models.CharField(max_length=4096)
    date = models.DateTimeField(auto_now_add=True)

