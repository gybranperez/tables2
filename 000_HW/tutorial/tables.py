# tutorial/tables.py
import django_tables2 as tables
from .models import Person
class PersonTable(tables.Table):
    class Meta:
        model = Person
        """
        Hay varios templates pata renderizar las tablas
        https://django-tables2.readthedocs.io/en/latest/pages/custom-rendering.html
        """
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name","lastname" )