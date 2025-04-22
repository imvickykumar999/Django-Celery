# 🚀 Running the Project (Django + Celery + Redis)

![image](https://github.com/user-attachments/assets/9e95b35c-2507-4095-890e-020b1087b60d)

This project uses **Celery** for background task processing and **django-celery-beat** for periodic task scheduling. Below are the steps and commands to get everything running for local development.

---

## 📦 Install Redis (Ubuntu / Codespaces / Dev Containers)

If Redis is not already installed on your system:

```bash
sudo apt update
sudo apt install redis-server -y
```

### ✅ Start Redis Manually

Since `systemd` may not be available (e.g., in a Codespace), start Redis manually:

```bash
redis-server &
```

### 🔎 Test Redis is Working

```bash
redis-cli ping
# Expected output: PONG
```

> If `redis-cli` is missing:
```bash
sudo apt install redis-tools
```

---

## 🔧 1. Start Django Development Server

This runs your web application on `localhost`.

```bash
python3 manage.py runserver
```

> This command starts the Django application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
> Use it to access the Django admin panel and trigger/view task results.

---

## 🧵 2. Start Celery Worker

This runs the Celery worker, which listens for tasks and executes them in the background.

```bash
celery -A myproject worker --loglevel=info
```

- `-A myproject` refers to the project directory containing `celery.py`.
- `--loglevel=info` shows task processing logs in the terminal.

> ✅ Make sure Redis is running before starting the worker.

---

## ⏰ 3. Start Celery Beat Scheduler

This runs the beat service, which schedules and dispatches periodic tasks.

```bash
celery -A myproject beat --loglevel=info
```

- This should run in a separate terminal.
- Beat uses the database schedule from the `django-celery-beat` app.

> You can define and manage periodic tasks directly from the Django admin under **"Periodic Tasks"**.

---

## ✅ Summary

| Service        | Command                                       | Description                              |
|----------------|-----------------------------------------------|------------------------------------------|
| Redis Server   | `redis-server &`                              | Starts Redis manually in foreground      |
| Django Server  | `python3 manage.py runserver`                 | Web server and admin access              |
| Celery Worker  | `celery -A myproject worker --loglevel=info` | Executes background tasks                |
| Celery Beat    | `celery -A myproject beat --loglevel=info`   | Schedules and dispatches periodic tasks  |

---
