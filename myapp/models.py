from django.db import models

class ModelOne(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class ModelTwo(models.Model):
    name = models.CharField(max_length=50)
    model_one = models.ForeignKey(to=ModelOne, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
