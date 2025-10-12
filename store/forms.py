from django import forms
from django.contrib.auth.models import User
from datetime import date
from .models import Perfil

class ProfileForm(forms.ModelForm):
    # Campos del modelo User
    first_name = forms.CharField(label="Nombre", required=False)
    last_name  = forms.CharField(label="Apellido", required=False)
    email      = forms.EmailField(label="Correo", required=True)

    # Campos del modelo Perfil
    telefono = forms.CharField(label="Teléfono", required=False)
    direccion = forms.CharField(label="Dirección", required=False)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Perfil
        fields = ['first_name', 'last_name', 'email', 'telefono', 'direccion', 'fecha_nacimiento']
        field_order = ['first_name', 'last_name', 'email', 'telefono', 'direccion', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # Inicializar campos del modelo User
        self.fields['first_name'].initial = self.user.first_name
        self.fields['last_name'].initial  = self.user.last_name
        self.fields['email'].initial      = self.user.email

        # Aplicar estilo uniforme
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("Este correo ya está registrado por otro usuario.")
        return email

    def clean_fecha_nacimiento(self):
        fn = self.cleaned_data.get('fecha_nacimiento')
        if fn:
            hoy = date.today()
            edad = hoy.year - fn.year - ((hoy.month, hoy.day) < (fn.month, fn.day))
            if edad < 13:
                raise forms.ValidationError("Debes tener al menos 13 años.")
        return fn

    def save(self, commit=True):
        perfil = super().save(commit=False)
        self.user.first_name = self.cleaned_data.get('first_name', '')
        self.user.last_name  = self.cleaned_data.get('last_name', '')
        self.user.email      = self.cleaned_data.get('email', '')
        if commit:
            self.user.save()
            perfil.user = self.user
            perfil.save()
        return perfil