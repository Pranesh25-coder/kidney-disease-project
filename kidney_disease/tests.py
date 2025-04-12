# from django.test import TestCase

# import numpy as np
# import joblib

# # Load model and scaler
# model = joblib.load("model.pkl")
# scaler = joblib.load("scaler (2).pkl")

# # # CKD case input
# # input_data = np.array([[7800, 54.0, 145.0, 3.2, 33.0, 2.0, 10.2, 56, 1.0, 1]])
# # input_scaled = scaler.transform(input_data)

# # # Predict
# # pred = model.predict(input_scaled)
# # prob = model.predict_proba(input_scaled)[0][1]  # Probability of CKD

# # print("Prediction:", "CKD" if pred[0] == 1 else "No CKD")
# # print("Probability of CKD:", prob)
# # Non-CKD case input (normal range values)
# # CKD case (with abnormal values)
# input_data = np.array([[7200,   # wc (white blood cell count)
#                         56.0,   # bu (blood urea)
#                         160.0,  # bgr (blood glucose random)
#                         3.6,    # sc (serum creatinine)
#                         30.0,   # pcv (packed cell volume)
#                         2.0,    # al (albumin)
#                         9.5,    # hemo (hemoglobin)
#                         65,     # age
#                         2.0,    # su (sugar)
#                         1       # htn (hypertension)
#                        ]])

# # Scale the input
# input_scaled = scaler.transform(input_data)

# # Predict
# pred = model.predict(input_scaled)
# prob = model.predict_proba(input_scaled)[0][1]

# # Output
# print("Prediction:", "CKD" if pred[0] == 1 else "No CKD")
# print("Probability of CKD:", round(prob, 4))

import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCojMDHvo5C3L8VD4fYmFJNJlH4CJ3HyeAre"
