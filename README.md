# Bug Tracker API

A simple backend API for managing issues using FastAPI.

## 🚀 Features
- Create, Read, Update, Delete issues
- Input validation using Pydantic
- SQLite database with SQLAlchemy
- Interactive API docs using Swagger
- Automatic database table creation
- RESTful API design

## 🛠️ Tech Stack
- **Python** - Programming language
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 📂 Project Structure
```
bug_tracker_task/
├── main.py          # FastAPI application and routes
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic validation schemas
├── crud.py          # Database CRUD operations
├── database.py      # Database configuration and session management
├── requirements.txt # Python dependencies
├── bugtracker.db    # SQLite database (auto-generated)
└── README.md        # Project documentation
```

## 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## ▶️ How to Run

### 1. Clone/Download the Project
```bash
cd path/to/bug_tracker_task
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

### 6. Access the API
- **API Base URL**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📚 API Endpoints

### Issues Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/issues` | Create a new issue |
| `GET` | `/issues` | Get all issues (with pagination) |
| `GET` | `/issues/{id}` | Get issue by ID |
| `PUT` | `/issues/{id}` | Update an existing issue |
| `DELETE` | `/issues/{id}` | Delete an issue |

### Issue Schema

**Issue Fields:**
- `id` (integer): Auto-generated unique identifier
- `title` (string): Issue title (required, 1-255 characters)
- `description` (string): Issue description (optional, max 5000 characters)
- `priority` (string): Priority level - "Low", "Medium", "High"
- `status` (string): Status - "Open", "In Progress", "Closed"

## 🔧 API Usage Examples

### Create an Issue
```bash
curl -X POST "http://localhost:8000/issues" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Fix login bug",
       "description": "Users cannot log in with valid credentials",
       "priority": "High",
       "status": "Open"
     }'
```

### Get All Issues
```bash
curl -X GET "http://localhost:8000/issues"
```

### Get Issue by ID
```bash
curl -X GET "http://localhost:8000/issues/1"
```

### Update an Issue (Partial Update)
```bash
curl -X PUT "http://localhost:8000/issues/1" \
     -H "Content-Type: application/json" \
     -d '{
       "status": "In Progress",
       "priority": "Medium"
     }'
```

### Delete an Issue
```bash
curl -X DELETE "http://localhost:8000/issues/1"
```

## 🧪 Testing the API

1. Start the server: `uvicorn main:app --reload`
2. Open http://localhost:8000/docs in your browser
3. Use the interactive Swagger UI to test endpoints
4. Or use tools like Postman, Insomnia, or curl commands

## 📊 Database

- **Type**: SQLite (file-based)
- **File**: `bugtracker.db` (auto-created)
- **Tables**: `issues`
- **ORM**: SQLAlchemy with declarative base

## 🔒 Validation

- **Priority**: Must be one of: "Low", "Medium", "High"
- **Status**: Must be one of: "Open", "In Progress", "Closed"
- **Title**: Required, 1-255 characters
- **Description**: Optional, max 5000 characters

## 🚨 Error Handling

- **400 Bad Request**: Invalid input data
- **404 Not Found**: Issue not found
- **500 Internal Server Error**: Server/database errors

## 🛠️ Development

### Adding New Features
1. Update models in `models.py`
2. Add validation schemas in `schemas.py`
3. Implement CRUD operations in `crud.py`
4. Add API routes in `main.py`

### Database Migrations
The app automatically creates tables on startup. For schema changes:
1. Update the model in `models.py`
2. Restart the application (tables will be recreated in development)

## 📝 Notes

- This is a development setup with `--reload` for auto-restart
- SQLite is used for simplicity - consider PostgreSQL/MySQL for production
- The database file `bugtracker.db` is created automatically
- All endpoints include proper error handling and validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.