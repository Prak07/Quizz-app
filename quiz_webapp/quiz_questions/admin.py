from django.contrib import admin
from .models import Catagory, Question, Answers

# Register your models here.
admin.site.register(Catagory)
admin.site.register(Question)
admin.site.register(Answers)