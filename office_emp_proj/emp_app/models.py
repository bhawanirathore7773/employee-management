from django.db import models

# Create your models here.


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


class Role(models.Model):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s"%(self.first_name,self.last_name,self.number)

