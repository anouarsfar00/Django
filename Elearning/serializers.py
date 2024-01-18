from django.db.models import fields
from projet_django.Elearning_Solution.Elearning.models import Enseignant
from rest_framework import serializers
from Elearning.models import Etudiant, Travail_a_Rendre


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta :
        model = Etudiant
        fields=('first_name','last_name','dateEt','imageEt','mailEt','etatEt','situationEt','idgroupe')



class Travail_a_RendreSerializer(serializers.ModelSerializer):
    class Meta :
        model = Travail_a_Rendre
        fields=('titreT','date_lancement','date_limite','descrip','nature_travail','pieceTa','etat','eval')

class EnseignementSerializer(serializers.ModelSerializer):
    class Meta:
        model:Enseignant
        fields:('nomENS','prenomENS','mailPerso','mailTravail','imageENS','module')