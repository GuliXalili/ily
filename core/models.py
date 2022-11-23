from django.db import models

class Automobile(models.Model):
    typeauto = models.CharField(max_length=50)
    releaseyear = models.IntegerField(default=1900)
    color = models.CharField(max_length=50)
    img = models.TextField()
    price = models.IntegerField(default=20000)
    
    def __str__(self):
        return self.typeauto
