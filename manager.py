import requests 

"""
This class handles manages the interactions between the user and 
the Zendesk API.
"""

class Manager:

    username = ''
    user_in = ''
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

            self.user_in = self.username + "/token" 

            # Establish a connection with the API and verify user credentials by querying job statuses
            r = requests.get('https://zccwright.zendesk.com/api/v2/job_statuses', auth=(self.user_in, self.api_token))

            # Check the status code to verify good connection
            if r.status_code != 200:
                print(f"Problem with connection. Status code: {r.status_code}")
            else:
                print("Connection to API successful")
                self.authenticated = True
        

    # This method displays all tickets currently in the tickets dictionary
    def viewAll(self, tl):
        
        # TODO: Send a request for a paginated ticket base organized in 25-ticket increments
        payload = {"page[size]" : "25"}
        r = requests.get('https://zccwright.zendesk.com/api/v2/tickets', auth=(self.user_in, self.api_token), params=payload)
        response = r.json()

        # TODO: Pass output to formatter to store and print it
        tl.parse_page(response)
        # translator object holds a dictionary of the current 25 tickets on display and formats them to be printed. Recreated with every page transition.

        # TODO: Make a forward/backwards loop controlled by user input

        print("Type - to page back, + to page forward, help for help, quit to exit")
        choice = input(">> ")
        while choice != "quit":
            if choice == '+':
                pass
            elif choice == '-':
                pass
            elif choice == "help":
                pass
            else:
                print("Command not recognized")
                choice = input(">> ")
        print("Returning to menu")
        self.print_menu()
        return



    # This method displays one specifc ticket from the tickets dictionary
    def viewOne(self, tl):
        id = input("Enter the ID of the ticket you want to view: ")
    
    def print_menu(self):
        print("List of commands: ")
        print("1. View all tickets")
        print("2. View an individual ticket")
        print("3. Quit")