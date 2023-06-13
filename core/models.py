from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Unique_Login(models.Model):
    login=models.CharField(max_length=10)
    
    

class IQ_Test(models.Model):
    score=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(50)])
    login_f=models.ForeignKey(Unique_Login, on_delete=models.CASCADE, unique=True)
    date_passed=models.DateTimeField(auto_now=True)
    
class EQ_Test(models.Model):
    result=models.CharField(max_length=5)
    login_f=models.ForeignKey(Unique_Login, on_delete=models.CASCADE, unique=True)
    date_passed=models.DateTimeField(auto_now=True)
    