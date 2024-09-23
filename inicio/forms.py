from django import forms 
from .models import ResponsableVenta,VentasRealizadas

class FormResponsableVenta(forms.ModelForm):
    class Meta:
        model = ResponsableVenta
        fields = ('nombre',)


