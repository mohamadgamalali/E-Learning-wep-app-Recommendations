from django.db import models


class Company (models.Model):
    companyId = models.CharField(max_length=250)
    companyName = models.CharField(max_length=250)
    companyInterest = models.CharField(max_length=250)

    def __str__(self):
        return self.companyName + " - " + self.companyInterest
