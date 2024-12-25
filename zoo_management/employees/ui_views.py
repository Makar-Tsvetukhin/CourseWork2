from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = "employees/index.html"
    context_object_name = "employees"

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'position', 'department', 'hire_date', 'schedule', 'contact_info']
    template_name = "employees/form.html"
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'position', 'department', 'hire_date', 'schedule', 'contact_info']
    template_name = "employees/form.html"
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employees/confirm_delete.html"
    success_url = reverse_lazy('employee-list')