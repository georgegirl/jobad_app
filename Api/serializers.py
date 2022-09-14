from rest_framework import serializers
from.models import JobAdvert, JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    job_name= serializers.ReadOnlyField()

    class Meta:
        model= JobApplication
        fields= '__all__'


class JobAdvertSerializer(serializers.ModelSerializer):
    job_list_count = serializers.ReadOnlyField()

    class Meta:
        model = JobAdvert
        fields= '__all__'

class PublishSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobAdvert
        fields = ['Publish_status']