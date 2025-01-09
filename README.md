# Quiz Application with AI-Powered Explanations

This is a simple yet innovative quiz application built using Django. The app allows users to test their knowledge through multiple-choice questions (MCQs) and benefit from AI-powered explanations for incorrect answers, enhancing their learning experience.

## Features

- **Quiz Sessions**: Users can start a quiz session and answer random MCQs from a selected category.
- **Answer Submission**: Users can select answers for each question and submit them.
- **AI-Powered Explanations**: For any incorrect answers, an AI (powered by Groq API and Llama-3.3) provides a detailed explanation of why the selected answer was wrong and clarifies the correct answer.
- **Admin Interface**: An intuitive admin panel for managing quiz categories, questions, and answers.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python**: Version 3.8 or above.
- **Django**: Version 3.2 or above.
- **Groq API**: Version 0.13.0 for AI integration.

## Assumptions

1. **Category Selection**:
   - Users choose a category from the predefined list available in the database.
   - Categories represent various topics or quiz types.

2. **Quiz Duration**:
   - Each quiz session consists of 10 randomly selected MCQs from the chosen category.
   - Questions have four options (A, B, C, D), and users select one option as their answer.

3. **Answer Submission**:
   - Answers are submitted one by one.
   - The system evaluates each answer for correctness and stores the results in the database for future reference.

4. **AI Explanations for Incorrect Answers**:
   - Users can request an AI-generated explanation for incorrect answers.
   - The explanation provides insights into why the answer was incorrect and elaborates on the correct choice.

5. **Results**:
   - At the end of the quiz, users are shown their total score with a breakdown of correct and incorrect answers.
   - AI explanations are provided for all incorrect responses.

## Technologies Used

### Backend:
- **Django**: For web application development.
- **Groq API**: For generating AI-powered explanations.
- **SQLite**: To store categories, questions, and answers.

### Frontend:
- **HTML, CSS**: For creating a user-friendly and responsive interface.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Prak07/quiz-app.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd quiz-app
   ```

3. **Set up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up Environment Variables**:
   - Configure the Groq API key for AI integration.
   - Add `GROQ_API_KEY` to your environment variables.

6. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open `http://127.0.0.1:8000` in your browser.

## Usage

1. **Select a Category**:
   Choose a quiz category from the list.

2. **Answer Questions**:
   Respond to the questions presented one by one.

3. **Request AI Explanation**:
   For incorrect answers, request an AI explanation to understand the reasoning behind the correct choice.

4. **View Results**:
   At the end of the quiz, review your performance, including detailed explanations for incorrect responses.

## Contributions

This project was solely developed by **Prakhar Agarwal**, implementing the quiz logic, AI integration, and user interface.

## Acknowledgments

This application leverages the power of the Groq API and Llama-3.3 to deliver meaningful AI-driven explanations, enhancing the educational experience.

