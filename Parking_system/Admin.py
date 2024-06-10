import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import Home as home

class Admin:
    def __init__(self):
        try:
            # Attempt to establish a connection to the MySQL database
            self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="parking_management")
            # Check if the connection is successful
            if self.connection.is_connected():
                self.Option()
        except mysql.connector.Error as error:
            # If connection fails, print an error message
            print("Failed to connect to MySQL:", error)

    def Option(self):
        while True:
            print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("*                                                                         *")
            print("*    1).Display History.                                                  *")
            print("*                                                                         *")
            print("*    2).Graph Comparison.                                                 *")
            print("*                                                                         *")
            print("*    3).Return to login page.                                             *")
            print("*                                                                         *")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            choice = input("Enter one Option: ")

            if choice == "1":
                self.Get_History()
            elif choice == "2":
                self.Get_graf()
            elif choice == "3":
                home.menu()
            else:
                print("<-------Enter Valid Option--------->")
                
    def Get_graf(self):

        year=self.Get_graf_info_year('year')
        print("Available Years:",year)
        In_year=int(input("Enter Year: "))
        if In_year not in year:
            print("<---------Plese Enter valied Year---------->")
            return
        month=self.Get_graf_info_month('month',In_year)
        print("Available Months:",month)
        In_month=int(input("Enter month: "))
        if In_month not in month:
            print("<---------Plese Enter valied Month---------->")
            return
        day=month=self.Get_graf_info_day('day',In_month,In_year)
        print("Available Days:",day)
        start_day=int(input("Enter day , you start Graph: "))
        if start_day not in day:
            print("<---------Plese Enter valied Day---------->")
            return
        end_day=int(input("Enter day , you end Graph: "))
        if end_day not in day:
            print("<---------Plese Enter valied Day---------->")
            return
        graph_data=self.graph_data(In_year,In_month)
        self.sort_graph_data(graph_data,start_day,end_day)
        
    def sort_graph_data(self,graph_data,start_day,end_day):
        graph_day=[]
        graph_payment=[]
        for i in graph_data:
            counter=1
            for j in i:
                if counter==1:
                    graph_day.append(j)
                else:
                    graph_payment.append(j)
                counter+=1
        if start_day < end_day:
            min=start_day
            max=end_day
        else:
            max=start_day
            min=end_day
        min_index=graph_day.index(min)
        max_index=graph_day.index(max)
        Days=[]
        Payment=[]
        for i in range(min_index,max_index+1):
            Days.append(graph_day[i])
            Payment.append(graph_payment[i])
        self.Display(Days,Payment)
        
    def Display(self,Days,Payment):
        x=np.array(Days)
        y=np.array(Payment)
        plt.bar(x,y,color="red")
        plt.xlabel("Days")
        plt.ylabel("Payment")
        plt.legend()
        plt.title("Data of Parking Menegment System ",fontweight="bold")
        plt.show()
        
    def graph_data(self,In_year,In_month):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(("SELECT day,payment FROM cash_records where year=%s and month=%s"),(In_year,In_month,))
            rows = mycursor.fetchall()
            Sloat = []
            if rows:
                for row in rows:
                    add=[]
                    for field in row:
                        add.append(field)
                    Sloat.append(add)
            else:
                print("No history found.")
            return Sloat
        except mysql.connector.Error as error:
            print("Error fetching history:", error)
    def Get_graf_info_year(self,year):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT DISTINCT {} FROM cash_records".format(year))
            rows = mycursor.fetchall()
            Sloat = []
            if rows:
                for row in rows:
                    for field in row:
                        Sloat.append(field)
            else:
                print("No history found.")
            return Sloat
        except mysql.connector.Error as error:
            print("Error fetching history:", error)
    def Get_graf_info_month(self,month,year):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(("SELECT DISTINCT {} FROM cash_records where year=%s".format(month)),(year,))
            rows = mycursor.fetchall()
            Sloat = []
            if rows:
                for row in rows:
                    for field in row:
                        Sloat.append(field)
            else:
                print("No history found.")
            return Sloat
        except mysql.connector.Error as error:
            print("Error fetching history:", error)
    def Get_graf_info_day(self,day,month,year):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(("SELECT DISTINCT {} FROM cash_records where year=%s and month=%s".format(day)),(year,month))
            rows = mycursor.fetchall()
            Sloat = []
            if rows:
                for row in rows:
                    for field in row:
                        Sloat.append(field)
            else:
                print("No history found.")
            return Sloat
        except mysql.connector.Error as error:
            print("Error fetching history:", error)
    def Get_History(self):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT * FROM histry")
            rows = mycursor.fetchall()
            if rows:
                for row in rows:
                    self.Display_History(row)
                    n=input("Continue or exit :")
                    if n=='exit':
                        return
            else:
                print("No history found.")
        except mysql.connector.Error as error:
            print("Error fetchin;g history:", error)

    def Display_History(self, row):
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*   History No          : ", row[0])
        print("*   Block No            : ", row[1])
        print("*   Slot No             : ", row[2])
        print("*   Car No              : ", row[3])
        print("*   Mobile No           : ", row[4])
        print("*   Enter Date & Time   : ", row[5])
        print("*   Exit Date & Time    : ", row[6])
        print("*   Difference of Time  : ", row[7])
        print("*   Payment             : ", row[8])
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

def menu():
    admin=Admin()