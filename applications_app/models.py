from datetime import date
from django.conf import settings
from django.db import models


class ApplicationItem(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    get_an_invitation = models.BooleanField(default=False)
    applied_on = models.DateField(default=date.today())
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="application_item")

    class Meta:
        app_label = "applications_app"
        db_table = "application_item"
        verbose_name = "application_item"
        verbose_name_plural = "application_items"

    def __str__(self):
        return self.company
