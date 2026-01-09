
# 🚀 ORBIT — Full-Stack AI Chatbot Platform

ORBIT is a **full-stack AI chatbot system** designed with a clean separation of concerns between **backend (Python)** and **frontend (React + Vite)**.

This documentation is written to ensure that **any developer** can:
- Recreate the **exact same environment**
- Understand **why each file and folder exists**
- Understand **what each major function/module does**
- Confidently extend, debug, or deploy the project

---

## 📌 Table of Contents

1. [Project Philosophy](#project-philosophy)
2. [System Architecture](#system-architecture)
3. [Tech Stack](#tech-stack)
4. [Project Structure Explained](#project-structure-explained)
5. [Environment Setup (Step-by-Step)](#environment-setup-step-by-step)
6. [Backend Deep Dive](#backend-deep-dive)
7. [Frontend Deep Dive](#frontend-deep-dive)
8. [Frontend–Backend Communication](#frontendbackend-communication)
9. [Environment Variables Explained](#environment-variables-explained)
10. [Common Pitfalls & Fixes](#common-pitfalls--fixes)
11. [Development Rules & Best Practices](#development-rules--best-practices)
12. [How to Extend the Project](#how-to-extend-the-project)

---

## 🧠 Project Philosophy

ORBIT follows these core principles:

- **Single Responsibility**  
  Every folder, file, and function has one clear purpose.
- **Separation of Concerns**  
  UI logic never lives in backend, business logic never lives in frontend.
- **Environment Reproducibility**  
  Any developer should get identical behavior on any machine.
- **Scalability First**  
  Code structure supports growth without refactoring chaos.

---

## 🏗️ System Architecture





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
- FastAPI / Flask-style architecture
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

---

## 🗂️ Project Structure



## 🧠 Backend: Virtual Environment & Environment Variables

This project uses a Python virtual environment (`venv`) to manage backend dependencies and a `.env` file to store environment variables.

---

### 📦 Create Python Virtual Environment

Run the following commands **from the project root**:

```bash
cd backend
python -m venv .venv



## 🎨 Frontend Setup & Commands

This section explains how to set up, run, and manage the frontend application locally.

---

### 📁 Navigate to Frontend Directory

From the project root:

## 🎨 Frontend Setup & Commands

This section explains how to set up, run, and manage the frontend application locally.  
Follow these steps **after cloning the repository**.

---

### 📁 Navigate to Frontend Directory

From the project root:

```bash
cd frontend


npm install


npm run dev
