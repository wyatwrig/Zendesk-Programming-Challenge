"""
This class serves as a mechanism to transform the responses from 
the Zendesk API from JSON to Python data structures for easy access and
it also provides the output to the terminal. Holds the current page
state.
"""

class Translator:

    # {'ticket_id': {ticket}}
    current_page_dict = {}
    total_ticket_count = 0
    
    def __init__(self):
        pass

    # takes in the json data from the requests response in manager and translates it into the current_page_dict object
    def parse_page(self, in_json):
        self.current_page_dict.clear()
        tickets_list = in_json["tickets"]
        for ticket in tickets_list:
            self.current_page_dict.update({ticket["id"] : ticket})

    # prints a list of tickets based on the contents of the current_page_dict
    def print_page(self):
        for ticket in self.current_page_dict.values():
            id = ticket["id"]
            status = ticket["status"]
            subject = ticket["subject"]
            priority = ticket["priority"]
            print(f"| {status} ticket {id} with priority {priority} has subject: {subject} |")
        try:
            first = list(self.current_page_dict.keys())[0]
            second = list(self.current_page_dict.keys())[-1]
            print(f"Viewing tickets {first} - {second} of {self.total_ticket_count}")
        except IndexError:
            print("Page in the other direction")

    # prints the ticket details as well as the description for an individual ticket
    def print_ticket(self, ticket_id):
        ticket = self.current_page_dict.get(int(ticket_id))
        try:
            id = ticket["id"]
            status = ticket["status"]
            subject = ticket["subject"]
            priority = ticket["priority"]
            description = ticket["description"]
            print(f"| {status} ticket {id} with priority {priority} has subject: {subject} |")
            print("=============================")
            print(f"Ticket description: {description}")
            print("=============================")
        except TypeError:
            print("Ticket not found.")
            print("Make sure the ticket you're trying to access is on the current page.")

