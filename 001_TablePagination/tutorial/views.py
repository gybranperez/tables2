from django.shortcuts import render

from django.views.generic import ListView
from .models import Person

from django_tables2 import SingleTableView
from .tables import PersonTable

from django_tables2.config import RequestConfig
# Create your views here.

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


class PersonTableView(SingleTableView):
    model = Person
    
    table = PersonTable
    template_name = 'peopleTable.html'
def PersonTableFunction(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request, paginate={"per_page": 5}).configure(table)
    return render(request, "peopleTableFunction.html", {"table": table})