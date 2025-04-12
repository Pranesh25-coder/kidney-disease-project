from django import forms

class MedicalRecordForm(forms.Form):
    wc = forms.FloatField(label="White Blood Cell Count")
    bu = forms.FloatField(label="Blood Urea")
    bgr = forms.FloatField(label="Blood Glucose Random")
    sc = forms.FloatField(label="Serum Creatinine")
    pcv = forms.FloatField(label="Packed Cell Volume")
    al = forms.FloatField(label="Albumin")
    hemo = forms.FloatField(label="Hemoglobin")
    age = forms.FloatField(label="Age")
    su = forms.FloatField(label="Sugar")
    htn = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], label="Hypertension")
