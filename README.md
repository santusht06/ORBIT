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
cp .env.example .env   # if .env.example exists
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

> **⚠️ Important**  
> - Never commit `.env` files to the repository.  
> - Use placeholder values in documentation.  
> - Keep a `.env.example` file for reference.

## 🎨 Frontend Setup & Commands

This section explains how to set up, run, and manage the frontend application locally.  
Follow these steps **after cloning the repository**.

### 📁 Navigate to Frontend Directory

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

1. **Clone the repository**  
   ```bash
   git clone <repository_url>
   cd ORBIT
   ```

2. **Backend**  
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   cp .env.example .env   # customize the values
   ```

3. **Frontend**  
   ```bash
   cd ../frontend
   npm install
   ```

4. **Optional: Docker**  
   If you prefer containerised setup, ensure Docker is installed and run:  
   ```bash
   cd ..
   docker-compose up --build
   ```

## 🚀 Usage

### Local Development

- **Start the backend server**  
  ```bash
  cd backend
  uvicorn index:app --reload
  ```

- **Start the frontend development server**  
  ```bash
  cd ../frontend
  npm run dev
  ```

- Open a web browser and navigate to `http://localhost:3000`.

### Docker Compose

```bash
docker-compose up --build
```

- Backend will be available at `http://localhost:8000`.  
- Frontend will be available at `http://localhost:3000`.

---