# 🚀 Running the Project (Django + Celery + Redis)

This project uses **Celery** for background task processing and **django-celery-beat** for periodic task scheduling. Below are the commands to run each service required for local development.

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

> ✅ Make sure Redis is running (`redis-server`) before starting the worker.

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
| Django Server  | `python3 manage.py runserver`                 | Web server and admin access              |
| Celery Worker  | `celery -A myproject worker --loglevel=info` | Executes background tasks                |
| Celery Beat    | `celery -A myproject beat --loglevel=info`   | Schedules and dispatches periodic tasks  |

---
