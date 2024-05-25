from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField()

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def __str__(self):
        return f"{self.get_fullname()}"
    
    class Meta:
        ordering = ["-birthday"]