from django.db import models

# Create your models here.
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=40)

    def __str__(self):
         return self.nazwa

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"

class Wydawnictwo(models.Model):
    nazwa = models.CharField(max_length=40)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Wydawnictwa"
        verbose_name_plural = "Wydawnictwa"

class Ksiazki(models.Model):
    wydawnictwo = models.ForeignKey(Wydawnictwo, on_delete=models.CASCADE, null=True)
    kategoria = models.ForeignKey(Kategoria,on_delete=models.CASCADE,null=True)
    nazwa = models.CharField(max_length=40)
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Ksiazki"
        verbose_name_plural = "Ksiazki"