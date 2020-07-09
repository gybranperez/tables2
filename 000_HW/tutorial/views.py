from django.shortcuts import render

from django.views.generic import ListView
from .models import Person

from django_tables2 import SingleTableView
from .tables import PersonTable
# Create your views here.
 
def index (request):
    return render(request, 'index.html')

class PersonListView(ListView):
    model = Person
    template_name = 'peopleList.html'

class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'peopleTable.html'