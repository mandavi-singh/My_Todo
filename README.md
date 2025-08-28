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
```
2. **Create and activate virtual environment**
   
```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```
3.**Install dependencies**

```bash
pip install -r requirements.txt
```
4.**Set PostgreSQL Database URL**

Create a free PostgreSQL database on Render.

Copy the database URL (something like postgresql://username:password@host:port/dbname).

Set it as an environment variable:
```bash
export DATABASE_URL="your_database_url_here" # Mac/Linux
set DATABASE_URL="your_database_url_here"    # Windows
```
5.**Run the application**
```bash
python app.py
```
Visit http://127.0.0.1:5000 to view your app locally.

**🗂️ Project Structure**

Project/

├─ app.py             # Main Flask application
├─ templates/         # HTML templates
│  ├─ index.html
│  ├─ update.html
│  └─ about.html
├─ static/
│  └─ style.css
├─ requirements.txt   # Python dependencies
└─ README.md

**🔗 Deployment on Render**

Go to Render
 and create a new web service.

Connect your GitHub repository.

Set Build Command: pip install -r requirements.txt

Set Start Command: gunicorn app:app

Set Environment Variable DATABASE_URL with your PostgreSQL URL.

Deploy and visit your live app.

**📌 Todos / Future Improvements**

Add user authentication (login/signup).

Implement task categories and due dates.

Add notifications for pending tasks.

Improve UI with Bootstrap or TailwindCSS.

Add error pages (404, 500) for better user experience.

**👩‍💻 Author**

Mandavi Singh
