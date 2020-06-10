from django.db import models
from django.contrib.auth.models import User

class Assurance(models.Model):
    ville=models.CharField(max_length=255)
    natureAssurance=models.CharField(max_length=255)
    specialiteExecute=models.CharField(max_length=255)
    qualiteBenificiaire=models.CharField(max_length=255)
    manierExecuter=models.CharField(max_length=255)
    prestation=models.CharField(max_length=255)
    tauxRemb=models.FloatField()
    baseRemb=models.FloatField()
    dateRemb=models.CharField(max_length=7)
    dateEnregitrement=models.DateTimeField(auto_now_add=True)
    auteur=models.ForeignKey(User,on_delete=models.CASCADE)
    archive=models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.natureAssurance} : {self.dateRemb}]"


