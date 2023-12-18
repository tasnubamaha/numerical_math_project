from django.db import models

# Create your models here.
class MathProblem(models.Model):
    latex_input = models.TextField()
    result = models.TextField()