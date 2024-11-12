from django.db import models

class Name(models.Model):
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()

    def __str__(self):  
        return self.username + " " + str(self.password)