# Task Manager API

[English](#english) | [中文](#中文)

---

## English

### Overview
Task Manager API is a backend project built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.  
It supports user registration, login, and full CRUD operations for tasks.

### Features
- User authentication (register, login) with JWT
- Task CRUD:
  - Create task with `title`, `category`, `status`, `due_date`
  - Read single task or task list
  - Update task (partial updates supported)
  - Delete task with ownership validation
- Extended task fields:
  - `category` (default: `life`)
  - `status` (`todo` / `doing` / `done`)
  - `due_date` (optional)

### Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) - modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database models
- [Pydantic](https://docs.pydantic.dev/) - schema validation
- [Passlib](https://passlib.readthedocs.io/) - password hashing
- [Python-JOSE](https://python-jose.readthedocs.io/) - JWT authentication
- SQLite (default, easy to run locally)

### Quick Start
```bash
# 1. Clone repo
git clone https://github.com/<your-username>/task-manager.git
cd task-manager

# 2. Setup virtual environment
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server
uvicorn app.main:app --reload

# 5. Open API docs
http://127.0.0.1:8000/docs
```

### API Endpoints

*   `POST /auth/register` → Register new user
    
*   `POST /auth/login` → Login and get JWT
    
*   `GET /tasks/` → List user’s tasks
    
*   `GET /tasks/{id}` → Get single task
    
*   `POST /tasks/` → Create task
    
*   `PATCH /tasks/{id}` → Update task (partial)
    
*   `DELETE /tasks/{id}` → Delete task


## 中文

### 簡介

Task Manager API 是一個基於 **FastAPI**、**SQLAlchemy** 與 **JWT 認證** 的後端專案。  
它支援使用者註冊、登入，以及任務的完整 CRUD 操作。

### 功能特色

*   使用者驗證：註冊、登入（JWT 驗證）
    
*   任務 CRUD：
    
    *   建立任務（含 `title`、`category`、`status`、`due_date`）
        
    *   查詢單筆或多筆任務
        
    *   更新任務（支援部分更新）
        
    *   刪除任務（限任務擁有者）
        
*   擴充任務屬性：
    
    *   `category`（預設：`life`）
        
    *   `status`（`todo` / `doing` / `done`）
        
    *   `due_date`（可選）
        
### 技術棧

*   FastAPI - 現代化 Python Web 框架
    
*   SQLAlchemy - ORM 資料庫模型
    
*   Pydantic - 資料驗證
    
*   Passlib - 密碼雜湊
    
*   Python-JOSE - JWT 認證
    
*   SQLite（預設，方便本地測試）
    

### 快速開始
```bash
# 1. 複製專案
git clone https://github.com/<your-username>/task-manager.git
cd task-manager

# 2. 建立虛擬環境
python -m venv .venv
source .venv/bin/activate   # Windows 用 .venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 啟動伺服器
uvicorn app.main:app --reload

# 5. 開啟 API 文件
http://127.0.0.1:8000/docs
```

### API 端點

*   `POST /auth/register` → 使用者註冊
    
*   `POST /auth/login` → 使用者登入並取得 JWT
    
*   `GET /tasks/` → 查詢使用者任務
    
*   `GET /tasks/{id}` → 查詢單一任務
    
*   `POST /tasks/` → 建立任務
    
*   `PATCH /tasks/{id}` → 更新任務（部分欄位）
    
*   `DELETE /tasks/{id}` → 刪除任務