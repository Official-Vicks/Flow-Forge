🚀 Flow Forge API

Flow Forge is a backend API built with FastAPI, designed to simulate real-world backend development practices while strengthening my skills as a junior backend developer.

This project focuses on:

Clean architecture

Secure authentication

Scalable project structure

Production-ready backend patterns

Modular design for future frontend/mobile integration

🧠 Project Goals

Flow Forge is not just another CRUD API.

It is designed to:

Improve my understanding of backend architecture

Implement JWT-based authentication securely

Apply best practices in API design

Practice writing maintainable and scalable Python code

Serve as a foundation for future full-stack integration

🏗️ Tech Stack

Backend Framework: FastAPI

Language: Python

Authentication: JWT

Password Hashing: Passlib (bcrypt)

Database: (PostgreSQL / SQLite)

ORM: (SQLAlchemy)

Environment Management: Python-dotenv

API Documentation: Swagger UI (auto-generated)

📂 Project Structure
flow-forge/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── db/
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md

The structure follows a modular design to keep responsibilities separated and maintainable.

🔐 Authentication System

Flow Forge implements:

Secure password hashing using bcrypt

JWT access token generation

Token validation middleware

Protected routes with dependency injection

Security logic is structured in the core/security.py module.

🚧 Current Features

User registration

User login

JWT authentication

Protected routes

Role-based logic (if applicable)

🔮 Planned Improvements

Refresh tokens

Role-based access control (RBAC)

Logging system

Pagination utilities

Rate limiting

Dockerization

CI/CD setup

Deployment (Render / Railway / etc.)

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/flow-forge.git
cd flow-forge
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set up environment variables

Create a .env file:

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=your_database_url
5️⃣ Run the server
uvicorn app.main:app --reload

Visit:

http://127.0.0.1:8000/docs
📘 API Documentation

FastAPI automatically generates:

Swagger UI → /docs

ReDoc → /redoc

💡 Why This Project Matters

This project represents my commitment to becoming a strong backend developer by:

Writing clean, structured Python code

Following secure authentication practices

Building production-minded APIs

Continuously improving through refactoring

👨‍💻 Author

Built by Chidiebere Victory
Aspiring Backend Developer focused on Python & FastAPI.
