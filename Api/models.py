from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


class JobAdvert(models.Model):
    FULLTIME= 'Full-time'
    CONTRACT= 'Contact'
    REMOTE= 'Remote'
    PART_TIME= 'Part-time'

    EMPLOYMENT_TYPE = (
        (FULLTIME, 'Full-Time'),
        (CONTRACT, 'Contract'),
        (REMOTE, 'Remote'),
        (PART_TIME, 'Part-Time'),
    )

    EMPLOYMENT_LEVEL= (
        ('ENTRY-LEVEL', 'Entry-Level'),
        ('MID-LEVEL', 'Mid-Level'),
        ('SENIOR', 'Senior'),
    )

    STATUS_CHOICES = (
        ('unpublished', 'Unpublished'),
        ('published', 'Published')
    )


    Title= models.CharField(max_length=255)
    Company_Name=models.CharField(max_length=255)
    Employment_type= models.CharField(max_length=20, choices=EMPLOYMENT_TYPE, default='Remote')
    Experience_level= models.CharField(max_length=20, choices=EMPLOYMENT_LEVEL, blank=True)
    Desc= models.TextField()
    location= models.CharField(max_length=100, blank=True)
    job_desc= models.TextField()
    Publish_status = models.CharField(max_length=20,choices=STATUS_CHOICES,
                                blank=True)
    publish = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.Title + ' | ' + str(self.Company_Name)
    @property
    def job_list_count(self):
        return self.Job.all().values().count()


    class Meta:
        ordering = ('-Publish_status',)

class JobApplication(models.Model):

    top_1= '0-1'
    top_2= '1-2' 
    top_3= '3-4'
    top_4= '5-6'
    top_5= '7-Above'

    YEARS_OF_EXPERIENCE= (
    (top_1,'0-1'),
    (top_2,'1-2'), 
    (top_3,'3-4'),
    (top_4,'5-6'),
    (top_5,'7-Above') 
    )

    job_Advert= models.ForeignKey(JobAdvert,related_name='Job', on_delete= models.CASCADE )
    first_name= models.CharField(max_length=40)
    Last_name= models.CharField(max_length=40)
    Phone= PhoneNumberField(blank=True)
    Image= models.ImageField(blank=True, null=True)
    Linkedin_profile= models.URLField(max_length=100, db_index=True, unique=True) 
    Github_profile= models.URLField(max_length=100, db_index=True, unique=True)
    Website= models.URLField(max_length=100, default='optional', null=True)
    Years_of_experience= models.CharField(max_length=100, choices=YEARS_OF_EXPERIENCE, blank=True) 
    Cover_letter= models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    


    def __str__(self):
        return self.Last_name + " | " + self.first_name

    @property
    def job_name(self):
        return model_to_dict(self.job_Advert, fields=['Title'])

    class Meta:
        ordering= ('-date_added',)


    