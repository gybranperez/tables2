# tutorial/tables.py
import django_tables2 as tables
from .models import Person
#Libreria para exportar tablas a csv, json, latex, ods, tsv, xls, xlsx, yaml
from django_tables2.export.views import ExportMixin
class PersonTable(ExportMixin,tables.Table):
    class Meta:
        model = Person
        """
        Hay varios templates pata renderizar las tablas
        https://django-tables2.readthedocs.io/en/latest/pages/custom-rendering.html
        """
        
        empty_text = "No hay datos que mostrar"
        template_name = "django_tables2/bootstrap4.html"
        #fields = ("id","name","lastname" )
