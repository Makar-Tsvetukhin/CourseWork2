from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Animal

class AnimalListView(ListView):
    model = Animal
    template_name = "animals/index.html"
    context_object_name = "animals"

class AnimalCreateView(CreateView):
    model = Animal
    fields = ['name', 'species', 'age', 'health_status', 'diet', 'location']
    template_name = "animals/form.html"
    success_url = reverse_lazy('animal-list')

class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ['name', 'species', 'age', 'health_status', 'diet', 'location']
    template_name = "animals/form.html"
    success_url = reverse_lazy('animal-list')

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = "animals/confirm_delete.html"
    success_url = reverse_lazy('animal-list')
