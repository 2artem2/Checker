from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    code_thhp = models.IntegerField(default=404)
    port_site = models.IntegerField(default=80)
    update_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.id)
    

# Create your models here.
