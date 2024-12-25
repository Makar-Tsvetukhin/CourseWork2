from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Statistics
from django.db.models import Sum, IntegerField, DecimalField
from django.db.models.functions import Coalesce
from datetime import datetime

class StatisticsListView(ListView):
    model = Statistics
    template_name = "statistics/index.html"
    context_object_name = "statistics"

    def get_queryset(self):
        queryset = Statistics.objects.all()
        
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%d.%m.%Y').date()
                queryset = queryset.filter(date__gte=start_date)
            except ValueError:
                print(f"Ошибка преобразования начальной даты: {start_date}")

        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%d.%m.%Y').date()
                queryset = queryset.filter(date__lte=end_date)
            except ValueError:
                print(f"Ошибка преобразования конечной даты: {end_date}")

        print(f"SQL Query: {queryset.query}")
        print(f"Количество записей: {queryset.count()}")
        
        return queryset.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        context['debug'] = {
            'start_date': self.request.GET.get('start_date'),
            'end_date': self.request.GET.get('end_date'),
            'query_string': self.request.GET.urlencode(),
            'sql_query': str(queryset.query),
            'record_count': queryset.count()
        }

        # Определяем output_field для revenue в соответствии с моделью
        revenue_field = DecimalField(max_digits=12, decimal_places=2)
        
        summary = queryset.aggregate(
            total_visitors=Coalesce(
                Sum('visitors_count', output_field=IntegerField()),
                0,
                output_field=IntegerField()
            ),
            total_revenue=Coalesce(
                Sum('revenue', output_field=revenue_field),
                0,
                output_field=revenue_field
            ),
            total_events=Coalesce(
                Sum('event_count', output_field=IntegerField()),
                0,
                output_field=IntegerField()
            )
        )
        
        context.update(summary)
        return context

class StatisticsCreateView(CreateView):
    model = Statistics
    fields = ['date', 'visitors_count', 'revenue', 'event_count']
    template_name = "statistics/form.html"
    success_url = reverse_lazy('statistics-list')

class StatisticsUpdateView(UpdateView):
    model = Statistics
    fields = ['date', 'visitors_count', 'revenue', 'event_count']
    template_name = "statistics/form.html"
    success_url = reverse_lazy('statistics-list')

class StatisticsDeleteView(DeleteView):
    model = Statistics
    template_name = "statistics/confirm_delete.html"
    success_url = reverse_lazy('statistics-list')