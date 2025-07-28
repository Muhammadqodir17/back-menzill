from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response


class HomeViewSet(ViewSet):
    def header(self, request, *args, **kwargs):
        pass
