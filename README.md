# FlowForge 🚀

FlowForge is a **role-based workflow management API** built with **FastAPI**.  
It simulates the backend architecture of modern productivity tools like **Jira, Trello, or Asana**, focusing on clean architecture, authentication, permissions, and workflow tracking.

The project is designed as a **portfolio-ready backend system** that demonstrates real-world backend development practices.

---

## ✨ Features

### 🔐 Authentication System

- JWT-based authentication
- Access tokens and refresh tokens
- Secure password hashing using **Passlib (bcrypt)**
- Stateless authentication architecture

### 👥 User Management

- Role-based user system
- Roles:
  - `admin`
  - `manager`
  - `staff`
- User creation and management
- Secure password storage

### 📁 Project Management

- Create and manage projects
- Each project belongs to a user
- Projects can contain multiple tasks
- Role-based visibility and access

### 📌 Task Management

- Tasks belong to projects
- Tasks can be assigned to users
- Status workflow:
  - `todo`
  - `in_progress`
  - `done`
- Priority levels:
  - `low`
  - `medium`
  - `high`

### 📜 Activity Logging

Automatic system logs for actions such as:

- Project creation
- Task creation
- Task updates
- Task assignments

This creates a **timeline history similar to Jira or Asana activity feeds**.

### 🛡 Role-Based Permissions

Centralized permission layer controlling access to:

- User management
- Project creation
- Task assignment
- Workflow updates

---

## 🏗 Architecture

FlowForge follows a **modular and scalable backend structure**.
app/
│
├── api/
│ └── v1/
│ ├── auth.py
│ ├── users.py
│ ├── projects.py
│ ├── tasks.py
│ └── activities.py
│
├── core/
│ ├── config.py
│ ├── security.py
│ ├── dependencies.py
│ ├── permissions.py
│ └── activity_logger.py
│
├── crud/
│ ├── userCrud.py
│ ├── projectCrud.py
│ ├── taskCrud.py
│ └── activityCrud.py
│
├── db/
│ ├── base.py
│ ├── session.py
│ └── init_db.py
│
├── models/
│ ├── userModel.py
│ ├── projectModel.py
│ ├── taskModel.py
│ └── activityModel.py
│
├── schemas/
│ ├── userSchema.py
│ ├── projectSchema.py
│ ├── taskSchema.py
│ └── activitySchema.py
│
└── main.py

This structure separates:

- **Data models**
- **Business logic**
- **API routes**
- **Core services**

---

## 🧠 Workflow Model

The system follows a hierarchical workflow:
User
└── Project
└── Task
└── Activity Log

### Role Permissions

| Role    | Permissions               |
| ------- | ------------------------- |
| Admin   | Full system access        |
| Manager | Create projects and tasks |
| Staff   | Work on assigned tasks    |

---

## 🛠 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **PostgreSQL / SQLite** – Database
- **Pydantic** – Data validation
- **JWT** – Authentication
- **Passlib (bcrypt)** – Password hashing

---

## 📌 Example API Endpoints

### Authentication

POST /auth/register
POST /auth/login
POST /auth/refresh

### Users

GET /users
GET /users/{id}
PATCH /users/{id}
DELETE /users/{id}

### Projects

POST /projects
GET /projects
GET /projects/{id}
PATCH /projects/{id}
DELETE /projects/{id}

### Tasks

POST /tasks
GET /tasks
PATCH /tasks/{id}
DELETE /tasks/{id}

### Activities

GET /activities/projects/{project_id}
GET /activities/tasks/{task_id}

---

## 🚀 Running the Project

### 1️⃣ Clone the repository

git clone https://github.com/yourusername/flowforge.git

cd flowforge

### 2️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate

Windows:

venv\Scripts\activate

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Configure environment variables

Create `.env`

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 5️⃣ Run the server

uvicorn app.main:app --reload

---

## 📖 API Documentation

FastAPI automatically generates interactive docs.

Swagger UI:

http://127.0.0.1:8000/docs

Redoc:

http://127.0.0.1:8000/redoc

---

## 📈 Future Improvements

Planned enhancements include:

- Pagination & filtering
- Advanced RBAC policies
- Task assignment endpoints
- Email notifications
- Docker containerization
- Background job processing
- WebSocket activity updates

---

## 🎯 Purpose of This Project

FlowForge was built to demonstrate **real backend engineering practices**, including:

- modular architecture
- authentication systems
- role-based permissions
- workflow modeling
- activity tracking
