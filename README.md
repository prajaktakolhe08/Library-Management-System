# 📚 Library Management System

## Overview
This project is a **Library Management System** built using **Django 5.1.1** and **Django REST Framework (DRF)**. The application includes Admin functionality to manage books and a Student view to explore available books. The project uses MySQL as the database. The system provides the following functionalities:

### Admin Operations
- **Admin Signup:** Create a new admin account using email, username, and password.
- **Admin Login:** Authenticate admin and return a token for future requests.

### Book Management
- **Create:** Admin can add new books.
- **Read:** Retrieve a list of all available books.
- **Update:** Admin can modify book details.
- **Delete:** Admin can delete a book record.

### Student View
- Provides a UI where students can view all available books with search functionality.

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Frontend** Django Templates (HTML, CSS, Bootstrap)

## Demo

- Library Management System Demo

<table> <tr> <td width="65%"> <video src="https://github.com/user-attachments/assets/b1450434-33fc-425e-b825-5eab4debe063" controls width="100%"></video> </td> <td width="35%"> The demo showcases: - 🔐 Admin Authentication: Admin can sign up and log in to manage the library. - 📚 Book Management: Admin can add, update, delete, and view books. - 🎓 Student View: Students can search and explore the list of available books. - 📄 RESTful API Operations: Endpoints allow CRUD operations using Django REST Framework (DRF). - ✅ Token-Based Authentication: Secure login and token-based access for APIs. </td> </tr> </table>

## Project Structure
```
Library_System/
├── books/                         # App handling book management
|   ├── templates/                 # HTML templates for views
│   │   └── home.html              # Home page for listing books
│   ├── admin.py                   # Admin panel settings
|   ├── apps.py                    # App configuration
│   ├── models.py                  # Database models
│   ├── serializers.py             # Serializers to convert models to JSON
│   ├── urls.py                    # URL patterns for the app
│   └── views.py                   # Business logic and API handling
├── library_system/                # Main Django project directory
│   ├── __init__.py                # Marks the directory as a package
│   ├── asgi.py                    # ASGI configuration for the project
│   ├── settings.py                # Project settings and configurations
│   ├── urls.py                    # Root URL configuration
│   └── wsgi.py                    
├── manage.py                      # Project management script
├── requirements.txt               # Dependencies and package list
└── README.md                      # Project documentation
```

## Installation & Setup

Follow these steps to set up and run the project on your local machine
1. **Clone the repository**

    Download the Project by running:
    ```bash
    git clone https://github.com/yourusername/Library-Management-System.git
    cd library-management-system
    ```

2. **Create and activate a virtual environment**

   It’s best to use a virtual environment to manage dependencies. Run the following command:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate    # For Windows
    ```

3. **Install required packages**
   
   Run the following command to install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure MySQL Database**
   
    Update `settings.py` with your MySQL database credentials:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'library_system_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Run Migrations**
   
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Server**
   
   Start the web application:
    ```bash
    python manage.py runserver
    ```
   The application will be accessible at `http://127.0.0.1:8000/`
   

## API Endpoints

**Admin Operations**

| Method | Endpoint           | Description        |
|--------|-------------------|--------------------|
| POST   | /api/admin/signup/ | Admin Registration |
| POST   | /api/admin/login/  | Admin Login        |

**Book Management**

| Method   | Endpoint            | Description              |
|----------|--------------------|--------------------------|
| POST     | /api/admin/book/create/ | Add a new book      |
| GET      | /api/admin/book/list/   | Get all books        |
| PUT      | /api/admin/book/update/{id}/ | Update book info |
| DELETE   | /api/admin/book/delete/{id}/ | Delete a book    |

**Student View**

| Method | Endpoint     | Description       |
|--------|--------------|-------------------|
| GET    | /            | View book list UI |


## Student UI
The student view provides a clean and modern UI to display the list of available books with a search feature.

## Running Tests
To run unit tests:

```bash
python manage.py test
```

## Screenshots

### 🔐 Admin Operations

**Admin Signup**

<img alt="Homepage" src="https://github.com/user-attachments/assets/76a2ebad-c5c0-4892-9744-9c3b91829acc" width="500">
<img alt="Homepage" src="https://github.com/user-attachments/assets/863dc9f8-244f-4ef1-b9a0-b3762aa42439" width="500">

**Admin Login**

<img alt="Homepage" src="https://github.com/user-attachments/assets/aa3c1d22-dfc9-48db-b95d-1ea6516c440e" width="500">
<img alt="Homepage" src="https://github.com/user-attachments/assets/9189e5ea-7c22-48ca-a314-bd60a57d10fd" width="500">

**Create Book**

<img alt="Homepage" src="https://github.com/user-attachments/assets/66de1eab-4400-4f99-b447-c78282d8ab2d" width="500">
<img alt="Homepage" src="https://github.com/user-attachments/assets/c10433fd-b183-4b75-a4c2-ae1ab2e30e98" width="500">

**Update Book**

<img alt="Homepage" src="https://github.com/user-attachments/assets/2bb9a743-a614-4c90-a947-3ef5a1125d63" width="500">
<img alt="Homepage" src="https://github.com/user-attachments/assets/a6016270-241a-4694-94b2-5aa8becb8537" width="500">

**Delete Book**

<img alt="Homepage" src="https://github.com/user-attachments/assets/3d96a539-1362-44ae-a169-53f651e78e81" width="500">
<img alt="Homepage" src="https://github.com/user-attachments/assets/78d86de9-1ef8-4746-8f0f-0b5b0a26a533" width="500">

**List of Books (Admin)**

<img alt="Homepage" src="https://github.com/user-attachments/assets/0a61681d-d42a-4a41-8818-ab2b7e2150f6" width="500">


### 🎓 Student View

**View Available Books**

<img alt="Homepage" src="https://github.com/user-attachments/assets/7a3c356c-2048-4dd7-b830-2ecf82566db0" width="500">

## Assumptions & Considerations

1. Admin user requires email, username, and password for signup.
2. Only authenticated admins can perform CRUD operations on books.
3. Students can only view book records.

## Contact

If you have any questions or would like to contribute, feel free to email me or connect with me on [Linkedin](https://linkedin.com/in/prajakta-kolhe08).

⭐ **If you like this project, don't forget to give it a star!** ⭐

