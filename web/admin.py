from django.contrib import admin
from web.models import Hospital, Patient, Physician
 
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'gender', 'age',]




@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = [ 'Hospital_name',]



@admin.register(Physician)
class PhysicianAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'expertise',]
 
