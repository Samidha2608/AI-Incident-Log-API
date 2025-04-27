from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Incident
from .serializers import IncidentSerializer

# here i have created a class which will basically handle
# two things - first is listing all the incidents from db
# and second is creating a new incident if user sends data

class IncidentList(APIView):

    # inside this get function what im doing is simple
    # first im fetching all incidents from db using .all()
    # then im serializing them coz we cant send raw db objects
    # and finally returning that serialized data in the response

    def get(self, request):
        incidents = Incident.objects.all()  
        serializer = IncidentSerializer(incidents, many=True)  
        return Response(serializer.data) 

    # in this post function here i am handling data which
    # is coming from frontend/user side
    # so first im making a serializer object with that data
    # then checking if serializer is valid (means data is ok)
    # if it is valid im saving that data to db
    # and returning the saved data with 201 created status
    # otherwise if not valid im sending back error and 400 bad request

    def post(self, request):
        serializer = IncidentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# here i made another class IncidentDetail
# this one is handling cases when user wants
# either details of one specific incident
# or wants to delete that particular incident

class IncidentDetail(APIView):

    # in this get function basically what im doing is
    # first trying to fetch one incident from db using pk (primary key)
    # if that id exists then serializing it and sending back
    # if not found then returning an error msg with 404 not found status

    def get(self, request, pk):
        try:
            incident = Incident.objects.get(pk=pk)  
        except Incident.DoesNotExist:
            return Response({'error':'Incident not found'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = IncidentSerializer(incident) 
        return Response(serializer.data)  

    # in this delete function im trying to delete the incident
    # first again trying to find it using pk
    # if not found then sending error msg
    # if found then deleting it and returning empty 204 response
    # 204 means successfully deleted but no content to show

    def delete(self, request, pk):
        try:
            incident = Incident.objects.get(pk=pk) 
        except Incident.DoesNotExist:
            return Response({'error':'Incident not found'}, status=status.HTTP_404_NOT_FOUND) 
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
