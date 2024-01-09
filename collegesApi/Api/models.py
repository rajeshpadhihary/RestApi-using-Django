from django.db import models

# Create your models here.
class CollegeModel(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100,choices = (
        ('GOVT','GOVT'),('PRIVATE','PRIVATE')))
    college_for = models.CharField(max_length=100,choices = (
        ('Science','Science'),('Commerce','Commerce'),('Arts','Arts'),('Engineering','Engineering'),
        ('MBA','MBA'),('B.E.D','B.E.D')))
    city = models.CharField(null=True,blank=True,max_length = 50)
    state = models.CharField(null=True,blank=True,max_length = 50)

    def __str__(self):
        return self.name + "--->" + self.city
    
class StudentModel(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=(("MALE", "MALE"), ("FEMALE","FEMALE"),("OTHERS", "OTHERS")))
    dateOfBirth = models.DateField()
    address = models.TextField()
    contactNo = models.BigIntegerField()
    emailId = models.EmailField(unique = True,max_length = 50)
    college = models.ForeignKey(CollegeModel,on_delete=models.CASCADE)
                                                      
