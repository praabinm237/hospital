from enum import Enum, auto

class Role(Enum):
    DOCTOR = auto()
    NURSE = auto()
    RECEPTIONIST = auto()
    MANAGER = auto()

class Permission(Enum):
    VIEW_PATIENT = auto()
    EDIT_PATIENT = auto()
    DELETE_PATIENT = auto()
    ADD_PATIENT = auto()
    VIEW_APPOINTMENT = auto()
    EDIT_APPOINTMENT = auto()
    SCHEDULE_APPOINTMENT = auto()
    CANCEL_APPOINTMENT = auto()
    ACCESS_PATIENT_CLASS = auto()
    ACCESS_APPOINTMENT_CLASS = auto()

role_permissions = {
    Role.DOCTOR: {
        Permission.VIEW_PATIENT, 
        Permission.EDIT_PATIENT, 
        Permission.VIEW_APPOINTMENT,
        Permission.ACCESS_PATIENT_CLASS
    },
    Role.NURSE: {
        Permission.VIEW_PATIENT, 
        Permission.VIEW_APPOINTMENT, 
        Permission.SCHEDULE_APPOINTMENT,
        Permission.ACCESS_PATIENT_CLASS,
        Permission.ACCESS_APPOINTMENT_CLASS
    },
    Role.RECEPTIONIST: {
        Permission.VIEW_PATIENT, 
        Permission.ADD_PATIENT, 
        Permission.SCHEDULE_APPOINTMENT, 
        Permission.CANCEL_APPOINTMENT,
        Permission.ACCESS_APPOINTMENT_CLASS
    },
    Role.MANAGER: {
        Permission.VIEW_PATIENT, 
        Permission.EDIT_PATIENT, 
        Permission.DELETE_PATIENT, 
        Permission.ADD_PATIENT, 
        Permission.VIEW_APPOINTMENT, 
        Permission.EDIT_APPOINTMENT, 
        Permission.SCHEDULE_APPOINTMENT, 
        Permission.CANCEL_APPOINTMENT,
        Permission.ACCESS_PATIENT_CLASS,
        Permission.ACCESS_APPOINTMENT_CLASS
    },
}

def has_permission(role, permission):
    return permission in role_permissions.get(role, set())

class Patient:
    def __init__(self, user, name, age):
        if not has_permission(user.role, Permission.ACCESS_PATIENT_CLASS):
            raise PermissionError(f"{user.role.name} does not have access to the Patient class.")
        self.user = user
        self.name = name
        self.age = age

    def get_details(self):
        if has_permission(self.user.role, Permission.VIEW_PATIENT):
            return f"Patient Name: {self.name}, Age: {self.age}"
        else:
            return "Permission denied."


