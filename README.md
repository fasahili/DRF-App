# 🧪 DRF Playground Project

This is a Django Rest Framework (DRF) playground project built for learning and experimenting with building RESTful APIs.
It includes multiple apps such as `quickstart`, `snippets`, and `service` --- each designed to demonstrate various features of DRF including serialization, views, permissions, and more.

-----

## 📦 Project Structure

drfapp/\
├── drfapp/ # Main Django project\
├── quickstart/ # Basic DRF app\
├── service/ # Utility or service logic\
├── snippets/ # App for code snippet API\
├── manage.py\
├── db.sqlite3\
└── README.md

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/play-with-drf.git
cd play-with-drf

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


# Apply migrations and start the server
python manage.py migrate
python manage.py runserver

```

---
🔗 API Endpoints
----------------

Base URL: `http://127.0.0.1:8000/api/`

| Endpoint | Method(s) | Description |
| --- | --- | --- |
| `/users/` | GET, POST | List or create users |
| `/users/<id>/` | GET, PUT, DELETE | Retrieve, update or delete a user |
| `/groups/` | GET, POST | List or create groups |
| `/appointments/` | GET, POST | List or create service appointments |
| `/appointments/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete appointment |
| `/snippets/` | GET, POST | List or create code snippets |
| `/snippets/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete snippet |

* * * * *

### 📎 Postman Documentation

If you have a Postman collection, link it here:

[🔗 Postman Docs](https://documenter.getpostman.com/view/34356312/2sB2qUnjnY)

* * * * *

🧠 Features
-----------

-   Modular app design with DRF

-   Serialization & Deserialization

-   Permissions & Authentication

-   SQLite default database (easy setup)

* * * * *
