import restaurant as resto
import booking as book
import sys

# Function to display the main menu
def menu():
    print("\n\n\n")
    flag = True
    while flag:
        # Displaying the menu options
        print("======================================")
        print("|               MENU                 |")
        print("|====================================|")
        print("|                                    |")
        print("|  1. Press 1 for bookings           |")
        print("|  2. Press 2 for only restaurant    |")
        print("|  3. Press any number for exit      |")
        print("|                                    |")
        print("======================================")
        print("\n\n")
        
        # Prompting user for choice
        n = int(input("~> ENTER YOUR CHOICE : "))
        
        # Checking user choice
        if n == 1:
            book.main()  # Start booking process
        elif n == 2:
            resto.main()  # Start restaurant process
        else:
            flag = False  # Exit loop
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
            print("*                                                   *")
            print("*                                                   *")
            print("*                     Thank you                     *")
            print("*                For visit our hotel                *")
            print("*                                                   *")
            print("*                                                   *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
            sys.exit(1)  # Exit program with status code 1
    
    
if __name__ == "__main__":
    # Displaying welcome message and starting menu
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                                   *")
    print("*                                                   *")
    print("*                    Welcome To                     *")
    print("*              Hotel Menegment System               *")
    print("*                                                   *")
    print("*                                                   *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    menu()

