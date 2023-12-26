from django.db import models
from ckeditor.fields import RichTextField


class Note(models.Model):
    title = models.CharField(max_length=64, verbose_name="Title")
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at: ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at: ")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
