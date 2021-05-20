from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateForm(forms.Form):
    job_id = forms.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(20)
        ]
    )