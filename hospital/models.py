from django.db import models
import uuid

class Patient(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.IntegerField()
    sex = models.PositiveSmallIntegerField()


class Ecog(models.Model):
    ECOG_CHOICES = (
        (0, "ECOG 0"),
        (1, "ECOG 1"),
        (2, "ECOG 2"),
        (3, "ECOG 3"),
        (4, "ECOG 4"),
    )
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    value = models.PositiveSmallIntegerField(choices=ECOG_CHOICES)


class BloodType(models.Model):
    BLOOD_TYPE_CHOICES = (
        (0, "A"),
        (1, "B"),
        (2, "AB"),
        (3, "O"),
    )
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    value = models.PositiveSmallIntegerField(choices=BLOOD_TYPE_CHOICES)


class Imaging(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)



class ImageryType(models.Model):
    IMAGING_CHOICES = (
        (0, "CT"),
        (1, "PET"),
        (2, "EBUS"),
        (3, "Other"),
    )
        
    imaging = models.ForeignKey(Imaging, on_delete=models.CASCADE, related_name='types')
    value = models.PositiveSmallIntegerField(choices=IMAGING_CHOICES)