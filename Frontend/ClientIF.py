import requests

class ClientIF():
    """
    Client Interface: Interface between the client and the server.

    This class provides methods for the Authentication, Game Management,
    and Message Translator subsystems and interacting with the server for game-related functionalities.

    Attributes:
        base_url (str): The base URL of the server.
        session (requests.Session): The HTTP session used for making requests.
        is_logged_in (bool): A flag indicating whether the user is logged in.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initialize the ClientIF with the base URL.

        Args:
            base_url (str): The base URL of the server.
        """
        self.base_url = base_url
        self.session = requests.Session()  # Create a session for persistent connections
        self.is_logged_in = False  # Track login status
        print(f"Client IF: base URL: {base_url}")

    def setCookies(self, args: str) -> None:
        """
        Set cookies for the session (to be implemented).
        """
        # TODO: Implement cookie handling
        pass

    def register(self, args: str) -> None:
        """
        Register a new account with the provided username and passwords.

        Args:
            args (str): A string containing username, password1, and password2.

        Raises:
            ValueError: If the input format is incorrect or registration fails.
        """
        try:
            username, password1, password2 = args.split()
            data = {
                'username': username,
                'password1': password1,
                'password2': password2,
            }

            response = self.session.post(f"{self.base_url}/register/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except ValueError:
            print("Error: Please provide username, password1, and password2.")
        except requests.RequestException as e:
            print(f"Registration failed: {e}")

    def login(self, args: str) -> None:
        """
        Log in to the account using the provided username and password.

        Args:
            args (str): A string containing username and password.

        Raises:
            ValueError: If the input format is incorrect.
        """
        try:
            username, password = args.split()
            response = self.session.post(f"{self.base_url}/login/", data={'username': username, 'password': password})
            response.raise_for_status()  # Raise an error for bad responses

            self.is_logged_in = True
            print("Logged in successfully.")

        except ValueError:
            print("Error: Please provide both username and password.")
        except requests.RequestException as e:
            print(f"Login failed: {e}")

    def logout(self) -> None:
        """
        Log out of the current account.

        Raises:
            requests.RequestException: If the logout request fails.
        """
        response = self.session.post(f"{self.base_url}/logout/")
        try:
            response.raise_for_status()  # Raise an error for bad responses
            self.is_logged_in = False
            print("Logged out successfully.")
        except requests.RequestException as e:
            print(f"Logout failed: {e}")

    def send(self, args: str) -> None:
        """
        Send a message to another user.

        Args:
            args (str): A string containing the recipient's username and the message.

        Raises:
            ValueError: If the user is not logged in or input format is incorrect.
        """
        if not self.is_logged_in:
            print("You must be logged in to send messages.")
            return

        try:
            username, message = args.split(maxsplit=1)
            response = self.session.post(f"{self.base_url}/send-message/", data={'recipient': username, 'message': message})
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())
        except ValueError:
            print("Error: Please provide both username and message.")
        except requests.RequestException as e:
            print(f"Failed to send message: {e}")

    def joinGameRequest(self, arg):
        pass

    def startGameRequest(self, arg):
        pass

    def playerMove(self, arg):
        pass

    def makeSuggestion(self, arg):
        pass

    def makeAccusation(self, arg):
        pass

    def EndTurn(self, arg):
        pass

    def EndGameEarlyRequest(self, arg):
        pass

    def exit(self, arg):
        """
        Exit the CLI.

        Args:
            arg (str): Command to exit.

        Returns:
            bool: Always returns True to indicate exit.
        """
        print("Thank you. Goodbye!")
        return True