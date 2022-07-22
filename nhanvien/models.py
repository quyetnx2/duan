from django.db import models

# Create your models here.


# Create your models here.

class ThemMoiNV(models.Model):
    ten = models.CharField(max_length=100)
    chucvu = models.CharField(max_length=100)
    namsinh = models.CharField(max_length=100)

    def __str__(self):
        return self.ten
