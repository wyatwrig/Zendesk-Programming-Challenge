import requests 
import sys

"""
This class handles manages the interactions between the user and 
the Zendesk API.
"""

class Manager:
    
    # user info variables

    username = ""
    user_in = ""
    api_token = ""
    web_address = "" 
    authenticated = False

    # pagination variables keep track of current page.
    cursor_next = ''
    cursor_previous = ''

    def __init__(self, tl):
        print("Welcome to the Zendesk CLI ticket viewer")
        
        """ 
            This block pulls the email and API token for the user from the user_info.txt file.
            This may be an unnecessary feature but I included it to avoid pushing sensitive info to a 
            public git repo where I'm hosting this project.
            """
        if self.authenticated == False:
            try:
                with open("user_info.txt", 'r') as info_file:
                    holdinglist = info_file.read().splitlines()
                    self.username = holdinglist[0]
                    self.api_token = holdinglist[1]
                    self.web_address = holdinglist[2]

                self.user_in = self.username + "/token"
                self.authenticated = True
            except OSError as e:
                print("File user_info.txt not found")
                print("Ensure file exists and re-run program")
                sys.exit()

        # setting up initial page
        ticket_count = self.get_count()
        tl.total_ticket_count = ticket_count
        

        # if tickets > 25, set up for pagination
        if ticket_count > 25:
            payload = {"page[size]" : "25"}
            response = self.query_api(f"{self.web_address}/api/v2/tickets", self.user_in, self.api_token, payload)
            self.update_cursors(response["links"]["next"], response["links"]["prev"])
            tl.parse_page(response)
            tl.print_page()
        # else, print all tickets
        else:
            response = self.query_api(f"{self.web_address}/api/v2/tickets", self.user_in, self.api_token)
            tl.parse_page(response)
            tl.print_page()
       

    # provides pagination functionality
    def page(self, tl, page_token):
        if page_token == '+':
            response = self.query_api(self.cursor_next, self.user_in, self.api_token)
            tl.parse_page(response)
            tl.print_page()
            self.update_cursors(response["links"]["next"], response["links"]["prev"])
                
        elif page_token == '-':
            response = self.query_api(self.cursor_previous, self.user_in, self.api_token)
            tl.parse_page(response)
            tl.print_page()
            self.update_cursors(response["links"]["next"], response["links"]["prev"])
    
    def get_count(self):
        # get total tickets
        try:
            i = requests.get(f"{self.web_address}/api/v2/tickets/count", auth=(self.user_in, self.api_token))
            if i.status_code != 200:
                print("Problem contacting Zendesk API")
                print(f"Response Status: {i.status_code}")
                error = i.json()["error"]
                print(f"Error response from Zendesk: {error}")
                sys.exit()
            tc_response = i.json()
            ticket_count = int(tc_response["count"]["value"])
            return ticket_count
        except requests.exceptions.RequestException as e:
            print("Encountered a problem with your internet connection")
            print("Ensure connection and re-run program")
            sys.exit()


    def query_api(self, url, user_in, api_token, payload = None):
        try:
            r = requests.get(url, auth=(user_in, api_token), params=payload)
            if r.status_code != 200:
                print("Problem contacting Zendesk API")
                print(f"Response Status: {r.status_code}")
                error = r.json()["error"]
                print(f"Error response from Zendesk: {error}")
                sys.exit()
            response = r.json() 
            return response
        except requests.exceptions.RequestException as e:
            print("Encountered a problem with your internet connection")
            print("Ensure connection and re-run program")
            sys.exit()

    def update_cursors(self, forwards, backwards):
        if forwards and backwards != None:
            self.cursor_next = forwards
            self.cursor_previous = backwards
        else:
            print("Can't page beyond bounds")
        

    # displays one specifc ticket from the tickets dictionary
    def view(self, tl):
        id = input("Enter the ID of the ticket you want to view: ")
        tl.print_ticket(id)
    
    # prints the menu
    def print_menu(self):
        print("=============================")
        print("List of commands: ")
        print("+ : view next page")
        print("- : view previous page")
        print("view : view specific ticket")
        print("help : display this menu")
        print("quit : exit the program")
        print("=============================")