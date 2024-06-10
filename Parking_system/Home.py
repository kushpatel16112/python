import mysql.connector
import Parking_Menegment as pm
import Admin as Ad
import sys
from datetime import datetime

class Login:
    def __init__(self):
        try:
            # Establishing connection to the MySQL database
            self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="parking_management")
            if self.connection.is_connected():
                print("Connection is successful")
        except mysql.connector.Error as error:
            print("Failed to connect to MySQL:", error)

    def login(self):
        # Prompting user for ID
        id = input("Enter your id: ")
        if not (self.check_id(id)):
            print("<-----------Enter Valid ID------------>")
            return
        
        # Prompting user for password
        password = input("Enter Your Password: ")
        if not (self.check_password(id, password)):
            print("<-----------Enter Valid Password------------>")
            return
        
        # Checking user's post (Manager or Security)
        post = self.check_post(id)
        if post == "Manager":
            Ad.menu()  # Add Manager functionality here
        else:
            pm.menu()  # Redirect to Parking Management menu for Security staff
    
    def check_password(self, id, password):
        # Create a cursor object to execute SQL queries
        mycursor = self.connection.cursor()
        
        # Define the SQL query to retrieve the password associated with the provided ID
        sql = "SELECT password FROM {} WHERE id = %s".format("staff_info")
        
        # Execute the SQL query with the provided ID as a parameter
        val = (id,)
        mycursor.execute(sql, val)
        
        # Fetch the result of the query (the password)
        slot = mycursor.fetchone()
        
        # Compare the fetched password with the provided password
        if slot[0] == password:
            return True  # Return True if the passwords match
        else:
            return False  # Return False if the passwords do not match


    def check_post(self, id):
        # Create a cursor object to execute SQL queries
        mycursor = self.connection.cursor()
        
        # Define the SQL query to retrieve the post (Manager or Security) associated with the provided ID
        sql = "SELECT Post FROM {} WHERE id = %s".format("staff_info")
        
        # Execute the SQL query with the provided ID as a parameter
        val = (id,)
        mycursor.execute(sql, val)
        
        # Fetch the result of the query (the post)
        slot = mycursor.fetchone()
        
        # Determine the user's post based on the fetched result
        if slot[0] == "Manager":
            return "Manager"  # Return "Manager" if the user is a manager
        elif slot[0] == "Security":
            return "Security"  # Return "Security" if the user is a security staff
        else:
            return "0"  # Return "0" if the user's post is undefined or invalid

    def check_id(self, id):
        # Create a cursor object to execute SQL queries
        mycursor = self.connection.cursor()
        
        # Define the SQL query to retrieve the name associated with the provided ID
        sql = "SELECT name FROM {} WHERE id = %s".format("staff_info")
        
        # Execute the SQL query with the provided ID as a parameter
        val = (id,)
        mycursor.execute(sql, val)
        
        # Fetch the result of the query (the name)
        Sloat = []
        for row in mycursor:
            for field in row:
                Sloat.append(field)
        
        # Check if the name exists (i.e., if the ID is valid)
        if len(Sloat) == 1:
            return True  # Return True if the ID is valid
        else:
            return False  # Return False if the ID is invalid or corresponds to multiple names


def menu():
    # Initialize a flag to control the menu loop
    Flag = True
    
    # Start the menu loop
    while Flag:
        # Display the main menu options
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                                   *")
        print("*       1). Login.                                  *")
        print("*                                                   *")
        print("*       2). Exit System.                            *")
        print("*                                                   *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        
        # Prompt the user to enter an option
        number = int(input("Enter one Option: "))
        
        # Check the user's choice
        if number == 1:
            # Create a Login object and call the login method
            login = Login()
            login.login()
        else:
            # Set the flag to False to exit the loop
            Flag = False
            # Display a farewell message
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
            print("*                                                   *")
            print("*                                                   *")
            print("*                   Thank you                       *")
            print("*         For visit our Parking System              *")
            print("*                                                   *")
            print("*                                                   *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
            sys.exit(1)

if __name__ == "__main__":
    # Display a welcome message when the program starts
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                                   *")
    print("*                                                   *")
    print("*                   Welcome To                      *")
    print("*            Parking Menegment System               *")
    print("*                                                   *")
    print("*                                                   *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    
    # Call the menu function to start the program
    menu()
