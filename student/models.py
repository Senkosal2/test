from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    
    def __self__(self):
        self.name
        self.gender
        self.dob
        
    class Meta:
        db_table = "tb_students"