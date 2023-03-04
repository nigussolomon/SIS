from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SisUser
from .serializers import SisUserSerializer, CreateSisUserSerializer


class RegisterUser(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateSisUserSerializer

class ListUsers(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        results = SisUser.objects.all()
        serializer = SisUserSerializer(results, many=True)
        return Response({"SUCCESS": True, "DATA": serializer.data}, status=status.HTTP_200_OK)
