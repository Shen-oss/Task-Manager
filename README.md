# Task Manager API

一個使用 **FastAPI + SQLAlchemy** 開發的任務管理系統 API。  
支援 **使用者註冊/登入 (JWT)** 與 **任務 CRUD** 功能。  

## 技術棧
- FastAPI
- SQLAlchemy
- JWT (python-jose)
- Passlib (密碼雜湊)
- SQLite (可切換 MySQL)

## 功能
- 使用者註冊 / 登入
- JWT 驗證
- 建立 / 查詢 / 更新 / 刪除任務

## 快速開始
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload