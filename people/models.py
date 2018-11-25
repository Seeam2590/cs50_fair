from django.db import models

class people(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =50)
    house_class = models.CharField(max_length =50)
    about = models.TextField()

    def __str__(self):
        return self.name
