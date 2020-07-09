from django.shortcuts import render

from django.views.generic import ListView
from .models import Person

from django_tables2 import SingleTableView
from .tables import PersonTable


# Create your views here.

data = [
    {
        "name": "lista personas",
        "link": "/peopleList"
    },{
        "name": "tabla personas",
        "link": "/peopleTable"
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