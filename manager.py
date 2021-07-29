import requests
import base64

"""
This module handles manages the interactions between the user and 
the Zendesk API through a repl format. Holds a list of ticket objects.
"""

class Manager:

    tickets = []
    username = ''
    api_token = ''
    web_address = "https://zccwright.zendesk.com/"
    authenticated = False

    def __init__(self):
        print("Welcome to the Zendesk CLI ticket viewer")
        self.authenticate()
    
    # This method establishes the user's connection to the API
    def authenticate(self):

        # TODO: Add regex to sanitize user input
        while self.authenticated == False:
            # TODO: Implement an authorization method that pulls username/password/API token from a file.

            # Creating request object & adding authorization header
            user_in = self.username + ":" + self.password
            header = {"Authorization" : "Basic " + base64.b64encode(user_in)}

            r = requests.get()


    # This method refreshes the dictionary of tickets by querying the API
    def query_tickets(self):
        pass

    # This method displays all tickets currently in the tickets dictionary
    def viewAll(self):
        pass

    # This method displays one specifc ticket from the tickets dictionary
    def viewOne(self):
        pass
    
    def print_menu(self):
        print("List of commands: ")
        print("1. View all tickets")
        print("2. View an individual ticket")
        print("3. Refresh tickets")
        print("4. Menu")
        print("5. Quit")