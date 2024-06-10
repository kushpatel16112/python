import mysql.connector
from datetime import datetime
from datetime import date
import Home as home

class ParkingSystem:
    def __init__(self):
        try:
            # Attempt to establish a connection to the MySQL database
            self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="parking_management")
            
            # Check if the connection is successful
            if self.connection.is_connected():
                pass  # If successful, do nothing (optionally, print a success message)
                # print("Connection is successful")
                # print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
                # print("*                                                   *")
                # print("*                                                   *")
                # print("*                   Welcome To                      *")
                # print("*            Parking Menegment System               *")
                # print("*                                                   *")
                # print("*                                                   *")
                # print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        except mysql.connector.Error as error:
            # If connection fails, print an error message
            print("Failed to connect to MySQL:", error)


    def ask_car_entry_exit(self):
        # Start a loop to repeatedly ask for the car entry/exit option
        while True:
            # Display the menu options for car entry/exit
            print()
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("*                                                                         *")
            print("*    1).Vehicle is Enter.                                                     *")
            print("*                                                                         *")
            print("*    2).Vehicle is Exit.                                                      *")
            print("*                                                                         *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            # Prompt the user to enter an option
            choice = input("Enter one Option: ")
            
            # Check the user's choice
            if choice in ["1"]:
                # If the user chooses option 1, return "1" indicating car entry
                return "1"
            elif choice in ["2"]:
                # If the user chooses option 2, return "2" indicating car exit
                return "2"
            else:
                # If the user enters an invalid option, display an error message
                print("<-------Enter Valid Option--------->")


    def display_entry_receipt(self, block_number, car_number, mobile_number, entry_time, slot_number):
        # Display the receipt for vehicle entry in parking slot
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*   Receipt for the Vehicle Entry in Parking Slot                         * ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("*   Block No           : ", block_number)
        print("*   Car No             : ", car_number)
        print("*   Mobile No          : ", mobile_number)
        print("*   Slot No            : ", slot_number)
        print("*   Enter Date & Time  : ", entry_time)
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        # Call the method to update entry data in the database
        self.update_entry_data(block_number, car_number, mobile_number, entry_time, slot_number)


    def display_exit_receipt(self, block_number, car_number):
        # Retrieve parking slot details for the given car number from the specified block
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM {} WHERE car_number=%s LIMIT 1".format(block_number), (car_number,))
        Sloat = []

        # Extract details from the fetched row
        for row in mycursor:
            for field in row:
                Sloat.append(str(field))

        # Display the receipt for vehicle exit in parking slot
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*   Receipt for the Vehicle Exit in Parking Slot                          * ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("*   Block No           : ", block_number)
        print("*   Car No             : ", Sloat[1])
        print("*   Mobile No          : ", Sloat[2])
        print("*   Slot No            : ", Sloat[0])
        print("*   Enter Date & Time  : ", Sloat[3])
        print("*   Exit Date & Time   : ", Sloat[4])
        print("*   Difference of Time : ", Sloat[5])
        print("*   Payment            : ", Sloat[6])
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        # Update history with exit details
        self.Update_Histry(block_number, Sloat)

        # Update cash records with the payment amount
    def update_cash(self, payment):
        mycursor = self.connection.cursor()
        
        # Get today's date components
        todays_date = date.today()
        current_year = todays_date.year
        current_month = todays_date.month
        current_day = todays_date.day
        
        flag = True
        while flag:
            # Check if there is a record for today's date
            sql_select = "SELECT payment FROM cash_records WHERE year=%s AND month=%s AND day=%s"
            mycursor.execute(sql_select, (current_year, current_month, current_day))
            myresult = mycursor.fetchone()
            
            if myresult:
                # If a record exists, update the payment amount
                updated_payment = myresult[0] + payment
                sql_update = "UPDATE cash_records SET payment=%s WHERE year=%s AND month=%s AND day=%s"
                mycursor.execute(sql_update, (updated_payment, current_year, current_month, current_day))
                self.connection.commit()
                flag = False
            else:
                # If no record exists, insert a new record with 0 payment and update it
                sql = "INSERT INTO cash_records (year, month, day, payment) VALUES (%s, %s, %s, %s)"
                values = (current_year, current_month, current_day, 0)
                mycursor.execute(sql, values)
                self.connection.commit()

        # Retrieve the current counter value from the history table
    def get_Counter(self):
        mycursor = self.connection.cursor()
        sql = "SELECT counter FROM {}".format("histry")
        mycursor.execute(sql)
        counter = []

        # Fetch all rows and store the counter values
        for row in mycursor:
            for field in row:
                counter.append(field)
                
        # Find the maximum counter value
        number = max(counter)
        
        # Increment the counter value or reset it to 1 if it reaches 20
        if number == 20:
            number = 1
        else:
            number += 1
        
        return number

        # Update the history table with the latest entry
    def Update_Histry(self, block_number, Sloat):
        # Create a cursor object to execute SQL queries
        mycursor = self.connection.cursor()
        
        # SQL query to update the history table
        sql = "UPDATE {} SET Block_number = %s ,Sloat_number = %s , Car_number = %s , Mobile_number = %s , Entry_Time = %s , Exit_Time = %s, Difference_Time = %s, Payment = %s , counter = %s  WHERE hist_no = %s LIMIT 1".format("histry")
        
        # Values to be updated in the history table
        val = (block_number, Sloat[0], Sloat[1], int(Sloat[2]), Sloat[3], Sloat[4], int(Sloat[5]), int(Sloat[6]), self.get_Counter(), self.get_Counter())
        
        # Execute the SQL query with the values
        mycursor.execute(sql, val)
        
        # Commit the changes to the database
        self.connection.commit()
        
        # Update the cash records with the payment amount
        self.update_cash(int(Sloat[6]))
        
        # SQL query to update the parking block table with the latest entry details
        sql = "UPDATE {} SET  Car_number = %s , Mobile_number = %s , Entry_Time = %s , Exit_Time = %s, Difference_Time = %s, Payment = %s  Where Sloat_number=%s".format(block_number)
        
        # Values to be updated in the parking block table
        val = ('', '', '', '', '', '', int(Sloat[0]))
        
        # Execute the SQL query with the values
        mycursor.execute(sql, val)
        
        # Commit the changes to the database
        self.connection.commit()


        # Retrieve entry data for parking
    def get_entry_data(self, block_number):
        slot_number = self.check_sloat_number(block_number)
        
        # If parking is full, print a message and return
        if slot_number == 0:
            print("Parking is Full")
            return
        
        car_number = self.check_car_number()
        
        if self.check_car_Park(block_number, car_number):
            print("This Car is Already Park")
            return
        
        # Check the mobile number
        mobile_number = self.check_mobile_number()
        
        # Get the current entry time
        entry_time = self.get_current_time()
        
        # Update entry data in the parking system
        self.update_entry_data(block_number, car_number, mobile_number, entry_time, slot_number)
        
        self.display_entry_receipt(block_number, car_number, mobile_number, entry_time, slot_number)


    # Retrieve exit data for parking
    def get_exit_data(self, block_number):
        # Check the car number
        car_number = self.check_car_number()
        
        # If the car is not valid (not parked in the given block), return
        if not self.check_car_valid(block_number, car_number):
            return
        
        # Get the current exit time
        exit_time = self.get_current_time()
        
        # Calculate parking fee
        self.calculate_money(block_number, exit_time, car_number)
        
        # Display exit receipt
        self.display_exit_receipt(block_number, car_number)

    # Calculate parking fee
    def calculate_money(self, block_number, exit_time, car_number):
        mycursor = self.connection.cursor()
        
        # Retrieve entry time of the car
        mycursor.execute("SELECT Entry_Time FROM {} WHERE Car_number=%s".format(block_number), (car_number,))
        entry = mycursor.fetchone()
        
        # If entry record exists
        if entry:
            entry_time = entry[0]
            try:
                # Calculate time difference between entry and exit
                d1 = datetime.strptime(str(entry_time), "%Y-%m-%d %H:%M:%S")
                d2 = datetime.strptime(str(exit_time), "%Y-%m-%d %H:%M:%S")
                difference = (d2 - d1).total_seconds()
                difference_in_minutes = int(difference / 60)
                
                # Calculate payment
                payment = difference_in_minutes * 2
                
                # Update parking record with exit details and payment
                sql = "UPDATE {} SET Difference_Time = %s, Payment = %s, Exit_Time = %s  WHERE Car_number = %s".format(block_number)
                val = (difference_in_minutes, payment, exit_time, car_number)
                mycursor.execute(sql, val)
                self.connection.commit()
            except ValueError as e:
                print(e)
        else:
            print("Car entry not found.")

        # Check if the car is parked in the given block
    def check_car_valid(self, block_number, car_number):
        mycursor = self.connection.cursor()
        
        # Retrieve the slot number where the car is parked
        mycursor.execute("SELECT Sloat_number FROM {} WHERE Car_number=%s LIMIT 1".format(block_number), (car_number,))
        slot = mycursor.fetchone()
        
        # If slot number exists, return it
        if slot:
            return slot[0]
        else:
            print("Enter Valid Number")
            return 0

    # Check if the car is parked in the given block
    def check_car_Park(self, block_number, car_number):
        mycursor = self.connection.cursor()
        
        # Retrieve the slot number where the car is parked
        mycursor.execute("SELECT Sloat_number FROM {} WHERE Car_number=%s LIMIT 1".format(block_number), (car_number,))
        slot = mycursor.fetchone()
        
        # If slot number exists, return True (car is parked)
        if slot:
            return True
        else:
            return False

    # Check the car number format and validity
    def check_car_number(self):
        car_number = "0"
        flag = 0
        for i in range(4):
            count = 0
            print("-->Car number Enter this Format: GJ12CD0823")
            car_number = input("Enter Car No: ")
            if len(car_number) == 10:
                for j in range(10):
                    if j in [2, 3, 6, 7, 8, 9]:
                        if car_number[j].isdigit():
                            count += 1
                        else:
                            print(f"Enter Only Digit For {j + 1} character")
                            break
                    else:
                        if 'A' <= car_number[j] <= 'Z':
                            count += 1
                        else:
                            print(f"Enter Only A To Z For {j + 1} character")
                            break
                if count == 10:
                    flag = 1
            else:
                print("Enter 10 characters for Car No")
            if flag == 1:
                break
        return car_number


        # Check the format and validity of the mobile number
    def check_mobile_number(self):
        while True:
            mobile_number = input("Enter Mobile Number: ")
            if len(mobile_number) == 10 and mobile_number.isdigit():
                return mobile_number
            else:
                print("Enter 10 Digit Mobile Number")

    # Check for available parking slot number in the given block
    def check_sloat_number(self, block_number):
        mycursor = self.connection.cursor()
        
        # Retrieve the slot numbers where Mobile_number is 0 (i.e., available slots)
        sql = "SELECT Sloat_number FROM {} WHERE Mobile_number=0".format(block_number)
        mycursor.execute(sql)
        Sloat = []

        for row in mycursor:
            for field in row:
                Sloat.append(field)
                
        if Sloat:
            return min(Sloat)
        else:
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            print("*                                                                         *")
            print("*                           Parking is Full                               *")
            print("*                                                                         *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            return 0

        # Update entry data for a vehicle in the parking slot
    def update_entry_data(self, block_number, car_number, mobile_number, entry_time, slot_number):
        mycursor = self.connection.cursor()
        
        # SQL query to update the car number, mobile number, and entry time for the given slot number
        sql = "UPDATE {} SET Car_number = %s, Mobile_number = %s, Entry_Time = %s WHERE Sloat_number = %s".format(block_number)
        val = (car_number, mobile_number, entry_time, slot_number)
        mycursor.execute(sql, val)
        self.connection.commit()

    # Get the current date and time
    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    # Close the MySQL connection
    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


# if __name__ == "__main__":
def menu():
    parking_system = ParkingSystem()
    try:
        flag = True
        while flag:
            # Display menu options
            print()
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            print("*                                Vehicle type                             * ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("* 1).Two Wheeler Vehicle.                         3).Other                *")
            print("*                                                                         *")
            print("* 2).Four Wheeler Vehicle.                        4).Return to login page.*")
            print("*                                                                         *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            choice = input("Enter one Option: ")  # Prompt user for input choice
            if choice == "1":
                if parking_system.ask_car_entry_exit() == '1':
                    parking_system.get_entry_data("block_a")
                else:
                    parking_system.get_exit_data("block_a")  # Process exit data for block A
            elif choice == "2":
                # For four-wheeler vehicles
                if parking_system.ask_car_entry_exit() == '1':
                    # If vehicle is entering
                    parking_system.get_entry_data("block_b")  # Process entry data for block B
                else:
                    # If vehicle is exiting
                    parking_system.get_exit_data("block_b")  # Process exit data for block B
            elif choice == "3":
                # For other types of vehicles
                if parking_system.ask_car_entry_exit() == '1':
                    # If vehicle is entering
                    parking_system.get_entry_data("block_c")  # Process entry data for block C
                else:
                    # If vehicle is exiting
                    parking_system.get_exit_data("block_c")  # Process exit data for block C
            elif choice == "4":
                flag = False
            else:
                print("<-----------Enter Valid Option------------>")
    finally:
        home.menu()
