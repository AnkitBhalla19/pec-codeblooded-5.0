from django.db import models
import csv 
class SalaryRecord(models.Model):
    WAGE_UNIT_OF_PAY = models.CharField(max_length=255)
    WAGE_RATE_OF_PAY_FROM = models.IntegerField(max_length=255)
    

def import_csv_data(csv_file):
    with csv_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            SalaryRecord.objects.create(
                field1=row['WAGE_RATE_OF_PAY_FROM'],  # Use field1 to match the model's field name
                field2=row['WAGE_UNIT_OF_PAY'],  
            )
    