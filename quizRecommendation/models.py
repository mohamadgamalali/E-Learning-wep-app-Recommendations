from django.db import models


class Quizzes (models.Model):
    quizProgrammingLanguage = models.CharField(max_length=250)
    quizSkill = models.CharField(max_length=250)

    def __str__(self):
        return self.quizProgrammingLanguage + ' - ' + self.quizSkill

