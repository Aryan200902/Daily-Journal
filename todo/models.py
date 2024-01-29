from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
