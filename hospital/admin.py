from django.contrib import admin
from .models import User, Patient, Doctor, Staff, Appointment, MedicalRecord, Invoice, Inventory, EmergencyCase

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['username','role']
    list_per_page = 10
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'medical_history',
    ]
    search_fields = ['first_name','last_name']
    list_per_page = 10
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'specialty',
        'phone_number',
    ]
    search_fields = ['first_name','last_name']
    list_per_page = 10
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'role',
        'phone_number',
    ]
    search_fields = ['first_name','last_name']
    list_per_page = 10
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'doctor',
        'date',
        'status',
    ]
    search_fields = ['patient','doctor']
    list_editable = ['status']
    list_filter = ['status']
    list_per_page = 10
    
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'doctor',
        'diagnosis',
        'treatment',
        'date',
    ]
    search_fields = ['patient']
    list_per_page = 10
    
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'amount',
        'status',
        'date_issued',
    ]
    search_fields = ['patient']
    list_editable = ['status']
    list_filter = ['status']
    list_per_page = 10
    
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'quantity',
        'unit_price',
        'category',
    ]
    search_fields = ['name','category']
    list_filter = ['category']
    list_per_page = 10
    
@admin.register(EmergencyCase)
class EmergencyCaseAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'description',
        'status',
        'date_reported',
    ]
    search_fields = ['patient']
    list_editable = ['status']
    list_filter = ['status']
    list_per_page = 10



    

    


