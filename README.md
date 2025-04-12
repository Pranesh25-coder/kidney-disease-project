🩺 Kidney Disease Predictor + Gemini Chatbot (Django App)
This project is a web-based application built using Django that predicts the presence of Chronic Kidney Disease (CKD) based on medical inputs and provides an AI-powered chatbot for answering kidney-related health queries using Gemini (Google Generative AI).
📌 Features
🧠 CKD Prediction using a pre-trained ML model (model.pkl) and scaler (scaler.pkl)

🩻 Form-based input for relevant clinical parameters

💬 Gemini Chatbot for answering kidney-related questions

🔐 Form validation and error handling

📊 CKD probability score with a clear diagnosis result

📁 Project Structure
    graphql
    
    kidney_disease_project/
    │
    ├── predictor/
    │   ├── views.py           # Prediction logic & Gemini chatbot integration
    │   ├── forms.py           # MedicalRecordForm for input validation
    │   ├── templates/
    │   │   ├── forms.html     # Input form
    │   │   ├── result.html    # Prediction result
    │   │   └── chatbot.html   # Chatbot UI
    ├── model.pkl              # Trained machine learning model
    ├── scaler (2).pkl         # Scaler used for preprocessing input data
    ├── manage.py              # Django management file
    └── README.md              # This file
⚙️ Setup Instructions
1. Clone the repo and move into the project folder:
bash
Copy
Edit
git clone <your_repo_url>
cd kidney_disease_project
2. Create a virtual environment and activate it:
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies:
bash

pip install -r requirements.txt
4. Make migrations and start the server:

bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

🧪 Required Inputs for Prediction
The following clinical values must be provided via the form:

wc - White Blood Cell count

bu - Blood Urea

bgr - Blood Glucose Random

sc - Serum Creatinine

pcv - Packed Cell Volume

al - Albumin

hemo - Hemoglobin

age - Age

su - Sugar

htn - Hypertension

💬 Chatbot Functionality
Powered by Gemini (Google Generative AI).

Handles kidney-related questions.

Provides a brief answer and 3 related follow-up question suggestions.

To use Gemini:

Make sure your Gemini API Key is valid and correctly set in views.py:

python

Edit
genai.configure(api_key="YOUR_GEMINI_API_KEY")
🛡️ Notes
Make sure model.pkl and scaler (2).pkl are in the project root.

Never commit your Gemini API key to public repositories.

For production, consider .env files for secure key management.

🧠 Example Usage
Visit http://127.0.0.1:8000/

Enter medical values to get CKD prediction.

Open the chatbot to ask questions like:

"What are early symptoms of kidney disease?"

"Can CKD be cured?"

