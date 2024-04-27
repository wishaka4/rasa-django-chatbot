from django.urls import path
from .views import chat  # Import the chatbot view function

urlpatterns = [
    # path('chat/', chatbot, name='chatbot'),  # Use the chatbot view function without calling it
    path('chat/', chat, name='chat'),
]