from django import forms
from hospital.models import Patient, Ecog, BloodType, Imaging, ImageryType


class PatientForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField()

    def save(self, commit=True):
        patient = Patient(**self.cleaned_data)
        if commit:
            patient.save()
        return patient


class EcogForm(forms.Form):
    ecog = forms.ChoiceField(choices=Ecog.ECOG_CHOICES)

    def save(self, patient, commit=True):
        value = self.cleaned_data['ecog']
        ecog = Ecog(patient=patient, value=value)
        if commit:
            ecog.save()
        return ecog
    

class BloodTypeForm(forms.Form):
    blood_type = forms.ChoiceField(choices=BloodType.BLOOD_TYPE_CHOICES)

    def save(self, patient, commit=True):
        value = self.cleaned_data['blood_type']
        blood_type = BloodType(patient=patient, value=value)
        if commit:
            blood_type.save()
        return blood_type


class ImagingForm(forms.Form):
    imaging = forms.MultipleChoiceField(choices=ImageryType.IMAGING_CHOICES)

    def save(self, patient, commit=True):
        value = self.cleaned_data['imaging']
        imaging = Imaging(patient=patient)
        if commit:
            imaging.save()
        for v in value:
            imagery_type = ImageryType(imaging=imaging, value=v)
            if commit:
                imagery_type.save()
        return imaging

