from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.views.generic import ListView

from hospital.models import Patient

class PatientWizard(SessionWizardView):
    template_name = 'patient_form.html'

    def done(self, form_list, **kwargs):
        patient = form_list[0].save()
        for form in form_list[1:]:
            form.save(patient)
        return redirect('patient_list')


class PatientListView(ListView):
    queryset = Patient.objects.all()
    template_name = 'patient_list.html'
    model = Patient
    context_object_name = 'patients'