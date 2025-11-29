from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'expected_participants']
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-solid",
                    "placeholder": "Activity Name"
                }
            ),
            "expected_participants": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-solid",
                    "placeholder": "0",
                }
            ),
        }
