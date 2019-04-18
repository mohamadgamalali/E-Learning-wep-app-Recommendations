from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Users (models.Model):
    userId = models.CharField(max_length=250)
    userName = models.CharField(max_length=250)
    userInterest = models.CharField(max_length=250)
    userSkillScore = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.userId + ' - ' + self.userName + ' - ' + self.userInterest + ' - ' + str(self.userSkillScore)

