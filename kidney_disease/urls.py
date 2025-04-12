from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict_kidney_disease, name="predict_kidney_disease"),
    path("chatbot/", views.chatbot_view , name="chatbot"),
    # path("predict/", predict_kidney_disease, name="predict_kidney"),
]
