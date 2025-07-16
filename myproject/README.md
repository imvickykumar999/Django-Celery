## `length_is` is deprecated since 4.2 and removed in Django 5.1

<img width="1316" height="701" alt="image" src="https://github.com/user-attachments/assets/725c032d-a509-4288-a3d0-e5101c3d1454" />

```txt
Django==4.1.*
```

This ensures that only the versions in the 4.1 series of Django will be installed.

If you're also using other packages (like Celery, Redis, and others), here's a sample `requirements.txt` with the necessary versions:

```txt
Django==4.1.*
celery>=5.3,<6.0
redis>=5.0,<6.0
django-celery-beat>=2.5,<3.0
django-celery-results>=2.5,<3.0
gunicorn>=22.0,<23.0
Pillow>=10.0,<11.0
```

You can add or modify other packages as needed for your project.

### Steps:

1. Open your `requirements.txt`.
2. Add `Django==4.1.*`.
3. Save the file.
4. Run the following command to install dependencies:

```bash
pip install -r requirements.txt
```

This will install Django 4.1 and all other dependencies listed in your `requirements.txt`.
