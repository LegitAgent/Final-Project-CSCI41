from django import forms
from django.contrib.auth.models import User
from .models import Organizer, Participant
from django.core.exceptions import ValidationError


class OrganizerForm(forms.ModelForm):
    id_number = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "ID Number"
        }
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Organizer Name"
        }
    ))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Password"
        }
    ))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Confirm Password"
        }
    ))

    class Meta:
        model = Organizer
        exclude = ["user", "address", "contact_name",
                   "contact_email", "contact_number"]
        widgets = {
            "organizer_type": forms.Select(
                attrs={
                    "class": "form-select",
                    "data-control": "select2",
                    "data-placeholder": "Organizer Type",
                    "data-hide-search": "true"
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def clean_id_number(self):
        id_number = self.cleaned_data.get("id_number")
        if User.objects.filter(username=id_number).exists():
            raise forms.ValidationError(
                "A user with this ID number already exists.")
        return id_number


class ParticipantForm(forms.ModelForm):
    id_number = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "ID Number",
            "required": ""
        }
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Full Name"
        }
    ))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Password",
            "required": ""
        }
    ))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control bg-transparent",
            "placeholder": "Confirm Password",
            "required": ""
        }
    ))

    class Meta:
        model = Participant
        exclude = ["user"]
        widgets = {
            "department": forms.TextInput(
                attrs={
                    "class": "form-control bg-transparent",
                    "placeholder": "Department"
                }
            ), 
            "birthdate": forms.DateInput(attrs={
                "type": "hidden",
                "placeholder": "Select your birthdate"
            }),
            "participant_type": forms.Select(
                attrs={
                    "class": "form-select",
                    "data-control": "select2",
                    "data-placeholder": "Participant Type",
                    "data-hide-search": "true"
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def clean_id_number(self):
        id_number = self.cleaned_data.get("id_number")
        if User.objects.filter(username=id_number).exists():
            raise forms.ValidationError(
                "A user with this ID number already exists.")
        return id_number
