from django.db import models

# Create your models here.
from enum import auto
from tkinter import CASCADE
from django.db import models

# Create your models here.
class VehicleDetails(models.Model):
    vehicle_number=models.CharField(max_length=50,primary_key=True)
    vehicle_model=models.CharField(max_length=20)
    driver_name=models.CharField(max_length=20)
    ac_unit=models.CharField(max_length=30)
    r_mileage=models.FloatField()
    nr_mileage=models.FloatField()
    empty_mileage=models.FloatField()

class trip_details(models.Model):
    trip_id=models.AutoField(primary_key=True)
    vehicle_number=models.ForeignKey(VehicleDetails,on_delete=models.CASCADE)
    t_frm_date=models.DateField()
    t_to_date=models.DateField()
    client=models.CharField(max_length=20)
    opening_km=models.IntegerField()
    closing_km=models.IntegerField()
    total_km=models.IntegerField()
    hsd_rate=models.FloatField()
    hsd_ltr=models.FloatField()
    Total_value=models.FloatField()
    ac_start_hr=models.IntegerField()
    ac_end_hr=models.IntegerField()
    ac_total_hours=models.IntegerField()
    ac_mileage=models.FloatField()
    total_hsd_ac=models.FloatField()
    total_AC_HSD=models.FloatField()
    grand_total_hsd_ltr=models.FloatField()
    grand_total_hsd=models.FloatField()




