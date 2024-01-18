from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.
dir='storage/images'

# enumération
class type_enreg (models.TextChoices) :
    MP4 =('mp4','mp4')   
    FLV =('flv','flv') 
    MOV =('mov','mov') 
    AVI =('avi','avi') 
    WMV =('wmv','wmv')


class ETAT (models.TextChoices) :
   PRESENT =('present','Etudiant present')   
   ABSCENT =('abscent','Etudiant abscent') 
   RETARD  =('retard','Etudiant en retard') 
   EXCLU  =('exclu','Etudiant exclu') 


class SITUATION (models.TextChoices) :
   NOUVEAU  =('nouveau','Nouveau etudiant')   
   REDOUBLANT =('redoublant','Etudiant redoublant') 
   DEROGATAIRE =('derogataire','Etudiant derogataire') 
   AUTRE =('autre','Etudiant autre') 


class t_module (models.TextChoices) :
    OPTIONNEL =('optionnel','Model optionnel')   
    OBLIGATOIRE =('obligatoire','Model obligatoire') 



class type_Seance (models.TextChoices) :
    NORMALE =('Normale','Normale Seance')   
    RATTRAPPAGE =('Rattrapage','Rattrapage Seance') 
    SOUTIEN =('Soutien','Soutien Seance') 
    FORMATION =('Formation','Formation Seance') 



class ETATS (models.TextChoices) : 

   EN_COURS =('En_cours','En cours')   
   TERMINEE =('Terminée','Terminée') 
   ANNULEE =('Anulée','Anulée') 
   DIFFERE  =('Différée','Différée') 





 

class Groupe(models.Model):
	nomG = models.CharField( name ='groupe_name',max_length=50)
	nbEtudiants = models.IntegerField()
	mailG = models.EmailField(max_length=30)
	niveau = models.IntegerField()
    





class ModuleA(models.Model):
 nomMO = models.CharField( name ='nom_module',max_length=50,unique=True)
 nbheure = models.IntegerField()
 typem = models.CharField(max_length=11,choices=t_module.choices, default =t_module.OPTIONNEL ) 
 niveauM=models.IntegerField()
 groupeM = models.ManyToManyField(Groupe)
 class Meta :
      db_table ='ModuleA_tab'


class Enseignant(models.Model):
	nomEns = models.CharField( name ='first_nameens',max_length=50)
	prenomEns = models.CharField( name ='last_nameens',max_length=50 )
	mailPerso = models.EmailField(max_length=30)
	mailTravail = models.EmailField(max_length=30)
	imageEns = models.ImageField(null=True,blank=True ,upload_to=dir )
	module=models.ManyToManyField(ModuleA)


class Evaluation(models.Model):
       note = models.IntegerField()  
       commentaire=models.CharField(max_length=100)





class Travail_a_Rendre(models.Model):
       titreT=models.CharField(max_length=100)
       date_lancement = models.DateField(default=timezone.now ) 
       date_limite=models.DateField(default=timezone.now)
       description=models.CharField( name ='descrip',max_length=150 )
       nature=models.CharField( name ='nature_travail',max_length=50 )
       pieceTa = models.TextField(max_length=60)
       etat= models.BooleanField()
       idmodule =models.ForeignKey(ModuleA,on_delete=models.CASCADE)
       eval = models.OneToOneField(Evaluation,on_delete=models.CASCADE)
       class Meta :
        db_table ='Travail_a_Rendre_tab'


     

class Etudiant(models.Model) : 
 nomEt = models.CharField ( name='first_name', max_length=50)
 prenomEt = models.CharField ( name='last_name', max_length=50)
 dateEt = models.DateField (null=False, blank=True)
 imageEt = models.ImageField(null=True,blank=True ,upload_to=dir  )
 mailEt = models.EmailField(max_length=60)
 etatEt =models.CharField(max_length=11,choices=ETAT.choices, default =ETAT.PRESENT) 
 situationEt = models.CharField(max_length=11,choices=SITUATION.choices, default =SITUATION.AUTRE) 
 idgroupe =models.ForeignKey(Groupe,on_delete=models.CASCADE)
 travailarendreE=models.ManyToManyField(Travail_a_Rendre)
 class Meta :
      db_table ='Etudiant_tab'







class Seance(models.Model) : 
    Heure_Debut = models.DateTimeField()
    Heure_Fin = models.DateTimeField()
    objectif= models.TextField(max_length=120)
    resume = models.TextField(max_length=200)
    typeS = models.CharField(max_length=11,choices=type_Seance.choices, default =type_Seance.NORMALE) 
    EtatS =  models.CharField(max_length=11,choices=ETATS.choices, default =ETATS.DIFFERE)
    idModule =models.ForeignKey(ModuleA,on_delete=models.CASCADE)
    etud=models.ManyToManyField(Etudiant)
    

    class Meta :
        abstract = True 
       


class SeanceEnLigne (Seance) :
    class Meta :
      db_table ='SeanceEnLigne_tab'
class SeancePresontiel(Seance):
    #instruction vide
   # pass
   numSalle =  models.CharField (max_length=4)
   outils =  models.CharField (max_length=50)
   class Meta :
      db_table ='SeancePresontiel_tab'


 
class Enregistrement(models.Model) : 
    nomENR= models.CharField( max_length=50 ,unique=True) 
    urlENR = models.CharField(blank=True, max_length=50) 
    contenuENR = models.TextField() 
    typeENR = models.CharField(max_length=3,choices=type_enreg.choices ,blank=True) 
    descriptionENR = models.CharField( max_length=50) 
    dateENR = models.DateField(default=timezone.now ) 
    idseanceEN =models.ForeignKey(SeanceEnLigne,on_delete=models.CASCADE)
    class Meta :
       db_table ='Enregistrement_tab'
       
   










class Absence(models.Model):
       dateA= models.DateField(default=timezone.now ) 
       motif = models.TextField( max_length=100,blank=True)
       justificatif= models.TextField( max_length=100)
       idetudiant =models.ForeignKey(Etudiant,on_delete=models.CASCADE)
       seanceEN = models.OneToOneField(SeanceEnLigne,on_delete=models.CASCADE)
       seanceP = models.OneToOneField(SeancePresontiel,on_delete=models.CASCADE)
       class Meta :
        db_table ='Absence_tab'


class Responsable(Enseignant):

  class Meta :
     db_table ='responsable_tab'
