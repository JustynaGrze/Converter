from django.contrib import admin
from converter.models import Converter, ConversionResult

# Register your models here.
admin.site.register(Converter)
admin.site.register(ConversionResult)
