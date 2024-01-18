from django.contrib import admin

from Elearning.models import Absence,ModuleA ,Enregistrement, Enseignant, Etudiant, Evaluation, Groupe, Responsable, Seance, SeanceEnLigne, SeancePresontiel, Travail_a_Rendre

# Register your models here.

admin.site.register(Groupe)
admin.site.register(ModuleA)
admin.site.register(Enseignant)
admin.site.register(SeanceEnLigne)
admin.site.register(SeancePresontiel)
admin.site.register(Enregistrement)
admin.site.register(Evaluation)
admin.site.register(Travail_a_Rendre)
admin.site.register(Etudiant)
admin.site.register(Absence)
admin.site.register(Responsable)