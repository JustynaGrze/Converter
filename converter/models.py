from django.db import models


# Create your models here.
class Converter(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Converter {self.name}"


class ConversionResult(models.Model):
    converter = models.ForeignKey(Converter, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='', blank=True)
    output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ConversionResult {self.id} - {self.converter.name}"
