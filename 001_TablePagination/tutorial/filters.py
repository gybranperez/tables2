from django_filters import FilterSet,CharFilter

from .models import Person


class PersonFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')#iexact
    
    class Meta:
        model = Person
        fields = ["name"]
