# 🚀 AI Interview Proctoring & Evaluation System

### **Database Integration Layer**
This repository features a robust **Python-based database integration** for an automated interview proctoring system. It bridges the gap between raw **PostgreSQL** data and application logic, specifically designed to monitor candidate behavior and evaluate interview performance using AI.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **ORM:** SQLAlchemy (Object Relational Mapper)
* **Database:** PostgreSQL
* **Drivers:** Psycopg2-binary

---

## 📊 Database Schema
The project maps the following entities as defined in the PostgreSQL structure:

| Table | Purpose |
| :--- | :--- |
| **`users`** | Manages candidate profiles and authentication data. |
| **`interview_sessions`** | Central hub tracking status, timing, and cumulative risk scores. |
| **`object_detection_events`** | Logs AI-detected items (e.g., cell phones) with confidence levels. |
| **`face_pose_events`** | Tracks suspicious physical behavior and severity levels. |
| **`audio_transcripts`** | Stores text content and timestamps for candidate responses. |
| **`answer_evaluations`** | Links answers to AI-generated relevance scores and feedback. |

[Image of entity relationship diagram for an interview proctoring system database]

---

## 🚀 Getting Started

### **1. Prerequisites**
Ensure you have Python installed and a running PostgreSQL instance.

### **2. Installation**
```bash
pip install -r requirements.txt
