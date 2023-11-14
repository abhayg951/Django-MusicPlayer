from django.views import generic
from rest_framework import viewsets
from core.models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class MusicView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        book = Music.objects.all()
        serializer = MusicSerializer(book, many=True)
        return Response(serializer.data)
