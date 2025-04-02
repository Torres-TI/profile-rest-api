from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View """
    def get(self, request, format=None):
        """Return a list of APIView features."""
        an_apiview = [
            'Uses http as fucntions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello','an_apiview' : an_apiview})
# Create your views here.
