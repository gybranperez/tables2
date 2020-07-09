from django.db import models
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="name", null=True)
    lastname = models.CharField(max_length=100, verbose_name="last name", null=True)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name