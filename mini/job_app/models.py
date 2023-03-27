
from django.db import models
from django.contrib.auth.models import User

JOB = (
    ("TCS", "TCS"),
    ("IBM", "IBM"),
    ("Wipro", "Wipro"),
    ("Facebook", "Facebook"),
    ("Microsoft", "Microsoft"),
    ("Google", "Google"),
    ("Tesla", "Tesla"),
    ("Honda", "Honda"),
)
Qual = (
    ("Master", "Master"),
    ("Btech", "Btech"),
    ("Degree", "Degree"),
    ("Diploma", "Diploma"),
    ("Other", "Other"),
)


# Create your models here.
class application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ImageField(upload_to='image/', max_length=100, blank=True)
    name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=200, blank=True)
    college = models.CharField(max_length=200, blank=True)
    qualification = models.CharField(max_length=200, blank=True, choices=Qual, default='qualification')
    company = models.CharField(max_length=200, blank=True, choices=JOB, default='company')
    skill = models.TextField(max_length=200, blank=True)
    resume = models.FileField(upload_to='resume/', max_length=200, blank=True)

    def __str__(self):
        return self.name
