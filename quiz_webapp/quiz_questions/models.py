from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create your models here.
class Question(models.Model):
    Catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Question=models.CharField(max_length=1000)
    option_a=models.CharField(max_length=100)
    option_b=models.CharField(max_length=100)
    option_c=models.CharField(max_length=100)
    option_d=models.CharField(max_length=100)
    correct_option=models.CharField(max_length=100)
    
    def __str__(self):
        return f"Q: {self.Question} | C: {self.Catagory.name}"

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer =models.CharField(max_length=1)
    correct_ans=models.CharField(max_length=10,null=True)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return f"Q: {self.question.Question}"