from django.db import models
from user_auth.models import CustomUsers


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(CustomUsers , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created_at = models .DateTimeField(auto_now_add=True)
