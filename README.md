# 📚 Library Management System

## 📝 Overview
This project is a **Library Management System** built using **Django 5.1.1** and **Django REST Framework (DRF)**. The application includes Admin functionality to manage books and a Student view to explore available books. The project uses MySQL as the database. The system provides the following functionalities:

### 🔐 Admin Operations
- **Admin Signup:** Create a new admin account using email, username, and password.
- **Admin Login:** Authenticate admin and return a token for future requests.

### 📚 Book Management
- **Create:** Admin can add new books.
- **Read:** Retrieve a list of all available books.
- **Update:** Admin can modify book details.
- **Delete:** Admin can delete a book record.

### 🎓 Student View
- Provides a UI where students can view all available books with search functionality.

---

## 🚀 Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Frontend** Django Templates (HTML, CSS, Bootstrap)

---

## 📁 Project Structure
```
Library_System/
├── books/
│   ├── __init__.py
|   ├── templates/
│   │   └── home.html
│   ├── admin.py
|   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── library_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py                     
└── README.md 
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database
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

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to see the book listing.

---

## 🔥 API Endpoints

### Admin Operations
| Method | Endpoint           | Description        |
|--------|-------------------|--------------------|
| POST   | /api/admin/signup/ | Admin Registration |
| POST   | /api/admin/login/  | Admin Login        |

### Book Management
| Method   | Endpoint            | Description              |
|----------|--------------------|--------------------------|
| POST     | /api/admin/book/create/ | Add a new book      |
| GET      | /api/admin/book/list/   | Get all books        |
| PUT      | /api/admin/book/update/{id}/ | Update book info |
| DELETE   | /api/admin/book/delete/{id}/ | Delete a book    |

### Student View
| Method | Endpoint     | Description       |
|--------|--------------|-------------------|
| GET    | /            | View book list UI |

---

## 🎨 Student UI
The student view provides a clean and modern UI to display the list of available books with a search option.

---

## 🧪 Running Tests
To run unit tests:
```bash
python manage.py test
```

---

## 📄 Assumptions & Considerations
1. Admin user requires email, username, and password for signup.
2. Only authenticated admins can perform CRUD operations on books.
3. Students can only view book records.

---


## 🤝 Contributors
- **Prajakta Kolhe**

