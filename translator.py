import json

"""
This class serves as a mechanism to transform the responses from 
the Zendesk API from JSON to Python data structures.
"""

class Translator:

    # Organized like {'ticket_id': {ticket}}
    current_page_dict = {}
    
    def __init__(self):
        pass

    # This method takes in the json data from the requests response in manager and translates it into the current_page_dict object
    def parse_page(self, in_json):

        tickets_list = in_json["tickets"]
        for ticket in tickets_list:
            self.current_page_dict.update({ticket["id"] : ticket})

    def print_page(self):
        # TODO: write method that prints the list of 25 tickets.
        pass

    def print_ticket(self):
        # TODO: write method that looks up and prints individual ticket details.
        pass
