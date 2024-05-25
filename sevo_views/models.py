from django.db import models

# Create your models here.


class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    

    def __str__(self):
        return self.get_fullname()
    
    class Meta():
        ordering = ["birthday"]