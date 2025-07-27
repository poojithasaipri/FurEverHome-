from django import forms
from .models import AdoptionRequest

from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'description', 'image']


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = [
            "full_name", "email", "phone",
            "address_line1", "address_line2",
            "city", "state", "pincode",
            "message"
        ]

        

