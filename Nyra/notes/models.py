# No seu aplicativo, crie ou ajuste o arquivo models.py
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at: ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at: ")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
