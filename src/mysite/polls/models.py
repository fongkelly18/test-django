import datetime
from django.db import models
from django.utils import timezone

'''
Create your models here - the code will create a DB schema (i.e. CREATE TABLE statements) 
and create a Python db-access API for accessing Question + Choice Objects (aka tables)

Model is represented by a class that subclass of model (models.Model)
- Each model aka table has fields/columns 
(CharField = text fields, IntField = Integer Field, DateTimeField = date/time columns)
- Foreign Key is same concept as SQL. Supports many DB relationships: many-1, many-many, 1-1

Important Notes:
- add __str__() methods to your models

When "querying the DB", the below are how to utilize the DB API:
- Question.objects.filter(id=1)
- Question.objects.filter(question_text__startswith="What")
- Question.objects.get(id=1)
- Question.objects.get(pk=1) #to get the PK
'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text