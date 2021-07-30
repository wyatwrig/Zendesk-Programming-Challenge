import requests
import base64

"""
This module handles manages the interactions between the user and 
the Zendesk API.
"""

class Manager:

    tickets = []
    username = ''
    api_token = ''
    web_address = "https://zccwright.zendesk.com"
    authenticated = False

    def __init__(self):
        print("Welcome to the Zendesk CLI ticket viewer")
        self.authenticate()
    
    # This method establishes the user's connection to the API
    def authenticate(self):

        while self.authenticated == False:

            """ 
            This block pulls the email and API token for the user from the user_info.txt file.
            This may be an unnecessary feature but I included it to avoid pushing sensitive info to a 
            public git repo where I'm hosting this project.
            """
            with open('user_info.txt', 'r') as info_file:
                holdinglist = info_file.read().splitlines()
                self.username = holdinglist[0]
                self.api_token = holdinglist[1]

            user_in = self.username + "/token" 

            # Establish a connection with the API and verify user credentials by querying job statuses
            r = requests.get('https://zccwright.zendesk.com/api/v2/job_statuses', auth=(user_in, self.api_token))

            # Check the status code to verify good connection
            if r.status_code != 200:
                print(f"Problem with connection. Status code: {r.status_code}")
            else:
                print("Connection Successful")
                self.authenticated = True
        


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
        print("4. Quit")