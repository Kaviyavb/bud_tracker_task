# Bug Tracker API

A simple FastAPI-based backend application to manage issues with full CRUD functionality.

---

## 🚀 Features
- Create, Read, Update, Delete (CRUD) operations
- Input validation using Pydantic
- SQLite database with SQLAlchemy ORM
- Interactive API documentation (Swagger)

---

## 🛠️ Tech Stack
- Python  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Pydantic  

---

## 📂 Project Structure

bug_tracker_task/
├── main.py # API routes
├── models.py # Database models
├── schemas.py # Validation schemas
├── crud.py # Database logic
├── database.py # DB connection
└── README.md


---

## ▶️ How to Run

```bash
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn main:app --reload
🌐 Access the API
Swagger UI: http://127.0.0.1:8000/docs
Alternative Docs: http://127.0.0.1:8000/redoc
📌 API Endpoints
POST /issues → Create issue
GET /issues → Get all issues
GET /issues/{id} → Get issue by ID
PUT /issues/{id} → Update issue
DELETE /issues/{id} → Delete issue
🧪 Testing

Use Swagger UI to test all endpoints:
http://127.0.0.1:8000/docs