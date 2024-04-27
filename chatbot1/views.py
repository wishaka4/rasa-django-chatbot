# views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        rasa_response = send_message_to_rasa(user_message)
        return JsonResponse({'response': rasa_response})
    else:
        return render(request, 'chat.html')

def send_message_to_rasa(message):
    #rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    rasa_url = "http://127.0.0.1:5005/webhooks/rest/webhook"
    
    data = {"sender": "user", "message": message}
    response = requests.post(rasa_url, json=data)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to communicate with Rasa server.'}
