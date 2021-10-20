from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name