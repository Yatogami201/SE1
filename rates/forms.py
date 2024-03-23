from django import forms
from rates.models import Service, Rate

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['rate_type', 'user', 'rate_amount', 'service']