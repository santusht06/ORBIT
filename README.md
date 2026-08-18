# 🚀 ORBIT — Full Stack AI Chatbot

ORBIT is a full-stack AI chatbot application built with a **Python backend** and a **React (Vite) frontend**.  
The project is structured for clarity, scalability, and ease of contribution.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Backend Documentation](#backend-documentation)
- [Frontend Documentation](#frontend-documentation)
- [Connecting Frontend & Backend](#connecting-frontend--backend)
- [Common Errors & Fixes](#common-errors--fixes)
- [Best Practices](#best-practices)
- [Deployment Notes](#deployment-notes)
- [Contributing](#contributing)

---

## 📖 Project Overview

ORBIT is an AI-powered chatbot platform consisting of:

- **Backend (Python)**  
  Handles APIs, AI logic, data processing, and responses.
- **Frontend (React + Vite)**  
  Provides the user interface and communicates with the backend.

The frontend and backend are kept **fully separate** for clean architecture and easier maintenance.

---

## 🧰 Tech Stack

### Backend
- Python 3.10+
- FastAPI / Flask‑style architecture
- REST APIs
- Virtual Environment (`.venv`)

### Frontend
- React
- Vite
- JavaScript (ES6+)
- CSS / Tailwind (optional)

### Tooling
- Git & GitHub
- Node.js (v18+ recommended)
- npm
- Docker

---

## 🗂️ Project Structure

The project is structured as follows:
```markdown
ORBIT/
├── backend/
│   ├── .gitignore
│   ├── .venv
│   ├── Dockerfile
│   ├── index.py
│   ├── models/
│   ├── controllers/
│   ├── routers/
│   ├── utils/
│   ├── lib/
│   └── requirements.txt
├── frontend/
│   ├── .gitignore
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── src/
│   └── README.md
├── .gitignore
├── docker-compose.yml
└── README.md
```

## 🧠 Backend: Virtual Environment & Environment Variables

This project uses a Python virtual environment (`venv`) to manage backend dependencies and a `.env` file to store environment variables.

### 📦 Create Python Virtual Environment

Run the following commands **from the project root**:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
.venv\Scripts\activate  # On Windows
```

### 📦 Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 📄 `.env` File Structure

Create a file named `.env` inside the `backend/` folder (you can copy the provided example):

```bash
cd backend

## 🧠 Core Web Framework & Server

### fastapi
- **Purpose:** Core backend web framework
- **Why it exists:** Handles API creation, routing, request/response handling
- **Used in:** `routers/`, `controllers/`, `index.py`
- **Cannot remove:** ❌ (Backend will not run)

### starlette
- **Purpose:** ASGI toolkit used internally by FastAPI
- **Why it exists:** FastAPI is built on top of Starlette
- **Used in:** Internal request lifecycle
- **Direct usage:** ❌ (Indirect dependency)

### uvicorn
- **Purpose:** ASGI server
- **Why it exists:** Runs the FastAPI application
- **Used in:** Application startup
- **Example usage:**
```bash
uvicorn index:app --reload
```

## 🔐 Backend Environment Variables (`.env`)

The backend relies on environment variables to manage secrets, API keys, and configuration.  
These values are stored in a `.env` file inside the `backend/` directory.

⚠️ **Important**
- Never commit `.env` files to GitHub
- Always use placeholder values in documentation
- Use `.env.example` for reference

---

## 📄 `.env` File Structure

Create a file named `.env` inside the `backend/` folder:

```bash
cd backend
touch .env
```

```makefile
# ================================
# AI / LLM Configuration
# ================================
GROQ_API_KEY=your_groq_api_key_here

# ================================
# Cloudinary (Media Storage)
# ================================
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

# ================================
# Database Configuration
# ================================
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>

# ================================
# Application Settings
# ================================
DEBUG=True
PORT=8000
```

## 🎨 Frontend Setup & Commands

This section explains how to set up, run, and manage the frontend application locally.  
Follow these steps **after cloning the repository**.

### 📁 Navigate to Frontend Directory

From the project root:

```bash
cd frontend
```

### 📦 Install Dependencies

```bash
npm install
```

### 📦 Run Development Server

```bash
npm run dev
```

## 🚀 Installation

To install the project, follow these steps:

1. Clone the repository
2. Navigate to the project root
3. Create a Python virtual environment for the backend
4. Activate the virtual environment
5. Install backend dependencies
6. Create a `.env` file for backend environment variables
7. Navigate to the frontend directory
8. Install frontend dependencies
9. Run the development server

## 🚀 Usage

To use the project, follow these steps:

1. Start the backend server using `uvicorn index:app --reload`
2. Start the frontend development server using `npm run dev`
