from django.urls import path
from . import views


urlpatterns = [
    path('ADVERT/', views.JobAdvertView.as_view(), name='jobadvert'),
    path('ADVERT/<int:job_id>', views.JobAdvertDetailView.as_view(), name='advert'),
    path('APPLICATION/', views.JobApplication.as_view(), name='application'),
    path('APPLICATION/<int:job_id>', views.JobApplicationDetailView.as_view(), name='application'),
    path('Update/<int:job_id>', views.Unpublish.as_view(), name='unpublish'),
    # path('PUBLISH/<int:job_id>', views.Publish.as_view(), name='unpublish'),
  
]


