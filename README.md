# 🎓 Intelligent LMS API

A **Learning Management System (LMS)** backend built with **FastAPI**, featuring secure user authentication, course management, and dynamic content handling.

## 🚀 Features

### 🔐 Authentication
- Register, login, and secure JWT-based auth
- Password hashing with `bcrypt` (`passlib`)
- Password reset and token verification

### 👤 User Management
- Read/update own profile
- View enrolled courses
- Protected routes with user authentication

### 📚 Course Management
- Create, publish, and fetch courses
- Admin/superuser access for moderation
- Purchase courses as a user

### 🧾 Content Handling
- Add and retrieve course content
- Authenticated content access only

### ⚙️ Developer Tools
- FastAPI auto-generated docs via Swagger/OpenAPI 3.1
- `.env` based config using `pydantic-settings`
- Health check endpoint: `/health`

---

## 🧠 Tech Stack

| Tool/Library      | Usage                          |
|------------------|---------------------------------|
| **FastAPI**       | Web framework                   |
| **Python 3.12**   | Core language                   |
| **SQLAlchemy**    | ORM for DB interaction          |
| **PostgreSQL**    | Relational database             |
| **python-jose**   | JWT token encoding/decoding     |
| **passlib**       | Password hashing (`bcrypt`)     |
| **Pydantic**      | Request/response validation     |
| **Uvicorn**       | ASGI server                     |

---

## 📁 Project Structure

---

## Architecture: Monolith + Auth Service + API Gateway
- api-gateway (Nginx):
  - Routes /api/v1/auth/* to auth_service
  - Routes everything else (/) to app
- app: existing LMS API without auth endpoints
- auth_service: dedicated FastAPI service for authentication (register/login/password reset)
- db: PostgreSQL shared by both services (simple setup for now)

## How to run (via API Gateway)
1) Ensure Docker is running
2) From the LLM directory:
   ```bash
   docker-compose up -d --build
   ```
3) Access:
   - Gateway base URL: http://localhost:8000/
   - API docs (app): http://localhost:8000/docs
   - Auth docs: http://localhost:8000/api/v1/auth/docs

To stop:
```bash
docker-compose down
```

## Environment
Key variables (in .env or compose):
- DATABASE_URL1: e.g. postgresql+asyncpg://superuser:postgres@db:5432/intelligent_lms
- SECRET_KEY: JWT signing key

Both app and auth_service read DATABASE_URL1, so they share the same database.

## New/updated files
- docker-compose.yml: added auth_service and api-gateway; app no longer publishes port to host
- gateway/nginx.conf: Nginx routing config
- auth_service/main.py: standalone FastAPI app exposing /api/v1/auth
- app/main.py: removed auth router registration
