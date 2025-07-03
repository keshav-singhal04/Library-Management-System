# Library Management System 📚

A comprehensive Library Management System built with Python and MySQL that provides both administrator and user functionalities for managing library operations efficiently.

---

## ✨ Features

### 👤 User Features
* **User Registration & Login**: Secure user registration with password confirmation and login system
* **Book Search & Browse**: Multiple search options including category, author, rental price, and book name
* **Book Issuing**: Users can issue books directly through the system
* **Issue History**: Complete history of all issued books with due dates and fine information
* **Profile Management**: Update personal details like password, mobile number, and email
* **Account Management**: Option to delete account (with proper validations)

### 👨‍💼 Administrator Features
* **User Management**: View all registered users and manage user accounts
* **Book Management**: Add, update, remove books and manage book quantities
* **Issue Tracking**: Complete oversight of all book issues and returns
* **Fine Management**: Track and manage overdue fines for all users
* **Supplier Management**: Manage book supplying centers and their details
* **Transaction History**: Track all book supply transactions
* **Return Processing**: Update book return status with fine calculation

---

## 🛠️ Getting Started

Follow these instructions to set up the Library Management System on your local machine.

### Prerequisites

Make sure you have the following installed on your system:
- **Python 3.x**: Programming language runtime
- **MySQL Server**: Database management system
- **Required Python packages**:
  
  ```bash
  pip install pymysql mysql-connector-python
  ```

### Installation

1. **Clone or Download**: Save the project files to your local machine
   - `LBMS.py` - Main application file
   - `backend.sql` - Database setup script

2. **Setup Database**: 
   - Connect to your MySQL server
   - Run the `backend.sql` script to create the database and tables:
    <br>
    
   ```mysql
   SOURCE /path/to/backend.sql;
   ```

3. **Configure Database Connection**: 
   - Open `LBMS.py` 
   - Update the database connection parameters at the bottom of the file:

   <br>

   ```python
   mycon=pymysql.connect(
       host='localhost',
       user='your_username',
       password='your_password',
       db='Library',
       port=3306,
       connect_timeout=5
   )
   ```

4. **Run the Application**:
   ```
   python LBMS.py
   ```

---

## 🚀 Usage

### Admin Login
- **Access Key**: `Admin@12345`
- Full access to all management functions

### User Operations
- **Register**: Create new user account with personal details
- **Login**: Access using User ID and password
- **Search Books**: Browse available books by various criteria
- **Issue Books**: Select and issue books (one at a time)
- **View History**: Check personal issue history and pending fines

### Admin Operations
- **User Management**: View, manage, and remove user accounts
- **Book Management**: Add new books, update quantities, remove books
- **Issue Management**: Track all book issues and process returns
- **Fine Management**: Monitor and manage overdue fines
- **Supplier Management**: Manage book supplying centers

---

## 📊 Database Schema

### Core Tables
- **Users**: Store user registration and profile information
- **Books**: Manage book inventory with details and quantities
- **Issues**: Track all book issues, returns, and fines
- **Book_Centres**: Manage book supplying centers
- **Transaction_History**: Record book supply transactions

---

## 🔧 Technical Details

### Technology Stack
- **Language**: Python 3.x
- **Database**: MySQL
- **Database Connectivity**: PyMySQL, MySQL Connector
- **Architecture**: Console-based application with menu-driven interface

### Key Features Implementation
- **Auto-incrementing IDs**: Automatic ID generation for users and issues
- **Date Management**: Current date integration for issue tracking
- **Fine Calculations**: Automatic fine calculation based on return dates
- **Data Validation**: Comprehensive input validation and error handling
- **Transaction Management**: Database commits for data integrity


## 🏆 Acknowledgment
- Mr. Sachin Ahuja, for the project idea and database management.  
- A tutorial on Python-MySQL connectivity by [Learn Coding](https://www.youtube.com/watch?v=DVtS-z9U5qk)
