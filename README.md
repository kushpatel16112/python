# Hotel Management System

## Overview
The Hotel Management System is a Python-based console application that allows users to manage hotel operations, including ordering food from a predefined menu. This system offers various features, such as selecting a meal from different cuisines and generating bills based on user selections.

## Features
- **Default Menu:** Users can view and order from a set menu.
- **Custom Orders:** Users have the option to create custom orders from different cuisines (Gujarati, Punjabi, Kathiyawadi).
- **Dynamic Billing:** Automatically calculates the total cost based on the number of people ordering.
- **User-friendly Interface:** Simple console-based interface for easy navigation.

## Technologies Used
- Python

## Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kushpatel16112/python.git
   cd hotel_system
   ```
2. **Run the Application: Make sure you have Python installed on your machine. You can run the application using:**
   ```bash
     python home.py
   ```
## Usage
Upon running the application, you will see a welcome message and a menu with options to:
- View the **default menu**
- Order by **your choice**
- **Exit** the system

Follow the prompts to select your meal and enter the number of people. The system will calculate and display your total bill based on your selections.

# Food Ordering System

This application is a simple Food Ordering System that allows users to:

- View a default menu.
- Order meals by their choice.
- Calculate and display the total bill.

## Usage

Upon running the application, you will see a welcome message and a menu with options to:

1. **View the default menu** (Option 1)
2. **Order by your choice** (Option 2)
3. **Exit the system** (Option 3)

Follow the prompts to select your meal and enter the number of people. The system will calculate and display your total bill based on your selections.

## Example of Usage

  1. **Welcome Message:**
     ```
     * * * * * * * * * * * * * * * * * * * * * * * * * * *
     *                                                   *
     *                    Welcome To                     *
     *               Food Ordering System                *
     *                                                   *
     * * * * * * * * * * * * * * * * * * * * * * * * * * *
     ```
  2. **Menu Options:**
     ```bash
     =============================
     |                           |
     |    1.Default menu         |
     |    2.Order by your choice |
     |    3.Exit                 |
     |                           |
     =============================
     Enter your choice:
     ```

  3. **Ordering Process:**
     - After choosing an option, you'll be prompted to select from different cuisines.
     - For example, if you select the default menu, you may see:
     ```bash
     Your Bill         
    ==========================
    |       ITEM         QUA.|
    | ---------------------- |
    | Default Lunch      3   |
    | ---------------------- |
    |     Total = 1500      |
    ==========================
     ```
## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Your contributions are welcome!

# Parking Management System

## Project Description

The **Parking Management System** is a software application designed to efficiently manage vehicle parking in a given facility. This system provides features for users to manage parking spots, track vehicle entries/exits, and handle administrative tasks related to parking lot operations.

The application includes a user-friendly interface for users to book and manage parking spots, an admin panel for managing system data, and a database for storing vehicle and parking information. It is scalable and can be adapted to various parking environments, such as commercial garages or residential parking lots.

---

## Features

- **User Panel**: Allows users to book parking spaces, check availability, and view their parking history.
- **Admin Panel**: Admins can manage parking spots, monitor parking activity, and generate reports.
- **Real-Time Availability**: View and track available parking spots in real-time.
- **Vehicle Management**: Logs details of vehicles entering and exiting the parking facility.
- **Billing System**: Automatically calculates parking fees based on the duration of stay.

---

## Technologies Used

- **Python**: Core programming language used for backend logic and functionality.
- **Tkinter**: A Python GUI library used to design the user interface for the parking management system. It provides various widgets to create buttons, labels, input fields, and more.
- **SQLite**: The system uses SQLite as the database to store and manage records related to parking slots, user data, and parking transactions.
- **Pandas**: Used for data manipulation and analysis, particularly for report generation and handling tabular data.

---

## File Structure

- **Parking_Menegment.py**: This file handles the main functionality of parking management, including checking availability and managing vehicle entries/exits.
- **Home.py**: This file defines the home screen and basic navigation for users.
- **Admin.py**: This file provides administrative functionality, such as managing parking slots, viewing logs, and handling other management tasks.

---

## Setup Instructions

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/kushpatel16112/python.git
   ```
2. **Install dependencies:**
   The project relies on Python and its libraries. You can install the dependencies using pip:
   ```bash
      pip install pandas
   ```
4. **Run the application:**
   ```bash
   python Home.py
   ```
## Usage

### User Operations:
- Users can book a parking slot based on availability.
- Users can track their parking time and calculate their bill.
- Users can check their parking history.

### Admin Operations:
- Admins can view and manage available parking spaces.
- Admins can generate reports on vehicle parking activity.
- Admins can handle any configuration or system-level changes.

---

## Future Enhancements
- **Online Booking System**: Allow users to book parking spaces online via a web interface.
- **Mobile App Integration**: Create a mobile application to provide a more convenient interface for users.
- **Advanced Reporting**: Add more detailed reports and data analysis for admin users, including parking trends and predictive analytics.

---

## License

This project is open source.
