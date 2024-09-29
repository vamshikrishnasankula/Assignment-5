
# Hello World Django App

A simple Django web application that returns a "Hello World" message in JSON format. 

It contains a single route that responds with `{"Message": "Hello World!"}`.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Git
- Django (you can install it using pip)

## How to Run

Follow these steps to clone and run the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vamshikrishnasankula/Assignment-5
   cd Assignment-5
   cd helloworld_django
   ```

2. **Install Django:**
   ```bash
   pip install django
   ```

3. **Run the migrations (if necessary):**
   ```bash
   python manage.py migrate
   ```

4. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the app:**
   - Open your browser and navigate to `http://127.0.0.1:8000/`.
   - You should see the JSON response: 
     ```json
     {
       "Message": "Hello World!"
     }
     ```



