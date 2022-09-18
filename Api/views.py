# from msilib.schema import ServiceInstall
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobAdvert, JobApplication
from .serializers import JobAdvertSerializer, JobApplicationSerializer, PublishSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAdminOrReadOnly, IsUser, IsAuthenticated
from rest_framework.permissions import IsAuthenticated, AllowAny


class JobAdvertView(APIView):
    '''RETRIEVE DELETE AND UPDATE THE JOB ADVERT INSTANCE'''

    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None):
        obj=JobAdvert.objects.all()
        serializer = JobAdvertSerializer(obj, many=True)
        
        data= {
            "message": 'success',
            "data_count": obj.count(),
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)



    @swagger_auto_schema(method="post", request_body=JobAdvertSerializer())
    @action(methods=["POST"], detail= True)
    def post(self, request,format=None):

        """THIS METHOD IS USED TO CREATE A NEW JOB ADVERT INSTANCE"""

        serializer = JobAdvertSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()

            data={
                "message": "Success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:

            data={
                "message": "failed",
                "error": serializer.errors,

            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class JobAdvertDetailView(APIView):
    """THIS RETRIVE UPDATE AND DELETE JOB ADVERT INSTANCES"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, job_id):
        """PROVIDES A SINGLE ADVERT INSTANCE"""

        try:
            return JobAdvert.objects.get(id=job_id)
        except JobAdvert.DoesNotExist:
            raise NotFound(detail= {
                "message": "Job advert does not exist"
            })

    def get(self, request, job_id, format=None):
        objs = self.get_object(job_id) 
        serializer= JobAdvertSerializer(objs)

        data= {
            "message": "success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="put",request_body=JobAdvertSerializer())
    @action(methods=["PUT"], detail= True)
    def put(self, request, job_id, format=None):
        obj= self.get_object(job_id)
        serializer= JobAdvertSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            data={
                "message": "Success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data={
                "message": "failed",
                "error": serializer.errors
            }
            return Response(data,status=status.HTTP_400_BAD_REQUEST)



    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail= True)
    def delete(self, request, job_id, format=None):
        obj = self.get_object(job_id)
        if obj.job.count()==0 and obj =="Unpublish":

            obj.delete()
            return Response(status=status.HTTP_200_OK)
        raise PermissionDenied(detail={
            "message": "Cannot delete this advert "
        })


        
class JobApplication(APIView):
    """THIS RETRIVE'S DELETE AND UPDATE JOB APPLICATION INSTANCES"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        objs= JobApplication.objects.all()
        serializer= JobApplicationSerializer(objs, many=True)

        data={
            "message": "success",
            "data-count": objs.count(),
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="post", request_body=JobApplicationSerializer())
    @action(methods=["POST"], detail= True)
    def post(self, request, format=None):
        serializer= JobApplicationSerializer(data=request.data)

        if serializer.is_valid() :
            serializer.save()
            data={
                "message": "success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data={
                "message": "failed",
                "error": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class JobApplicationDetailView(APIView):
    """THIS RETRIVES, UPDATE AND DELETE JOB APPLICATION INSTANCE"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, job_id):
        try:
            return JobAdvert.objects.get(id=job_id)
        except JobAdvert.DoesNotExist:
            raise NotFound(detail={
                "message": "Job does not exist",
            })
    
    def get(self,request,job_id, format=None):
        obj= self.get_object(job_id)
        add= obj.job.all()
        serializer= JobApplicationSerializer(add, many=True)

        data={
            "message": "success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=JobApplicationSerializer())
    @action(methods=["PUT"], detail= True)
    def put(self,request, job_id, format=None):
        obj= self.get_object(job_id)
        serializer= JobAdvertSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid() and data=='published':
            serializer.save()

            data={
                "message": "Success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data={
                "message": "failed",
                "error": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail= True)
    def delete(self, job_id, format=None):
        obj=  self.get_object(job_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Unpublish(APIView):
    """THIS PUBLISHES A JOB APPLICATION"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, job_id):
        try:
            return JobAdvert.objects.get(id=job_id)
        except JobAdvert.DoesNotExist:
            raise NotFound(detail={
                "message": "Job does not exist"
            })

    @swagger_auto_schema(method="put", request_body=PublishSerializer())
    @action(methods=["PUT"], detail= True)
    def put(self, request, job_id, format=None):
        obj= self.get_object(job_id)
        serializer= PublishSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()

            data={
                "message": "Successfull changed"
            
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data={
                "message": "failed",
                "error": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)





