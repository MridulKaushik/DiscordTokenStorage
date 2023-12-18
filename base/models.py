from django.db import models


# Create your models here.
class DiscordServer(models.Model):
    server_id = models.CharField(max_length=255)
    auth_code = models.CharField(max_length=255)
    auth_token = models.CharField(max_length=255)

    class Meta:
        ordering = ['server_id', 'auth_code']

