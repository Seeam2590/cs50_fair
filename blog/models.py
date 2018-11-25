from django.db import models

class blog(models.Model):
    author = models.CharField(max_length = 50, default='NA')
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    title = models.CharField(max_length = 50)
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pubdate.strftime(' %b %e %Y')

    def summary(self):
        return self.body[:100]
