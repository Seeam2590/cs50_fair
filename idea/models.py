from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class idea(models.Model):
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    title = models.CharField(max_length = 50)
    pubdate = models.DateTimeField()
    url = models.TextField()
    icon = models.ImageField(upload_to = 'images/')
    votes_total = models.IntegerField(default = 1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pubdate.strftime(' %b %e %Y')
