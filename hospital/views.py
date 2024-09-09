from rest_framework import mixins, generics
from .permissions import CustomPermission
from .models import (
    Patient,
    Doctor,
    Staff,
    Appointment,
    MedicalRecord,
    Invoice,
    Inventory,
    EmergencyCase,
)
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    StaffSerializer,
    AppointmentSerializer,
    MedicalRecordSerializer,
    InvoiceSerializer,
    InventorySerializer,
    EmergencyCaseSerializer,
)


# Create your views here.
class PatientList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class PatientDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

class DoctorList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class DoctorDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class StaffList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class StaffDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class AppointmentList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class AppointmentDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class MedicalRecordList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class MedicalRecordDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class InvoiceList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class InvoiceDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class InventoryList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class InventoryDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
class EmergencyCaseList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = EmergencyCase.objects.all()
    serializer_class = EmergencyCaseSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class EmergencyCaseDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = EmergencyCase.objects.all()
    serializer_class = EmergencyCaseSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
