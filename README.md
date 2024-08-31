# Task Manager

Task Manager is a web application built with Django for managing tasks.

## Features

- User authentication: Allows users to log in and manage their tasks.
- Task Management: Create, update, and delete tasks with ease.
- Clean and Responsive UI: A user-friendly interface for an optimal user experience.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1 - Clone the repository

2 - Navigate to the project directory:
cd django_project/

3 - Create a virtual environment:
python -m venv env

4 - Activate the virtual environment:

On Windows:
.\env\Scripts\activate

On macOS/Linux:
source env/bin/activate


5 - Install dependencies:
A- Navigate to directory where setup.py is located
- cd tasks/tasks
B - Install packages
- pip install -e .

6 - Apply migrations:
python manage.py makemigrations
python manage.py migrate


7 - Create superuser:
python manage.py createsuperuser
(add user - test, email- test@gmail.com, password- test)

8 - Run the development server:
python manage.py runserver

9 - Open your browser and go to http://127.0.0.1:8000/ to access the application.
enter the credentials you created at 7th step.
(example: username - test, password - test)
