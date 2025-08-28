# My Todo App

A simple **Todo application** built using **Flask** and **PostgreSQL**, deployed on **Render**. This app allows users to create, read, update, and delete todos with persistent storage.

---

## 🔗 Live Demo

[https://my-todo-sngt.onrender.com/](https://my-todo-sngt.onrender.com/)

---

## 🛠️ Features

- Add, update, delete, and view todos.
- Store todos in a PostgreSQL database.
- Web interface built using Flask templates.
- Fully deployed on Render cloud platform.
- Simple and clean UI with CSS styling.

---

## 💻 Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS
- **Deployment**: Render

---

## 🏗️ Setup & Installation

1. **Clone the repository**

```bash
git clone <your-repo-link>
cd Project/Flask
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
pip install -r requirements.txt
```
Set PostgreSQL Database URL


Create a free PostgreSQL database on Render.

Copy the database URL (something like postgresql://username:password@host:port/dbname).

Set it as an environment variable:
export DATABASE_URL="your_database_url_here" # Mac/Linux
set DATABASE_URL="your_database_url_here"    # Windows
