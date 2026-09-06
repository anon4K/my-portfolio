from django.db import models

# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('software', 'Software'),
        ('hardware', 'Hardware'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='software')
    tech_stack = models.CharField(max_length=200, blank=True, help_text="Comma-separated, e.g 'Django, DRF, PostgreSQL'")
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]