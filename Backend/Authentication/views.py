# backend/authentication/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token


class RegisterView(View):
    def post(self, request):
        print("performing user creatuib form")
        form = UserCreationForm(request.POST)
        print("is valid?!?")
        if form.is_valid():
            print("User is not valid?")
            user = form.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
        print(f"JAMARRRR'errors': {form.errors} jayyy")
        return JsonResponse({'errors': form.errors}, status=400)

    def get(self, request):
        print("***************************Getting the csrfToken")
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

class LoginView(View):
    def post(self, request):
        print("user name request?")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Notify all clients of the new login
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    'type': 'notify',
                    'message': f"{user.username} has logged in.",
                }
            )

            return JsonResponse({'message': 'Logged in successfully'}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=403)

class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'}, status=200)
