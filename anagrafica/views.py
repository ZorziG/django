from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.views import View
from .models import Anagrafica
from .forms import AnagraficaModelForm

# Create your views here.
class AnagraficaCreateView(CreateView):
    template_name = "anagrafica\\anagrafica_create.html"
    form_class = AnagraficaModelForm
    queryset = Anagrafica.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)  

class AnagraficaListView(ListView):
    template_name = "anagrafica\\anagrafica_list.html"
    queryset = Anagrafica.objects.all()

class AnagraficaDetailView(DetailView):
    template_name = "anagrafica\\anagrafica_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Anagrafica, codottico=id_)

class AnagraficaUpdateView(UpdateView):
    template_name = "anagrafica\\anagrafica_create.html"
    form_class = AnagraficaModelForm
    queryset = Anagrafica.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form) 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Anagrafica, codottico=id_)

class AnagraficaDeleteView(DeleteView):
    template_name = "anagrafica\\anagrafica_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Anagrafica, codottico=id_)

    def get_success_url(self):
        return reverse("anagrafica:anagrafica-list") 

class AnagraficaMenuView(View):
    template_name = "anagrafica\\anagrafica_menu.html"
    def get(self, request, *args, **kwargs):
        context = {
            "anagrafica_menu" : [
                "Mostra anagrafica", "Inserire anagrafica",
                "Modifica anagrafica", "Cancella anagrafica", 
                "Cerca anagrafica", "Torna indietro"
                ]
        }     
        return render(request, self.template_name, context)
