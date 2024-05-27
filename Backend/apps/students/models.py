from django.db import models

# Create your models here.

class Branches(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.branch_name
    


class Departments(models.Model):
    department_name = models.CharField(max_length=30)
    department_branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    department_head = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name



class StudentList(models.Model):
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Fmale', 'female'),
        ('Other', 'other')
    )
    stud_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.stud_name

