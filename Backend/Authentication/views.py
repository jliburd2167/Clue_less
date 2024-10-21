# backend/authentication/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token


class RegisterView(View):
    """
    View for handling user registration.

    This view allows new users to register by submitting a username and password.
    It uses Django's built-in UserCreationForm for validation and user creation.

    Methods:
        post(request): Handles user registration via POST request.
        get(request): Returns a CSRF token for secure form submissions.
    """

    def post(self, request) -> JsonResponse:
        """
        Handle user registration via POST request.

        Args:
            request: The HTTP request object containing registration data.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """
        form = UserCreationForm(request.POST)  # Create a form instance with POST data

        if form.is_valid():
            user = form.save()  # Save the new user
            return JsonResponse({'message': 'User created successfully'}, status=201)

        # If the form is not valid display and return errors
        print(f"Errors: {form.errors}")  # Debug message
        return JsonResponse({'errors': form.errors}, status=400)

    def get(self, request) -> JsonResponse:
        """
        Return a CSRF token for secure form submissions.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response containing the CSRF token.
        """
        csrf_token = get_token(request)  # Generate CSRF token
        return JsonResponse({'csrfToken': csrf_token})  # Return token


class LoginView(View):
    """
    View for handling user login.

    This view authenticates users and logs them in if valid credentials are provided.

    Methods:
        post(request): Handles user login via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handle user login via POST request.

        Args:
            request: The HTTP request object containing login credentials.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """
        # Get Username and password from database POST get request
        username = request.POST.get('username')
        password = request.POST.get('password')

          # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log user in

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

        return JsonResponse({'error': 'Invalid credentials'}, status=403)  # Return error for invalid credentials



class LogoutView(View):
    """
    View for handling user logout.

    This view logs out the currently authenticated user.

    Methods:
        post(request): Handles user logout via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handle user logout via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating successful logout.
        """

        logout(request)  # Log the user out
        return JsonResponse({'message': 'Logged out successfully'}, status=200)  # Return success message