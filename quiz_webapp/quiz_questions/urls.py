from django.urls import path,include
from.views import *
urlpatterns = [
    path("",index,name="index"),
    
    # Start quiz for a specific category
    path('start_quiz/<int:category_id>/', start_quiz, name='start_quiz'),
    
    # Get next question in the quiz
    path('get_question/', get_question, name='get_question'),
    
    # Submit an answer for a specific question
    path('submit_answer/<int:question_id>/', submit_answer, name='submit_answer'),
    
    # View quiz results
    path('results/', quiz_results, name='results'),
    
    # Reset the quiz
    path('reset-quiz/', reset_quiz, name='reset_quiz'),
    
    path('explain/<int:question_id>/<str:user_answer>/', explain, name='reset_quiz'),
]