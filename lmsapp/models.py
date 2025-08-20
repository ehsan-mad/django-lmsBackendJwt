from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}-{self.phone}"
    

class Teacher(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    is_active= models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)
    roll_number = models.CharField(max_length=100, null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Course(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.title}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
   

    def __str__(self):
        return f"{self.title} - {self.course.title}"
    
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date= models.DateField()

    def __str__(self):
        return f"{self.title} - {self.course.title}"
    
class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_at = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"