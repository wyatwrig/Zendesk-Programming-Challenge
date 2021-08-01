import manager, translator

def main():

    tl = translator.Translator()
    repl = manager.Manager(tl)
    
    choice = '-1'

    repl.print_menu()
    print("Type help at any time to redisplay the menu")

    choice = input(">> ")

    # TODO: Sanitize input with regex

    while choice != 'quit':

        # page forward
        if choice == '+':
            repl.page(tl, '+')
            repl.print_menu()
            choice = input(">> ")

        # page backwards
        elif choice == '-':
            repl.page(tl, '-')
            repl.print_menu()
            choice = input(">> ")

        # help
        elif choice == 'help':
            repl.print_menu()
            choice = input(">> ")
        
        # view individual ticket details
        elif choice == 'view':
            repl.view(tl)
            repl.print_menu()
            choice = input(">> ")

        else:
            print(f"Input: {choice} is not recognized.")
            choice = input(">> ")
    
    print("Exited")

main()        
