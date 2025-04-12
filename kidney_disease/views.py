
import numpy as np
import joblib
from django.shortcuts import render
from .forms import MedicalRecordForm
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="your_Api_key")
chat = genai.GenerativeModel("gemini-2.0-flash").start_chat()

# Load the scaler and model
scaler = joblib.load("scaler (2).pkl")
model = joblib.load("model.pkl")

def predict_kidney_disease(request):
    if request.method == 'POST':
        try:
            required_fields = ['wc', 'bu', 'bgr', 'sc', 'pcv', 'al', 'hemo', 'age', 'su', 'htn']
            input_data = []

            # Collect input from form
            for field in required_fields:
                value = request.POST.get(field)
                if value is None or value == '':
                    return render(request, 'predictor/result.html', {
                        "error": f"Missing input: {field}",
                        "form": MedicalRecordForm()
                    })
                input_data.append(float(value))

            # Prepare and scale the data
            input_array = np.array([input_data])
            scaled_input = scaler.transform(input_array)

            # Make prediction
            prediction = model.predict(scaled_input)[0]
            probability = float(model.predict_proba(scaled_input)[0][1])  # Probability of CKD

            # Final result logic
            result = "CKD Detected" if probability > 0.5 else "No CKD"

            # Render result
            return render(request, 'predictor/result.html', {
                "result": result,
                "probability": round(probability, 4),
                "form": MedicalRecordForm()
            })

        except ValueError as e:
            return render(request, 'predictor/result.html', {
                "error": f"Invalid input value: {str(e)}",
                "form": MedicalRecordForm()
            })

        except Exception as e:
            return render(request, 'predictor/result.html', {
                "error": f"Unexpected error occurred: {str(e)}",
                "form": MedicalRecordForm()
            })

    # GET request fallback
    return render(request, 'predictor/forms.html', {"form": MedicalRecordForm()})

def chatbot_view(request):
    response = ""
    suggestions = []
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            try:
                # Get response from Gemini
                gemini_response = chat.send_message(
                    f"Provide a concise answer (1-2 short paragraphs max) to this kidney disease question: {user_message} "
                    f"Also suggest 3 short follow-up questions the user might ask. "
                    f"Format the response as: 'ANSWER: [response] SUGGESTIONS: [1] [2] [3]'"
                )
                
                # Process response
                full_response = gemini_response.text
                if "ANSWER:" in full_response and "SUGGESTIONS:" in full_response:
                    response = full_response.split("ANSWER:")[1].split("SUGGESTIONS:")[0].strip()
                    suggestions = [s.strip() for s in full_response.split("SUGGESTIONS:")[1].split("[")[1:]]
                    suggestions = [s.replace("]", "").strip() for s in suggestions if s.strip()]
                else:
                    response = full_response  # fallback if formatting fails
                
            except Exception as e:
                response = f"Sorry, I encountered an error. Please try again."
                suggestions = [
                    "What are common kidney disease symptoms?",
                    "How can I prevent kidney disease?",
                    "What foods are bad for kidneys?"
                ]
    
    return render(request, 'predictor/chatbot.html', {
        "response": response,

    })
