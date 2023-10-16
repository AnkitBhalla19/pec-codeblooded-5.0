

from django.shortcuts import render
from .models import SalaryRecord

def send_data_to_postgresql(request):
    # Create and save a new record in the database
    new_data = SalaryRecord(WAGE_RATE_OF_PAY_FROM='Value1', WAGE_UNIT_OF_PAY='value2')
    new_data.save()
    
    return render(request, 'send_data_success.html')