from django.urls import path

from hospital.forms import PatientForm, EcogForm, BloodTypeForm, ImagingForm
from hospital.views import PatientWizard, PatientListView

urlpatterns = [
    path('', PatientWizard.as_view([PatientForm, EcogForm, BloodTypeForm, ImagingForm])),
    path('list/', PatientListView.as_view(), name='patient_list'),
]