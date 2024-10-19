import requests

class ClientIF():
    """
    Client IF: Interface between the client and the Server
    """
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.session = requests.Session()
        self.is_logged_in = False
        print(f"Client IF: base URL: {base_url}")

    def setCookies(self, args):
        pass

    def register(self, args):
        """Register a new account: register <username> <password>"""
        #include basic error handling

        username, password1, password2 = args.split()

        data = {
        'username': username,
        'password1': password1,
        'password2': password2,
        }

        response = self.session.post(f"{self.base_url}/register/", data)
        print(response.json())


    def login(self, args):
        """Login to your account: login <username> <password>"""
        username, password = args.split()
        print(f"****************:::     {self.base_url}/login/")
        response = self.session.post(f"{self.base_url}/login/", data={'username': username, 'password': password})
        if response.status_code == 200:
            self.is_logged_in = True
            print("Logged in successfully.")
        else:
            print("Login failed:", response.json())

    def logout(self, arg):
        """Log out of your account: logout"""
        response = self.session.post(f"{self.base_url}/logout/")
        if response.status_code == 200:
            self.is_logged_in = False
            print("Logged out successfully.")
        else:
            print("Logout failed:", response.json())

    def send(self, args):
        """Send a message to another user: send <username> <message>"""
        if not self.is_logged_in:
            print("You must be logged in to send messages.")
            return

        username, message = args.split(maxsplit=1)
        response = self.session.post(f"{self.base_url}/send-message/", data={'recipient': username, 'message': message})
        print(response.json())

    def senToAll(self, message):
        """Send a message to all connected users: send_to_all <message>"""
        if not self.is_logged_in:
            print("You must be logged in to send messages.")
            return

        response = self.session.post(f"{self.base_url}/send-message-to-all/", data={'message': message})
        print(response.json())

    def receive(self, arg):
        """Receive messages from the server: receive"""
        if not self.is_logged_in:
            print("You must be logged in to receive messages.")
            return

        response = self.session.get(f"{self.base_url}/receive-messages/")
        print(response.json())

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
        'Exit the CLI: exit'
        print("Thank you. Goodbye!")
        return True
