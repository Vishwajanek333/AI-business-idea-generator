# 🧠 AI Business Idea Generator

A professional **SaaS application** that generates creative business startup ideas using AI — built with **React (Frontend)** and **FastAPI (Backend)**.

![Architecture Diagram](./ad027f23-b04d-4dd8-8b58-d480aea4e0e7.png)

---

## 🗂️ Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Project Summary for Resume](#project-summary-for-resume)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🚀 Features

### Core Features
- **User Authentication** – Secure sign-up and login with JWT
- **AI-Powered Idea Generation** – Generate business ideas using keywords and industries
- **Business Plan Details** – Each idea includes title, model, audience, SWOT, and potential
- **Idea Management** – Save, favorite, and organize ideas
- **Search History** – Track all previous idea generation sessions
- **Analytics Dashboard** – View user-specific and platform-wide analytics
- **PDF Export** – Export business ideas as professional PDFs
- **Beautiful UI** – Clean blue-white theme with responsive layout

### Business Focus Areas
- **Finance** – FinTech and investment startups  
- **Education** – EdTech and learning innovation  
- **Social** – Community and social impact businesses  

---

## 🧰 Tech Stack

### Frontend
- **React 18**
- **Tailwind CSS**
- **Lucide React**
- **Axios**
- **React Router**

### Backend
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**
- **Python-Jose**
- **Passlib**

### Additional Tools
- **Uvicorn**
- **ReportLab**
- **python-dotenv**

---

## 🏗️ Project Structure



ai-business-idea-generator/
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.js
│ │ ├── index.js
│ │ └── index.css
│ ├── package.json
│ └── README.md
│
├── backend/
│ ├── app/
│ │ ├── api/
│ │ │ ├── auth.py
│ │ │ ├── ideas.py
│ │ │ ├── pdf.py
│ │ │ └── analytics.py
│ │ ├── core/config.py
│ │ ├── db/database.py
│ │ ├── models/models.py
│ │ ├── schemas/schemas.py
│ │ ├── services/
│ │ │ ├── auth_service.py
│ │ │ ├── ai_service.py
│ │ │ ├── pdf_service.py
│ │ │ └── db_service.py
│ │ ├── main.py
│ │ └── init.py
│ ├── run.py
│ ├── requirements.txt
│ └── .env
│
├── .env
├── .gitignore
└── README.md


---

## ⚙️ Prerequisites

### System Requirements
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+
- Git

### Tools
- Command Prompt / PowerShell
- VS Code
- Postman (optional)

---

## 🔧 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/ai-business-idea-generator.git
cd ai-business-idea-generator

Step 2: Setup Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Create .env

DATABASE_URL=postgresql://ai_admin:admin123@localhost:5432/ai_idea_generator
OPENAI_API_KEY=sk-proj-your-key
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

Step 3: Setup Frontend
cd ../frontend
npm install


Create .env

REACT_APP_API_URL=http://localhost:8000

▶️ Running the Application
Run Backend
cd backend
venv\Scripts\activate
python run.py

Run Frontend
cd frontend
npm start

Access

Frontend → http://localhost:3000

Backend → http://localhost:8000

API Docs → http://localhost:8000/docs

📘 API Documentation
Authentication

Register

POST /api/v1/auth/register


Login

POST /api/v1/auth/login

Idea Generation

Generate

POST /api/v1/ideas/generate

PDF Export

Single

GET /api/v1/pdf/export/{idea_id}


Multiple

POST /api/v1/pdf/export-multiple

Analytics

User

GET /api/v1/analytics/user


Platform

GET /api/v1/analytics/platform

🚢 Deployment
🐳 Docker Setup

backend/Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]


frontend/Dockerfile

FROM node:16-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


docker-compose.yml

version: '3.8'
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: ai_admin
      POSTGRES_PASSWORD: admin123
      POSTGRES_DB: ai_idea_generator
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://ai_admin:admin123@db:5432/ai_idea_generator
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - backend


Run:

docker-compose up -d

🧑‍💻 Project Summary for Resume
Title

AI Business Idea Generator – Full Stack SaaS App

Description

A full-stack SaaS platform that leverages AI to generate innovative business startup ideas and export them as professional PDF business plans.

Responsibilities

Developed RESTful API with FastAPI

Designed responsive frontend with React + Tailwind

Integrated JWT authentication

Implemented PostgreSQL with SQLAlchemy ORM

Created PDF export using ReportLab

Built analytics dashboard and tracking

Containerized app using Docker

Tech Used

Frontend: React, Tailwind CSS
Backend: FastAPI, PostgreSQL
Auth: JWT, bcrypt
DevOps: Docker, Git

Impact

Showcases full-stack expertise

Implements secure, scalable architecture

Demonstrates practical AI integration

🤝 Contributing

Fork this repo

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

Licensed under the MIT License. See LICENSE file for details.
