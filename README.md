
---

# 🧠 Smart Task Scheduler for Asynchronous File Processing

**Python | Flask | Celery | Redis | HTML | CSS**

---

## 📌 Project Overview

The **Smart Task Scheduler** is a web-based application that allows users to **upload files and process them asynchronously** using **Celery workers and Redis**.

Instead of blocking the main application, file processing tasks run in the background, ensuring **better performance, scalability, and responsiveness**.

This project demonstrates **real-world asynchronous task handling** using modern Python web technologies.

---

## 🚀 Features

* 📂 File upload via web interface
* ⚙️ Asynchronous background processing using **Celery**
* 🧠 Task queue management with **Redis**
* 🌐 Lightweight web UI using **HTML & CSS**
* 🔄 Non-blocking execution for better user experience

---

## 🧠 Architecture Overview

```
User → Flask Web App → Celery Task Queue → Redis Broker → Worker
```

* **Flask** handles HTTP requests and file uploads
* **Celery** executes long-running tasks asynchronously
* **Redis** acts as message broker and task queue
* **HTML/CSS** provides the frontend interface

---

## 🗂️ Project Structure

```
├── app.py            # Flask application (file upload & routing)
├── task.py           # Celery task for background file processing
├── requirements.txt  # Project dependencies
├── index.html        # Frontend HTML page
├── style.css         # Styling for frontend
└── README.md         # Project documentation
```

---

## ⚙️ Technologies Used

* **Python**
* **Flask**
* **Celery**
* **Redis**
* **HTML**
* **CSS**

---

## ✅ How It Works

1. User uploads a file via the web interface
2. Flask receives the file and sends a task to Celery
3. Celery places the task in Redis queue
4. Background worker processes the file asynchronously
5. User is free to continue without waiting

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start Redis Server

```bash
redis-server
```

### 3️⃣ Start Celery Worker

```bash
celery -A task worker --loglevel=info
```

### 4️⃣ Run Flask App

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🎯 Key Concepts Demonstrated

* Asynchronous task execution
* Background job scheduling
* Flask–Celery integration
* Redis as message broker
* Scalable web application design

---
