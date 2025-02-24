from django.db import models

# Create your models here.
class Mail(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email