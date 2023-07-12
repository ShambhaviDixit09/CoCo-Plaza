from django.db import models

class Contacts(models.Model):
    name = models.CharField( max_length=120)
    email = models.CharField( max_length=120)
    phone = models.CharField( max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
              return self.name

# class City(models.Model):
#     name = models.CharField(max_length=100)
#     # Add other relevant fields, such as latitude and longitude

#     def __str__(self):
#         return self.name
