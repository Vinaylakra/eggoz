from django.db import models

# Create your models here.


class Eggoz2(models.Model):
    studentid = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=100)
    studentloc = models.TextField()
    studentphon = models.IntegerField()
    genchoice = [
        ('boy','boy'),
        ('girl','girl'),
    ]
    studentgen = models.CharField(
        max_length=5,
        choices=genchoice,
        default=None
    )
    addeddate = models.DateTimeField(auto_now=True)








    