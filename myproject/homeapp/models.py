from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    query=models.TextField(max_length=250,blank=True, null=True)

    #def __str__(self):
        #return self.name
        


