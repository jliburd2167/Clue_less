import cmd
import ClientIF

class cmdClientIF(cmd.Cmd):

    intro = """
      ####### ##        ##      ##  ########
     ##       ##        ##      ##  ##
    ##        ##        ##      ##  ##
    ##        ##        ##      ##  #####
    ##        ##        ##      ##  ##
     ##       ##        ##      ##  ##
      ####### ######### ##########  ########

    Welcome to team Elemnt Edge's Clueless - CLI
        Type help or ? to list commands"""
    prompt = "(cli-Clueless) "

    def __init__(self, base_url):
        super().__init__()
        self.client = ClientIF.ClientIF(base_url)

    def do_register(self, args):
        """Register a new account: register <username> <password> <re-enter Password>"""
        self.client.register(args)

    def do_login(self, args):
        """Login to your account: login <username> <password>"""
        self.client.login(args)

    def do_logout(self, arg):
        """Log out of your account: logout"""
        self.client.logout(arg)

    def do_send(self, message):
        """Send a message to another user: send <username> <message>"""
        self.client.send(message)

    def do_senToAll(self, message):
        """Send a message to all connected users: send_to_all <message>"""
        self.client.senToAll(message)

    def do_receive(self, arg):
        """Receive messages from the server: receive"""
        self.client.receive(arg)

    def do_joinGameRequest(self, arg):
        pass

    def do_startGameRequest(self, arg):
        pass

    def do_playerMove(self, arg):
        pass

    def do_makeSuggestion(self, arg):
        pass

    def do_makeAccusation(self, arg):
        pass

    def do_EndTurn(self, arg):
        pass

    def do_EndGameEarlyRequest(self, arg):
        pass

    def do_exit(self, arg):
        'Exit the CLI: exit'
        print("Thank you. Goodbye!")
        return True

if __name__ == '__main__':
    SERVER_URL = "http://127.0.0.1:8000/"
    cli = cmdClientIF(SERVER_URL)  # Adjust the base URL as needed
    cli.cmdloop()