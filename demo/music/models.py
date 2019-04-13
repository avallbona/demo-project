from django.contrib.auth import get_user_model
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    artists = models.ManyToManyField(Artist, through='Calification')

    def __str__(self):
        return '{} - {}'.format(self.user, self.name)


class Calification(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='califications')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.portfolio, self.artist, self.rate)

