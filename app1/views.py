from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.response import Response
from .serializers import *
class SavolApi(APIView):
    def get(self, request):
        savol = Savol.objects.all()
        serializer = SavolSerializer(savol, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SavolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'good'})
        return Response(serializer.errors)

class JavobApi(APIView):
    def post(self, request):
        serializer = JavobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status:Saved"})
        return Response(serializer.errors)

class JavobModelView(ModelViewSet):
    queryset = Javob.objects.all()
    serializer_class = JavobSerializer
