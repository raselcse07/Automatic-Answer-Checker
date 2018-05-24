from django.db import models



class Question(models.Model):

    question_set        = models.CharField(max_length=200)
    tag_data            = models.CharField(max_length=200)


    def __str__(self):

        return str(self.question_set)
