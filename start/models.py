from django.db import models


class Songs(models.Model):
    
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey('auth.User',related_name='songs', on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)