import django_tables2 as tables
from .models import Ticket

class TicketTable(tables.Table):
    class Meta:
        model = Ticket
        template_name = 'django_tables2/bootstrap.html'