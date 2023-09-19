from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)

class Meta:
    db_table = 'contact_details'