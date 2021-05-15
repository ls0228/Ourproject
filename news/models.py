from django.db import models

# Create your models here.
class Articels(models.Model):
    title = models.CharField('Name',max_length=50)
    anons = models.CharField('Anons',max_length=250)
    text = models.TextField('Text')
    date = models.DateTimeField('Date Publication')

    def __str__(self):
        return self.title