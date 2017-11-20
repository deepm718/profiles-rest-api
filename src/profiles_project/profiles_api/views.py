from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (GET, POST, PUT, PATCH, DELETE)',
            'It is a similer to a traditional dgango view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Helloo..', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with your name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, Only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""


        a_viewset = [
            'Uses actions (list, create, retreave, update, partial_update)',
            'Automatically maps to Urls using routers',
            'Provides more functionality with less code',
        ]
        return Response({'Messafe': 'Hello...', 'a_viewset': a_viewset})



    def create(self, request):
        """Create a hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object by it's ID."""

        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Handles updating an object."""
        #serializer = serializers.HelloSerializer(data=request.data)

        #updates = request.data

        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """handles updating part of an object."""

        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

#"""Following section for permission classes...."""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


#""""""""""""""""" Filter backends.......
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    