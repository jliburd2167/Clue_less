from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    """
    Configuration class for the Authentication app in the Backend.

    This class configures the Authentication module of the Django application,
    setting the default auto field type for models and the name of the application.

    Attributes:
        default_auto_field (str): The type of auto field for models in this app.
        name (str): The full name of the app, used for application identification.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "Backend.Authentication"