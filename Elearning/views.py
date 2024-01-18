from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from Elearning.models import Etudiant, Responsable, Travail_a_Rendre
from Elearning.serializers import EtudiantSerializer, Travail_a_RendreSerializer
from rest_framework import viewsets


# Create your views here.
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset=Etudiant.objects.all()
    serializer_class=EtudiantSerializer

class Travail_a_RendreViewSet(viewsets.ModelViewSet):
    queryset=Travail_a_Rendre.objects.all()
    serializer_class=Travail_a_RendreSerializer
    
class EnseignantViewset(viewsets.ModelViewSet):
    querySet=Enseignant.objects.all()
    serializer_class=EnseignantSerializer


@api_view(['GET', 'POST'])
def etudiant(request):

    if request.method == 'GET':
        TravailaRendre = Etudiant.objects.all()
        serializer = EtudiantSerializer(TravailaRendre, many=True)
        return Responsable(serializer.data)

    elif request.method == 'POST':
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def etudiant_detail(request, pk):
    try:
        author = Etudiant.objects.get(pk=pk)
    except Etudiant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def enseignant(request):

    if request.method == 'GET':
        TravailaRendre = Enseignant.objects.all()
        serializer = EnseignantSerializer(TravailaRendre, many=True)
        return Responsable(serializer.data)

    elif request.method == 'POST':
        serializer = EnseignantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def enseignant_detail(request, pk):
    try:
        author = Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
