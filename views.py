import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render
from django import forms
from django.conf import settings
from django.http import JsonResponse

# Load the trained model, scaler, and training means
model = joblib.load(str(settings.BASE_DIR / "kidney_model.pkl"))
scaler = joblib.load(str(settings.BASE_DIR / "scaler.pkl"))
training_means = joblib.load(str(settings.BASE_DIR / "training_means.pkl"))

# Define the form for user input (collecting 9 features)
class MedicalRecordForm(forms.Form):
    age = forms.FloatField(label="Age")
    bmi = forms.FloatField(label="BMI")
    systolic_bp = forms.FloatField(label="Systolic Blood Pressure")
    diastolic_bp = forms.FloatField(label="Diastolic Blood Pressure")
    fasting_blood_sugar = forms.FloatField(label="Fasting Blood Sugar")
    serum_creatinine = forms.FloatField(label="Serum Creatinine")
    gfr = forms.FloatField(label="Glomerular Filtration Rate")
    protein_in_urine = forms.FloatField(label="Protein in Urine")
    hemoglobin_levels = forms.FloatField(label="Hemoglobin Levels")

def predict_kidney_disease(request):
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            try:
                # Extract input data from the form (9 features)
                input_features = list(form.cleaned_data.values())

                # Get the number of features expected by the scaler (should be 24)
                expected_features = scaler.n_features_in_  # This should be 24

                # If less than expected, fill missing features with training means
                if len(input_features) < expected_features:
                    missing_count = expected_features - len(input_features)
                    # Use the training means for the missing features:
                    input_features.extend(training_means[len(input_features):len(input_features) + missing_count])

                # Convert the list to a NumPy array and reshape for prediction
                input_array = np.array(input_features).reshape(1, -1)
                
                # Convert to DataFrame with appropriate feature names
                # Assuming scaler was fitted on a DataFrame, use its feature names:
                feature_names = scaler.feature_names_in_
                input_df = pd.DataFrame(input_array, columns=feature_names)
                
                # Scale the input data
                scaled_features = scaler.transform(input_df)
                prediction = model.predict(scaled_features)[0]

                return render(request, "predictor/result.html", {"prediction": prediction})

            except Exception as e:
                return JsonResponse({"error": str(e)})
    else:
        form = MedicalRecordForm()

    return render(request, "predictor/form.html", {"form": form})
