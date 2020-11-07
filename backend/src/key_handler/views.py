from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .models import Session, Key
from .serializers import SessionSerializer, UpdateSessionSerializer


# Create your views here.

@api_view(['POST'])
def update_session(request):

    if request.method == 'POST':

        
        serializer = UpdateSessionSerializer(data=request.data)
        
        
        
        if serializer.is_valid():
            
            # Delete all sessions longer than 5min to minmize cpu usage
            Session.objects.filter(expire_date__lt=timezone.datetime.now()).delete() 


            key = Key.objects.get(pk=serializer.data['license'])
            
            num_sessions = len(set([session_object.remote_session_id for session_object in Session.objects.filter(license__exact=key.license)]))

            if num_sessions > key.num_sessions_allowed:
                return Response("Max session limit reached for key, if program crashed please wait 5min and try again", status=status.HTTP_409_CONFLICT) 

            new_session = Session(remote_session_id=data['remote_session_id'], license=key)
            new_session.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_sessions(request):
    """
    List all sessions, or create a new snippet.
    """
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)




'''
@api_view(['POST'])
def generate_key(request):
    """
    Generates a new key
    """

    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
