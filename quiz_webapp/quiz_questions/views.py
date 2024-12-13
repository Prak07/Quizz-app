from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answers , Catagory
import random
import os
from groq import Groq
# Create your views here.
def index(request):
    catagories=Catagory.objects.all()
    return render(request,"index.html",{"Catagories":catagories})


# Start a new quiz session
def start_quiz(request, category_id):
    Answers.objects.all().delete()
    # Store the selected category in the session
    request.session['selected_category_id'] = category_id
    return redirect("/get_question/")

# Get a random question
def get_question(request):
    category_id = request.session.get('selected_category_id')
    if not category_id:
        return redirect('/')
    
    number_of_questions = Question.objects.filter(Catagory=category_id).count()
    # Get the category
    category = get_object_or_404(Catagory, id=category_id)
    answered_count = Answers.objects.count()
    if answered_count >= 10 or answered_count >= number_of_questions:
        return redirect('/results/')
    
    answered_questions = Answers.objects.values_list('question_id', flat=True)
    questions = Question.objects.filter(Catagory=category_id).exclude(id__in=answered_questions)
    if questions.exists():
        question = random.choice(questions)
        if number_of_questions<10:
            return render(request, 'quiz.html', {'question': question, 'current_question': answered_count + 1,"number_of_questions":number_of_questions})
        else:
            return render(request, 'quiz.html', {'question': question, 'current_question': answered_count + 1,"number_of_questions":10})
    else:
        return redirect('/results/')

# Submit an answer
def submit_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        is_correct = user_answer == question.correct_option
        Answers.objects.create(
            question=question,
            user_answer=user_answer,
            correct_ans=question.correct_option,
            is_correct=is_correct
        )
    return redirect('/get_question/')

# View results
def quiz_results(request):
    results = Answers.objects.all()
    total_questions = results.count()
    correct_answers = results.filter(is_correct=True).count()
    incorrect_answers = total_questions - correct_answers
    return render(request,'results.html',{'results': results,'total_questions': total_questions,'correct_answers': correct_answers,'incorrect_answers': incorrect_answers,'percentage': (correct_answers / total_questions * 100)})

def reset_quiz(request):
    # Clear the selected category from session
    if 'selected_category_id' in request.session:
        del request.session['selected_category_id']
    
    # Redirect to index
    return redirect('/')

def explain(request,question_id,user_answer):
    question = get_object_or_404(Question, id=question_id)     
    match question.correct_option:
        case 'A':
            correct=question.option_a
        case 'B':
            correct=question.option_b
        case 'C':
            correct=question.option_c
        case 'D':
            correct=question.option_d

    match user_answer:
        case 'A':
            user_choice=question.option_a
        case 'B':
            user_choice=question.option_b
        case 'C':
            user_choice=question.option_c
        case 'D':
            user_choice=question.option_d
    try:
        # Initialize Groq client
        client = Groq(api_key="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")

        # Prepare the prompt
        explanation_prompt = (
            f"Question: {question.Question}\n"
            f"User Choice: {user_choice}\n"
            f"Correct Answer: {correct}\n"
            "Please provide a detailed explanation of this question"
        )

        # Generate explanation
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": explanation_prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        explanation = chat_completion.choices[0].message.content

    except Exception as e:
        print(e)
        explanation = "An error occurred while generating the explanation. Please try again later."

    # Render the explanation in the template
    return render(request, "explain.html", {"explanation": explanation,"question":question,"correct":correct,"user_choice":user_choice})