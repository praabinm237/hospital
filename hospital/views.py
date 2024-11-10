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
    DoctorPatient,
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
    DoctorPatientSerializer,
)
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response


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
        user = request.user
        doctor_group = Group.objects.get(name="Doctor")
        isDoctor = request.user.groups.contains(doctor_group)
        if isDoctor:
            print("doctor")

        return Response(request.user.groups.contains(doctor_group))
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor_id = serializer.validated_data['groups']
        try:
            user = User.objects.get(email=user)
        except:
            return Response({'error': 'User with this email doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
            group = Group.objects.get(name=group_name)
        except:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
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
    
class DoctorPatientList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    queryset = DoctorPatient.objects.all()
    serializer_class = DoctorPatientSerializer
    permission_classes = [CustomPermission]
        
    def get(self,request):
        return self.list(request)
            
    def post(self,request):
        return self.create(request)
      
class DoctorPatientDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = DoctorPatient.objects.all()
    serializer_class = DoctorPatientSerializer
    permission_classes = [CustomPermission]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
