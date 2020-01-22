from django.db import models


# Create your models here.

class Website(models.Model):
    website = models.CharField(max_length=30)
    temp_keywords = models.TextField()

    @property
    def keywords(self):
        return self.temp_keywords.split(',')
