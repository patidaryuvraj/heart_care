from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class appoint(models.Model):
    doctor = (
              ('dr.chabra','Dr. Rohit chabra'),
              ('dr.Shahid', 'Dr. Abbas Shahid'),
              ('dr.Malik','Dr. Abdul Malik'),
              ('dr.Dilip','Dr. Achraya Dilip'),
              ('dr.Dinesh','Dr. Achraya Dinesh'),
              ('dr.Neelima','Dr. Admane Neelima'),
              ('dr.Sanjay','Dr. Dhanuka Sanjay'),
              ('dr.Hemlata','Dr. Dhand Hemlata'),
    )
    time=(
          ('morning','MORNING'),
          ('evening','EVENING'),

    )
    name = models.CharField(max_length=50,verbose_name="Your Name ")
    mobile = models.CharField(max_length=15,verbose_name="Your Mobile ")
    email = models.EmailField(max_length=75,verbose_name="Your Email ")
    doctor = models.CharField(max_length=50, choices=doctor, default='doctor')
    date=models.DateTimeField()
    time=models.CharField(max_length=50,choices=time,default='time')
    
class Meta:
    db_table = 'appoint data'
    