from django.db import models

# Create your models here.

"""
User Model
Defines the attributes of a user
"""
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=255)
    
    def get_name(self):
        return 'First Name: ' + self.first_name + ' Last Name: ' + self.last_name
    
    def __repr__(self):
        return self.get_name + ' is added.'
