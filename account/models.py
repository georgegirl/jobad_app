from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Option=(
        ('Male', 'MALE'),
        ('Female', 'FEMALE')
    )
    '''
        Users
    '''
    gender= models.CharField(max_length=50, choices= Option, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'gender']


    










#     is_job_seeker = models.BooleanField(default=False)
#     is_recruiter = models.BooleanField(default=False)
#     is_mentor = models.BooleanField(default=False)

# class Company(models.Model):
#     user = models.ForeignKey(User) # only user with is_recruiter flag active can be

# class JobSeeker(models.Model):
#     user = models.OneToOneField(User)
#     # job seeker profile related fields like experiences, skills, education, profile image etc

# class Recruiter(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, null=True, blank=True)
#     # recruiter related profile 