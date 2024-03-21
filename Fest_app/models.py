from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_School=models.BooleanField(default=False)
    is_Student=models.BooleanField(default=False)
    is_Year=models.BooleanField(default=False)

class School(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='school')
    School_Name=models.CharField(max_length=500)
    School_Register_No=models.CharField(max_length=30)
    Correspondent_Name=models.CharField(max_length=50)
    Principal_Name=models.CharField(max_length=50)
    Place=models.CharField(max_length=20)
    Contact_No=models.CharField(max_length=10)
    approval_status=models.IntegerField(default=0)
    def __str__(self):
      return self.School_Name
    
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='student')
    School_Name=models.ForeignKey(School,on_delete=models.CASCADE) 
    Student_Name=models.CharField(max_length=200)
    DOB=models.DateField()
    Class=models.CharField(max_length=10)
    Contact_No=models.CharField(max_length=10)
    def __str__(self):
      return self.Student_Name
    
class contest(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contest')
   Si_No=models.CharField(max_length=5)
   Contest_Name=models.TextField()
   def __str__(self):
      return self.Contest_Name

class participant(models.Model):  
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='participants')
   Name=models.CharField(max_length=200)
   Class=models.CharField(max_length=20)
   Contest_Name=models.TextField()

class judges(models.Model):  
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='judge')
   Name=models.CharField(max_length=100)
   Contest_Name=models.ForeignKey(contest,on_delete=models.CASCADE) 
   Room_No=models.CharField(max_length=5)

class result(models.Model):   
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='results')
   First=models.CharField(max_length=100)
   Second=models.CharField(max_length=100)
   Contest_Name=models.ForeignKey(contest,on_delete=models.CASCADE) 

class programmes(models.Model):  
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='programme')
   Si_No=models.CharField(max_length=100)
   Programme_Name=models.CharField(max_length=500)
   def __str__(self):
      return self.Programme_Name

class performer(models.Model):   
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='performers')
   Si_No=models.CharField(max_length=5)
   Programme_Name=models.ForeignKey(programmes,on_delete=models.CASCADE)
   Performer_Names=models.CharField(max_length=100)

class venue(models.Model):   
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='venue')
   Venue=models.CharField(max_length=100)
   Place=models.CharField(max_length=100)

class volunteers(models.Model):  
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='vol')
   Name=models.CharField(max_length=100)
   Contact_No=models.CharField(max_length=10)

class guests(models.Model):   
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='guest')
   Name=models.CharField(max_length=100)
   Photoes=models.ImageField(upload_to='guest_images')
   Details=models.CharField(max_length=500)

class gallery(models.Model):    
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='gallery')
   Photoes=models.ImageField(upload_to='gallery_images')
   Videos=models.FileField(upload_to='gallery_videos')

class achievements(models.Model):    
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='achivmnt')
   School_Achievements=models.TextField()
   Photoes=models.ImageField(upload_to='achievements_images')

class management(models.Model):    
   Members=models.CharField(max_length=100)
   Correspondent_Name=models.CharField(max_length=20)
   Contact_No=models.CharField(max_length=10)

class teachers(models.Model):    
   Name=models.CharField(max_length=50)
   Subject=models.CharField(max_length=50)
   Position=models.CharField(max_length=50)
   Contact_No=models.CharField(max_length=50)

class feedbacks(models.Model):   
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='feedback')
   Your_name=models.CharField(max_length=20)
   Your_mobile_no=models.CharField(max_length=10)
   Feedbacks=models.TextField()

class contact(models.Model):   
   Name=models.CharField(max_length=50)
   Email_address=models.EmailField()
   Subject=models.CharField(max_length=50)
   Message=models.CharField(max_length=500)
   def __str__(self):
      return self.Name

class year(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='year',null=True, blank=True)
  Year=models.CharField(max_length=10)
  Program_Name=models.CharField(max_length=100)
   
  def __str__(self):
     return self.Year

class history(models.Model):
   History=models.TextField()

class school_photoes(models.Model):
   photoes=models.ImageField(upload_to='school_photo')

