import manager, formatter, ticket

def main():

    # TODO: Create REPL loop

    repl = manager.Manager()
    choice = '-1'

    repl.print_menu()
    print("Type help at any time to redisplay the menu")

    choice = input("Enter a number: ")

    # TODO: Sanitize input with regex

    while choice != '4':

        # View all tickets
        if choice == '1':
            pass

        # View an individual ticket
        if choice == '2':
            pass

        # Refresh tickets
        if choice == '3':
            pass

        # Help
        if choice == 'help':
            repl.print_menu()
            choice = input("Enter a number: ")
    
    print("Exited")

main()        
