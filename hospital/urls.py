
from django.urls import path
from .views import (
    PatientList, PatientDetail,
    DoctorList, DoctorDetail,
    StaffList, StaffDetail,
    AppointmentList, AppointmentDetail,
    MedicalRecordList, MedicalRecordDetail,
    InvoiceList, InvoiceDetail,
    InventoryList, InventoryDetail,
    EmergencyCaseList, EmergencyCaseDetail,
    DoctorPatientList, DoctorPatientDetail,
)

urlpatterns = [
    path('patients',PatientList.as_view()),
    path('patients/<pk>',PatientDetail.as_view()),
    path('doctors',DoctorList.as_view()),
    path('doctors/<pk>',DoctorDetail.as_view()),
    path('staffs',StaffList.as_view()),
    path('staffs/<pk>',StaffDetail.as_view()),
    path('appointments',AppointmentList.as_view()),
    path('appointments/<pk>',AppointmentDetail.as_view()),
    path('medical_records',MedicalRecordList.as_view()),
    path('medical_records/<pk>',MedicalRecordDetail.as_view()),
    path('invoices',InvoiceList.as_view()),
    path('invoices/<pk>',InvoiceDetail.as_view()),
    path('inventories',InventoryList.as_view()),
    path('inventories/<pk>',InventoryDetail.as_view()),
    path('emergency_cases',EmergencyCaseList.as_view()),
    path('emergency_cases/<pk>',EmergencyCaseDetail.as_view()),
    path('doctorpatient',DoctorPatientList.as_view()),
    path('doctorpatient/<pk>',DoctorPatientDetail.as_view()),
]
