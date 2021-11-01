from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer,
                               on_delete=models.CASCADE,
                               related_name='songs')

    def __str__(self):
        return self.title
