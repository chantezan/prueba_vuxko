from django.db import models

# Create your models here.
class Bot(models.Model):
    #title
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    temp = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    def __str__(self):
        #return the task title
        return self.name + self.description

class Indicator(models.Model):
    #title
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    parameters = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, null=True)
    bot = models.ForeignKey(
        'Bot',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        #return the task title
        return self.name + self.description
