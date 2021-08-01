import json

"""
This class serves as a mechanism to transform the responses from 
the Zendesk API from JSON to Python data structures for easy access and
it also provides the output to the terminal.
"""

class Translator:

    # {'ticket_id': {ticket}}
    current_page_dict = {}
    
    def __init__(self):
        pass

    # takes in the json data from the requests response in manager and translates it into the current_page_dict object
    def parse_page(self, in_json):
        self.current_page_dict.clear()
        tickets_list = in_json["tickets"]
        for ticket in tickets_list:
            self.current_page_dict.update({ticket["id"] : ticket})

    # prints the current page based on the contents of the current_page_dict
    def print_page(self):
        for ticket in self.current_page_dict.values():
            id = ticket["id"]
            status = ticket["status"]
            subject = ticket["subject"]
            priority = ticket["priority"]
            print(f"{status} ticket {id} with priority {priority} has subject: {subject}")

    # prints the ticket details as well as the description for an individual ticket
    def print_ticket(self, ticket_id):
        ticket = self.current_page_dict.get(int(ticket_id))
        id = ticket["id"]
        status = ticket["status"]
        subject = ticket["subject"]
        priority = ticket["priority"]
        description = ticket["description"]
        print(f"{status} ticket {id} with priority {priority} has subject: {subject}")
        print(f"Ticket description: {description}")
