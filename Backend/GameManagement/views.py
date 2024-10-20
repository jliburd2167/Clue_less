from django.views import View
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class GameView(View):
        def post(self, request):
            # Logic to start a new game or join an existing one
            pass

        def get(self, request, game_id):
            # Logic to retrieve game state
              pass

class CreateGameView(View):
    """
    View for handling a player to create a game.

    This view allows users to create game lobbies.

    Methods:
        post(request): Handles creating game lobbies via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handles creating game lobbies via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """

        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB

        return JsonResponse({'message': 'This is a stub for the command "create_game".'}, status=200)

class JoinGameView(View):
    """
    View for handling player joining games.

    This view allows users to join game lobbies.

    Methods:
        post(request): Handles joining game lobbies via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handles joining game lobbies via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """

        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB

        return JsonResponse({'message': 'This is a stub for the command "join_game <key>".'}, status=200)
    
class LeaveGameView(View):
    """
    View for handling player leaving a game.

    This view allows users to leave game lobbies.

    Methods:
        post(request): Handles leaving game lobbies via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handles leaving game lobbies via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """

        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB

        return JsonResponse({'message': 'This is a stub for the command "leave_game".'}, status=200)
    
class StartGameView(View):
    """
    View for handling player starting a game.

    This view allows users to start games.

    Methods:
        post(request): Handles start games via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handles starting games via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """

        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB

        return JsonResponse({'message': 'This is a stub for the command "start_game".'}, status=200)
    
class ChooseCharacterView(View):
    """
    View for choosing a character.

    This view allows users to choose character.

    Methods:
        post(request): Handles choosing character via POST request.
    """

    def post(self, request) -> JsonResponse:
        """
        Handles choosing characters via POST request.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating success or failure.
        """

        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB
        # TODO: THIS IS A STUB

        return JsonResponse({'message': 'This is a stub for the command "choose_character".'}, status=200)