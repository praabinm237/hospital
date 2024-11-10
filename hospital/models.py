from django.db import models

# Create your models here.
    
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    medical_history = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'
    
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'
    
class Appointment(models.Model):
    
    APPOINTMENT_SCHEDULED_CHOICE = 'SCHEDULED'
    APPOINTMENT_PENDING_CHOICE = 'PENDING'
    APPOINTMENT_RESCHEDULED_CHOICE = 'RESCHEDULED'
    APPOINTMENT_CANCELLED_CHOICE = 'CANCELLED'
    APPOINTMENT_NO_SHOW_CHOICE = 'NO_SHOW'
    APPOINTMENT_COMPLETED_CHOICE = 'COMPLETED'
    APPOINTMENT_FOLLOWUP_NEEDED_CHOICE = 'FOLLOWUP_NEEDED'
    
    APPOINTMENT_STATUS = [
        (APPOINTMENT_SCHEDULED_CHOICE, 'SCHEDULED'),
        (APPOINTMENT_PENDING_CHOICE, 'PENDING'),
        (APPOINTMENT_RESCHEDULED_CHOICE, 'RESCHEDULED'),
        (APPOINTMENT_CANCELLED_CHOICE, 'CANCELLED'),
        (APPOINTMENT_NO_SHOW_CHOICE, 'NO_SHOW'),
        (APPOINTMENT_COMPLETED_CHOICE, 'COMPLETED'),
        (APPOINTMENT_FOLLOWUP_NEEDED_CHOICE, 'FOLLOWUP_NEEDED'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(choices=APPOINTMENT_STATUS, max_length=255)
    
    def __str__(self) -> str:
        return f'Appointment ID #{self.pk}'
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    diagnosis = models.TextField()
    treatment = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f'Medical record ID #{self.pk}'
    
class Invoice(models.Model):
    
    INVOICE_PENDING_CHOICE = 'PENDING'
    INVOICE_PAID_CHOICE = 'PAID'
    INVOICE_CLOSED_CHOICE = 'CLOSED'
    
    INVOICE_STATUS = [
        (INVOICE_PENDING_CHOICE, 'PENDING'),
        (INVOICE_PAID_CHOICE, 'PAID'),
        (INVOICE_CLOSED_CHOICE, 'CLOSED'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(choices=INVOICE_STATUS, max_length=255)
    date_issued = models.DateTimeField()
    
    def __str__(self):
        return f'Invoice ID #{self.pk}'
    
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    category = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
    
class EmergencyCase(models.Model):
    
    EMERGENCY_ADMITTED_CHOICE = 'ADMITTED'
    EMERGENCY_IN_PROGRESS_CHOICE = 'IN_PROGRESS'
    EMERGENCY_STABILIZED_CHOICE = 'STABILIZED'
    EMERGENCY_IMPROVED_CHOICE = 'IMPROVED'
    EMERGENCY_TRANSFERRED_CHOICE = 'TRANSFERRED'
    EMERGENCY_DISCHARGED_CHOICE = 'DISCHARGED'
    
    EMERGENCY_STATUS = [
        (EMERGENCY_ADMITTED_CHOICE, 'ADMITTED'),
        (EMERGENCY_IN_PROGRESS_CHOICE, 'IN_PROGRESS'),
        (EMERGENCY_STABILIZED_CHOICE, 'STABILIZED'),
        (EMERGENCY_IMPROVED_CHOICE, 'IMPROVED'),
        (EMERGENCY_TRANSFERRED_CHOICE, 'TRANSFERRED'),
        (EMERGENCY_DISCHARGED_CHOICE, 'DISCHARGED'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=EMERGENCY_STATUS, max_length=255)    
    date_reported = models.DateTimeField()
    
    def __str__(self):
        return f'Emergency case ID #{self.pk}'
    
class DoctorPatient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Doctor : {Doctor.name} Patient : {Patient.name}'
    
    
       
    
    
    

    

