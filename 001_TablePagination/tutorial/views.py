from django.shortcuts import render

from django.views.generic import ListView
from .models import Person

from django_tables2 import SingleTableView,SingleTableMixin
from .tables import PersonTable

from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport
# Create your views here.

from .filters import PersonFilter
#Libreria para filtros de las tablas
from django_filters.views import FilterView

#Links del Index
data = [
    {
        "name": "table people",
        "link": "/peopleTable"
    },{
        "name": "table people function",
        "link": "/peopleTableFunction"
    },
]

def index (request):
    context = {
        "data":data,
    }
    return render(request, 'index.html',context)

class PersonListView(ListView):
    model = Person
    template_name = 'peopleList.html'
    

class PersonTableView(SingleTableMixin,FilterView):
    model = Person
    filterset_class = PersonFilter
    table_class = PersonTable
    table_pagination = {
        'per_page': 3,
    }
    template_name = 'peopleTable.html'
    
def PersonTableFunction(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request, paginate={"per_page": 5}).configure(table)
    return render(request, "peopleTableFunction.html", {"table": table})