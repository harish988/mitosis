from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .ml import annotate
from .models import Model
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.conf import settings

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the


@csrf_exempt
def home(request):
    return render(request, 'upload/index.html', { 'path':None })

@csrf_exempt
def result(request, image_id):
    path = "/predictions/"+image_id+".jpg"
    print(Model.objects.get(id=1))
    model = Model.objects.get(id=1).model
    start_features = settings.MODELS[model]
    return render(request, 'upload/index.html', {'path':path, 'start_feature': start_features})

class FileUploadView(CsrfExemptSessionAuthentication, APIView):
    parser_class = (FileUploadParser,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        annotated_image = annotate(request.data)
        file_serializer = FileSerializer(data=request.data)
        model = request.data["model"]
        if(Model.objects.all().count() > 0):
            Model.objects.get(id=1).delete()
        row = Model(id=1, model=model)
        row.save()
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)