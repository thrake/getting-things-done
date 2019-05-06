import datetime

from django.db import models
from django.utils import timezone

class Capture(models.Model):
    capture_text = models.CharField(max_length=500)
    capture_date = models.DateTimeField('date captured')
    notes = models.CharField(null=True, blank=True, max_length=2000)
    category = models.SmallIntegerField(default=0)
    status = models.SmallIntegerField(default=0)
    project = models.CharField(null=True, blank=True, max_length=500)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.capture_text
    def was_published_recently(self):
        return self.capture_date >= timezone.now() - datetime.timedelta(days=1)