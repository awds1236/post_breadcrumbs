from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    parent_page = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

