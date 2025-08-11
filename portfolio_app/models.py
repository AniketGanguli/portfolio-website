# portfolio_app/models.py
from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('excel', 'Excel'),
        ('powerbi', 'Power BI'),
        ('salesforce', 'Salesforce'),
        ('django', 'Django'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='excel')
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(max_length=200)
    overview_pdf = models.FileField(upload_to='project_pdfs/')
    
    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

