import manager, translator

def main():

    # TODO: Create REPL loop

    repl = manager.Manager()
    tl = translator.Translator()
    choice = '-1'

    repl.print_menu()
    print("Type help at any time to redisplay the menu")

    choice = input(">> ")

    # TODO: Sanitize input with regex

    while choice != '3':

        # View all tickets
        if choice == '1':
            repl.viewAll(tl)
            choice = input(">> ")

        # View an individual ticket
        elif choice == '2':
            repl.viewOne(tl)
            choice = input(">> ")

        # Help
        elif choice == 'help':
            repl.print_menu()
            choice = input(">> ")

        else:
            print(f"Input: {choice} is not recognized.")
            choice = input(">> ")
    
    print("Exited")

main()        
