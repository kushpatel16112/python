import mysql.connector
from datetime import datetime
import home as h  # Assuming home.py contains the 'menu' function

class Book:
    def __init__(self):
        # Establish connection to the MySQL database
        self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="Hotel_Menegment")
        if self.connection.is_connected():
            # If connection is successful, proceed to ask for check-in or check-out
            self.ask_Check_IN_OUT()    
        else:
            print("Failed to connect to MySQL:")
    
    # Method to get the current date and time
    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Method to check available rooms of a specific type
    def Check_Available_Room(self, room_type):
        mycursor = self.connection.cursor()
        sql_select = "SELECT Room_No FROM Book WHERE Room_Type = %s and Mobile_no=0"
        mycursor.execute(sql_select, (room_type,))
        available_rooms = [row[0] for row in mycursor.fetchall()]  # Extracting room numbers
        return available_rooms
    
    # Method to get entry data for booking rooms
    def Get_entry_data(self, Quantity, Available_Room):
        name = input("Enter Your Name: ")
        Mobile_no = self.Check_mobile_number()
        Aadhar_no = self.Check_aadhar_number()
        entry_time = self.get_current_time()
        day = int(input("Enter How Many Days Stay in Hotel = "))
        for i in range(Quantity):
            print("Enter extra Bed For Room No ", i)
            Extra_Bed = self.Get_Extra_Bed()
            Room_no = Available_Room[i - 1]
            self.update_entry_data(name, Mobile_no, Aadhar_no, entry_time, day, Extra_Bed, Room_no)
            self.display_entry_receipt(Room_no)
    
    # Method to get extra bed count for a room
    def Get_Extra_Bed(self):
        print("Only Two Extra Bed is Available for one Room ")
        number = int(input("Enter number you want for Extra Bed: "))
        if 0 <= number <= 2:
            return number
        else:
            return self.Get_Extra_Bed()  # Recursively ask for input until valid input is provided
    
    # Method to check mobile number format
    def Check_mobile_number(self):
        while True:
            mobile_number = input("Enter Mobile Number: ")
            if len(mobile_number) == 10 and mobile_number.isdigit():
                return mobile_number
            else:
                print("Enter 10 Digit Mobile Number")
    
    # Method to check Aadhar number format
    def Check_aadhar_number(self):
        while True:
            aadhar_number = input("Enter Aadhar Number: ")
            if len(aadhar_number) == 12 and aadhar_number.isdigit():
                return aadhar_number
            else:
                print("Enter 12 Digit Aadhar card Number")
    
    # Method to update entry data in the database
    def update_entry_data(self, Name, Mobile_no, Aadhar_no, entry_time, day, Extra_Bed, Room_no):
        mycursor = self.connection.cursor()
        sql = "UPDATE Book SET Name=%s,Mobile_no=%s,Aadhar_card_no=%s, Entry_date_time=%s,Day_stay=%s,Extra_bad=%s WHERE Room_no = %s"
        val = (Name, Mobile_no, Aadhar_no, entry_time, day, Extra_Bed, Room_no)
        mycursor.execute(sql, val)
        self.connection.commit()
    
    # Method to display entry receipt for a room
    def display_entry_receipt(self, Room_no):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM Book WHERE Room_No = %s", (Room_no,))
        sloat = mycursor.fetchone()
        if sloat:
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            print("*   Receipt for the Room Entry                                          * ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("*   Room No            : ", sloat[0])
            print("*   Room Type          : ", sloat[1])
            print("*   Room Price         : ", sloat[2])
            print("*   Name               : ", sloat[3])
            print("*   Mobile No          : ", sloat[4])
            print("*   Aadhar No          : ", sloat[5])
            print("*   Enter Date & Time  : ", sloat[6])
            print("*   Day Stay           : ", sloat[8])
            print("*   Extra Bed          : ", sloat[7])
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")
    # Method to prompt for check-in or check-out options
    def ask_Check_IN_OUT(self):
        while True:
            print()
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("*                                                                         *")
            print("*    1) Check In.                                                        *")
            print("*                                                                         *")
            print("*    2) Check Out.                                                       *")
            print("*                                                                         *")
            print("*    3) Return to Main Menu.                                             *")
            print("*                                                                         *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            
            choice = input("Enter one Option: ")
            if choice in ["1"]:
                self.type()  # Proceed with check-in
            elif choice in ["2"]:
                self.get_exit_data()  # Proceed with check-out
            elif choice in ["3"]:
                h.menu()  # Return to main menu
            else:
                print("<-------Enter Valid Option--------->")

    # Method to get data for check-out
    def get_exit_data(self):
        Name = input("Enter your name: ")
        if not (self.check_Name(Name)):
            return
        self.calculate_money(Name)  # Calculate payment for check-out

    # Method to calculate payment for check-out
    def calculate_money(self, Name):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM Book WHERE Name=%s", (Name,))
        rows = mycursor.fetchall()  # Fetch all rows with the given name
        if rows:
            try:
                total_payment = 0
                for row in rows:
                    # Assuming column positions for payment calculation
                    payment = (row[2] * row[8]) + (row[7] * 1000)
                    total_payment += payment
                    self.Display_Check_Out(row)  # Display check-out details
                self.Display_Final_Payment(total_payment)  # Display final payment
                # Update all rows with empty values (assuming you want to clear them)
                mycursor.execute("UPDATE Book SET Name=%s, Mobile_no=%s, Aadhar_card_no=%s, Entry_date_time=%s, Day_stay=%s, Extra_bad=%s WHERE Name = %s",("", "", "", "", "", "", Name))
                self.connection.commit()  # Commit the changes to the database
                h.menu()  # Return to main menu
            except Exception as e:  # Catch specific exceptions if possible
                print("Error:", e)
        else:
            print("No entries found for Name:", Name)

    # Method to display final payment
    def Display_Final_Payment(self, Payment):
        print("\n\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                            Total Payment                                * ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("*                                                                          ")
        print("*   Total Payment      : ", Payment)
        print("*                                                                          ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Method to display check-out details
    def Display_Check_Out(self, Sloat):
        print("\n\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("*                          Particular Room Detail                         * ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("*   Room No            : ", Sloat[0])
        print("*   Room Type          : ", Sloat[1])
        print("*   Room Price         : ", Sloat[2])
        print("*   Name               : ", Sloat[3])
        print("*   Mobile No          : ", Sloat[4])
        print("*   Aadhar No          : ", Sloat[5])
        print("*   Enter Date & Time  : ", Sloat[6])
        print("*   Day Stay           : ", Sloat[8])
        print("*   Extra Bed          : ", Sloat[7])
        print("*   Extra Bed Payment  : ", Sloat[7] * 1000)
        print("*   Total Payment      : ", (Sloat[7] * 1000) + (Sloat[2] * Sloat[8]))
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

    # Method to check if a given name exists in the database
    def check_Name(self, Name):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM Book where Name=%s", (Name,))
        slot = mycursor.fetchone()
        if slot:
            return True
        else:
            print("Enter Valid Name")
            return False

    # Method to select room type for booking
    def type(self): 
        print("=== Which type of room you want to book ===")
        print("1. AC")
        print("2. NON AC")
        choice = input("Enter your choice: ")
        if choice == "1":
            Available_Room = self.Check_Available_Room("AC")
            Quantity = int(input("How many rooms you want: "))
            Total_Quantity = len(Available_Room)
            if Quantity <= Total_Quantity:
                self.Get_entry_data(Quantity, Available_Room)
            else:
                print(Quantity ,"Rooms are not Available only ",Available_Room,"Room are Available")
        elif choice == "2":
            Available_Room = self.Check_Available_Room('Non_AC')
            Quantity = int(input("How many rooms you want: "))
            Total_Quantity = len(Available_Room)
            if Quantity <= Total_Quantity:
                self.Get_entry_data(Quantity, Available_Room)
            else:
                print(Quantity ,"Rooms are not Available only ",Available_Room,"Room are Available")

        else:
            print("Invalid choice!")
            self.type()  # Ask again for a valid choice

# Main function to initiate the program
def main():
    B = Book()  # Instantiate the Book class when the script is executed

# Entry point of the script
if __name__ == "__main__":
    main()

