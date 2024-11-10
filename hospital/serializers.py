from rest_framework import serializers
from .models import (
    Patient, 
    Doctor, 
    Staff, 
    Appointment,
    MedicalRecord,
    Invoice,
    Inventory,
    EmergencyCase,
    DoctorPatient
)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name','phone_number','medical_history']
    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','first_name','last_name','phone_number','specialty']
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id','first_name','last_name','phone_number','role']
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','patient','doctor','date','status']
        
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id','patient','doctor','diagnosis','treatment','date']
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','patient','amount','status','date_issued']
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id','name','quantity','unit_price','category']
        
class EmergencyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyCase
        fields = ['id','patient','description','status','date_reported']
        
class DoctorPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorPatient
        fields = ['doctor','patient']