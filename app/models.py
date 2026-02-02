from django.db import models
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    RegexValidator,
                                    EmailValidator,
                                    MinLengthValidator,
                                    MaxLengthValidator,
                                    )
from django.core.exceptions import ValidationError



# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(validators=[MinValueValidator(18)])
    city=models.CharField(max_length=10)

    def _str_(self):
        return (self.name,self.city)