# here im making the model that will store incident info
# this model will create database table automatically

from django.db import models

class Incident(models.Model):
    # title field to store small heading about incident
    title = models.CharField(max_length=200)

    # description field to store full details of what happened
    description = models.TextField()

    # severity field to save how serious the incident is
    # like Low, Medium or High (just a text field here)

    severity = models.CharField(max_length=50)

    # reported_at will save date n time when record is created
    # auto_now_add=True means it will auto fill at creation

    reported_at = models.DateTimeField(auto_now_add=True)

    # here im overriding __str__ method
    # so that when we see object in admin it shows title not some id

    def __str__(self):
        return self.title

# Create your models here. (default comment by django when new app created)
