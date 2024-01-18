from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from Elearning.models import Etudiant
from rest_framework import routers


from Elearning.views import EtudiantViewSet, Travail_a_RendreViewSet,etudiant,etudiant_detail


router=routers.DefaultRouter()

router.register(r'etudiant',EtudiantViewSet)
router.register(r'travailarendre',Travail_a_RendreViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('alletudiant/',etudiant,name='allauthor'),
    path('etudiant/<int:pk>/',etudiant_detail,name='EtuDetail'),
]