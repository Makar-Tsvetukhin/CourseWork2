from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events/index.html"
    context_object_name = "events"

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'date', 'description', 'capacity', 'price']
    template_name = "events/form.html"
    success_url = reverse_lazy('event-list')

class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'date', 'description', 'capacity', 'price']
    template_name = "events/form.html"
    success_url = reverse_lazy('event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = "events/confirm_delete.html"
    success_url = reverse_lazy('event-list')