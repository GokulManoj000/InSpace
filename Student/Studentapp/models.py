from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HomeworkFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    file = models.FileField(upload_to='homework_files/')  # File upload
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.file.name
