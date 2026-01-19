# AI Coding Agent Instructions for `myportfolio` Django Project

Welcome to the `myportfolio` Django project! This document provides essential guidelines for AI coding agents to be productive in this codebase. It outlines the architecture, workflows, conventions, and integration points specific to this project.

---

## Project Overview

This is a Django-based portfolio project with the following structure:

- **`myportfolio/`**: The main Django project directory containing settings, URLs, and WSGI/ASGI configurations.
- **`portfolio/`**: A Django app for managing portfolio-related functionality (e.g., models, views, and admin configurations).
- **`migrations/`**: Tracks database schema changes for the `portfolio` app.

### Key Files:
- `myportfolio/settings.py`: Centralized configuration for the Django project.
- `myportfolio/urls.py`: Root URL routing.
- `portfolio/models.py`: Defines database models.
- `portfolio/views.py`: Handles HTTP request logic.
- `portfolio/admin.py`: Admin interface customizations.

---

## Developer Workflows

### Running the Development Server
To start the development server, navigate to the `myportfolio` directory and run:
```bash
python manage.py runserver
```

### Creating and Applying Migrations
To create migrations for database changes:
```bash
python manage.py makemigrations
```

To apply migrations:
```bash
python manage.py migrate
```

### Running Tests
To execute tests for the `portfolio` app:
```bash
python manage.py test portfolio
```

### Debugging
Use Django's built-in debugging tools. Ensure `DEBUG = True` in `settings.py` during development.

---

## Project-Specific Conventions

### URL Patterns
- All URLs are defined in `urls.py` files.
- Use `path()` or `re_path()` for routing.

### Models
- Define all database models in `portfolio/models.py`.
- Use Django's ORM for database interactions.

### Views
- Use function-based views (FBVs) in `portfolio/views.py`.
- Follow Django's request-response cycle.

### Admin Customization
- Register models in `portfolio/admin.py`.
- Use `@admin.register` decorator for cleaner registration.

---

## Integration Points

### Database
- Default database: SQLite (configured in `settings.py`).
- Update `DATABASES` in `settings.py` for production environments.

### Static and Media Files
- Static files: Configure `STATIC_URL` and `STATICFILES_DIRS` in `settings.py`.
- Media files: Configure `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`.

### External Dependencies
- Install dependencies using `pip install -r requirements.txt`.
- Add new dependencies to `requirements.txt`.

---

## Examples

### Adding a New Model
1. Define the model in `portfolio/models.py`:
    ```python
    from django.db import models

    class Project(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
    ```
2. Create and apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
3. Register the model in `portfolio/admin.py`:
    ```python
    from django.contrib import admin
    from .models import Project

    @admin.register(Project)
    class ProjectAdmin(admin.ModelAdmin):
        list_display = ('title', 'created_at')
    ```

### Adding a New View
1. Define the view in `portfolio/views.py`:
    ```python
    from django.shortcuts import render

    def home(request):
        return render(request, 'portfolio/home.html')
    ```
2. Add the URL pattern in `myportfolio/urls.py`:
    ```python
    from django.urls import path
    from portfolio import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]
    ```
3. Create the template `portfolio/templates/portfolio/home.html`.

---

## Notes for AI Agents
- Follow Django's MVC (Model-View-Controller) pattern.
- Ensure code adheres to Django's conventions and best practices.
- Validate changes by running tests and checking for errors.
- Avoid modifying `settings.py` unless explicitly instructed.

---

For further clarification, refer to the [Django documentation](https://docs.djangoproject.com/).