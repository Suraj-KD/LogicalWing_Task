from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from medicine.models import Medicine_Detail, Medicine_Type

class MedicineType_Form(forms.ModelForm):
    medicine_type = forms.CharField(max_length=40, help_text="Enter type of medicine")
    created = forms.DateTimeField(widget=forms.SelectDateWidget,
                                  help_text="Enter Date of creation")
    modified = forms.DateTimeField(widget=forms.SelectDateWidget,
                                   help_text="Enter Date of modification")
    class Meta:
        model = Medicine_Type
        fields = ('medicine_type', 'created', 'modified')


class MedicineDetail_Form(forms.ModelForm):
    medicine_type = forms.ModelChoiceField(queryset=Medicine_Type.objects.all(),
                                           help_text="Enter Medicine Type")
    name = forms.CharField(max_length=100, help_text="Enter the name of medicine")
    descriptions = forms.CharField(max_length=100, help_text="Enter Medicine Description")
    created = forms.DateTimeField(widget=forms.SelectDateWidget,
                                  help_text="Enter Date of creation")
    modified = forms.DateTimeField(widget=forms.SelectDateWidget,
                                   help_text="Enter Date of modification")
    expired = forms.DateTimeField(widget=forms.SelectDateWidget,
                                  help_text="Enter Date of expiry")
    class Meta:
        model = Medicine_Detail
        fields = ('medicine_type', 'name', 'descriptions', 'created', 'modified', 'expired')

    '''
    def clean(self):
        cleaned_data = self.cleaned_data
        created = cleaned_data.get('created')
        expired = cleaned_data.get('expired')
        if expired <= created:
            raise forms.ValidationError("Expired Date should be after Creation Date")
        return expired
    '''