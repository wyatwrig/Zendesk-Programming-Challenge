import requests 

"""
This class handles manages the interactions between the user and 
the Zendesk API.
"""

class Manager:
    
    # user info variables

    username = ''
    user_in = ''
    api_token = ''
    web_address = "https://zccwright.zendesk.com" # <-- Change this address to work with other zendesk support profiles. Also update the user_info.txt file.
    authenticated = False

    # pagination variables keep track of current page.
    cursor_next = ''
    cursor_previous = ''

    def __init__(self, tl):
        print("Welcome to the Zendesk CLI ticket viewer")
        self.authenticate()

        # setting up initial page

        # get total tickets
        i = requests.get("https://zccwright.zendesk.com/api/v2/tickets/count", auth=(self.user_in, self.api_token))
        tc_response = i.json()
        ticket_count = int(tc_response["count"]["value"])

        # if tickets > 25, set up for pagination
        if ticket_count > 25:
            payload = {"page[size]" : "25"}
            r = requests.get("https://zccwright.zendesk.com/api/v2/tickets", auth=(self.user_in, self.api_token), params=payload)
            response = r.json()
            self.cursor_next = response["links"]["next"]
            self.cursor_previous = response["links"]["prev"]
            tl.parse_page(response)
            tl.print_page()
        # else, print all tickets
        else:
            r = requests.get("https://zccwright.zendesk.com/api/v2/tickets", auth=(self.user_in, self.api_token))
            response = r.json()
            tl.parse_page(response)
            tl.print_page()
    
    # establishes the user's connection to the API
    def authenticate(self):

        while self.authenticated == False:

            """ 
            This block pulls the email and API token for the user from the user_info.txt file.
            This may be an unnecessary feature but I included it to avoid pushing sensitive info to a 
            public git repo where I'm hosting this project.
            """
            with open("user_info.txt", 'r') as info_file:
                holdinglist = info_file.read().splitlines()
                self.username = holdinglist[0]
                self.api_token = holdinglist[1]

            self.user_in = self.username + "/token" 

            # Establish a connection with the API and verify user credentials by querying job statuses
            r = requests.get("https://zccwright.zendesk.com/api/v2/job_statuses", auth=(self.user_in, self.api_token))

            # Check the status code to verify good connection
            if r.status_code != 200:
                print(f"Problem with connection. Status code: {r.status_code}")
            else:
                print("Connection to API successful")
                self.authenticated = True
        

    # provides pagination functionality
    def page(self, tl, page_token):
        if page_token == '+':
            r = requests.get(self.cursor_next, auth=(self.user_in, self.api_token))
            response = r.json()
            tl.parse_page(response)
            tl.print_page()
            link_forward = response["links"]["next"]
            link_backwards = response["links"]["prev"]
            if link_forward != None:
                self.cursor_next = link_forward
                self.cursor_previous = link_backwards
            else:
                print("End of forwards pagination")
                
        elif page_token == '-':
            r = requests.get(self.cursor_previous, auth=(self.user_in, self.api_token))
            response = r.json()
            tl.parse_page(response)
            tl.print_page()
            link_forward = response["links"]["next"]
            link_backwards = response["links"]["prev"]
            if link_forward != None:
                self.cursor_next = link_forward
                self.cursor_previous = link_backwards
            else:
                print("End of backwards pagination")

        

    # displays one specifc ticket from the tickets dictionary
    def view(self, tl):
        id = input("Enter the ID of the ticket you want to view: ")
        tl.print_ticket(id)
    
    # prints the menu
    def print_menu(self):
        print("List of commands: ")
        print("+ : view next page")
        print("- : view previous page")
        print("view : view specific ticket")
        print("help : display this menu")
        print("quit : exit the program")