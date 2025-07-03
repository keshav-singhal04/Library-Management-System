-- Drop database if it exists
DROP DATABASE IF EXISTS Library;

-- Create database
CREATE DATABASE Library;

-- Use the database
USE Library;

-- Create Users table
CREATE TABLE Users (
    User_ID INT PRIMARY KEY,
    Password VARCHAR(10) NOT NULL,
    User_Name VARCHAR(20) NOT NULL,
    DOB CHAR(10) NOT NULL,
    Gender VARCHAR(6),
    Mob_No CHAR(10) UNIQUE NOT NULL,
    Email_ID VARCHAR(25) UNIQUE
);

-- Insert data into Users table
INSERT INTO Users (User_ID, Password, User_Name, DOB, Gender, Mob_No, Email_ID) VALUES
(135, 'Naman12345', 'Naman Goel', '09-02-2002', 'Male', '9879879870', 'naman123@gmail.com'),
(136, 'Ritu@24680', 'Ritu Sharma', '27-11-2001', 'Female', '9988776655', NULL),
(137, 'Vansh5927', 'Vansh Arora', '11-06-2004', 'Male', '9753102468', 'vansh93428@gmail.com'),
(138, 'Ram@54321', 'Ram Kaushik', '24-05-2000', 'Male', '8242495262', 'ramkaushik4224@gmail.com'),
(139, 'Geeta@123', 'Geeta Chauhan', '08-09-2005', 'Female', '7934235676', NULL),
(140, '123_Tyagi', 'Kanika Tyagi', '30-11-2003', 'Female', '9326195634', 'kanika_2324@gmail.com'),
(141, 'Yash@Gupta', 'Yash Gupta', '16-02-2004', 'Male', '8246228323', NULL);

-- Create Books table
CREATE TABLE Books (
    Book_ID VARCHAR(5) PRIMARY KEY,
    Book_Name VARCHAR(50) NOT NULL,
    Author VARCHAR(20) NOT NULL,
    Category VARCHAR(40) NOT NULL,
    Price INT NOT NULL,
    Rental_Price INT NOT NULL,
    Quantity INT NOT NULL
);

-- Insert data into Books table
INSERT INTO Books (Book_ID, Book_Name, Author, Category, Price, Rental_Price, Quantity) VALUES
('CSPYT', 'Computer Science with Python', 'Preeti Arora', 'Programming Books', 600, 60, 15),
('HC1', 'Concepts of Physics: Part 1', 'HC Verma', 'Exam Preparation Books', 320, 32, 25),
('HC2', 'Concepts of Physics: Part 2', 'HC Verma', 'Exam Preparation Books', 320, 32, 15),
('LTUSC', 'Let Us C', 'Yashavant Kanetkar', 'Programming Books', 260, 26, 13),
('MAH', 'Milk and Honey', 'Rupi Kaur', 'Poetry', 220, 22, 25),
('OLTWT', 'Oliver Twist', 'Charles Dickens', 'Novel', 130, 13, 27),
('PKK', 'Panchtantra Ki Kaahaaniyaan', 'Vishnu Sharma', 'Fairy Tales', 750, 75, 10),
('TTM', 'The Time Machine', 'HG Wells', 'Novel', 100, 10, 12),
('TDOYG', 'The Diary of a Young Girl', 'Anne Frank', 'Autobiography', 110, 11, 20),
('TIM', 'The Invisible Man', 'HG Wells', 'Science Fiction', 90, 9, 30);

-- Create Issues table
CREATE TABLE Issues (
    Issue_ID INT PRIMARY KEY,
    User_ID INT NOT NULL,
    User_Name VARCHAR(20) NOT NULL,
    Mob_No CHAR(10) NOT NULL,
    Book_ID VARCHAR(5) NOT NULL,
    Book_Name VARCHAR(50) NOT NULL,
    Issue_Date CHAR(10) NOT NULL,
    Due_Date CHAR(10),
    Submission_Date CHAR(10),
    Fine INT,
    Fine_paid INT,
    Fine_due INT
);

-- Insert data into Issues table
INSERT INTO Issues (Issue_ID, User_ID, User_Name, Mob_No, Book_ID, Book_Name, Issue_Date, Due_Date, Submission_Date, Fine, Fine_paid, Fine_due) VALUES
(278, 140, 'Kanika Tyagi', '9326195634', 'TTM', 'The Time Machine', '06-02-2022', '13-02-2022', '13-02-2022', 0, 1, 0),
(279, 137, 'Vansh Arora', '9753102468', 'HC2', 'Concepts of Physics: Part 2', '14-02-2022', '21-02-2022', '23-02-2022', 10, 10, 0),
(280, 141, 'Yash Gupta', '8246228323', 'OLTWT', 'Oliver Twist', '14-02-2022', '21-02-2022', '28-02-2022', 35, 25, 10),
(281, 136, 'Ritu Sharma', '9988776655', 'TDOYG', 'The Diary of a Young Girl', '16-02-2022', '23-02-2022', NULL, NULL, NULL, NULL),
(282, 138, 'Ram Kaushik', '8242495262', 'TIM', 'The Invisible Man', '17-02-2022', '24-02-2022', '28-02-2022', 20, 0, 20),
(283, 139, 'Geeta Chauhan', '7934235676', 'OLTWT', 'Oliver Twist', '19-02-2022', '26-02-2022', '26-02-2022', 0, 1, 0),
(284, 140, 'Kanika Tyagi', '9326195634', 'MAH', 'Milk and Honey', '20-02-2022', '27-02-2022', '28-02-2022', 5, 0, 0),
(285, 135, 'Naman Goel', '9879879870', 'TTM', 'The Time Machine', '20-02-2022', '27-02-2022', '26-02-2022', 0, 0, 0),
(286, 137, 'Vansh Arora', '9753102468', 'MAH', 'Milk and Honey', '23-02-2022', '02-03-2022', '03-03-2022', 5, 0, 0),
(287, 135, 'Naman Goel', '9879879870', 'HC1', 'Concepts of Physics: Part 1', '26-02-2022', '05-03-2022', NULL, NULL, NULL, NULL),
(288, 140, 'Kanika Tyagi', '9326195634', 'TDOYG', 'The Diary of a Young Girl', '28-02-2022', '07-03-2022', NULL, NULL, NULL, NULL);

-- Create Book_Centres table
CREATE TABLE Book_Centres (
    Centre_ID VARCHAR(5) PRIMARY KEY,
    Centre_Name VARCHAR(25) NOT NULL,
    Address VARCHAR(60) NOT NULL,
    PIN_CODE CHAR(6) NOT NULL,
    Mob_No CHAR(10) NOT NULL,
    Email_ID VARCHAR(25)
);

-- Insert data into Book_Centres table
INSERT INTO Book_Centres (Centre_ID, Centre_Name, Address, PIN_CODE, Mob_No, Email_ID) VALUES
('DK92', 'Saraswati Publications', '22/7, Ashok Nagar, New Delhi', '110018', '8293479948', 'sarawati2489@gmail.com'),
('OD29', 'Arora Publications', '75, Circular Road, Meerut Cantt', '250001', '9481389136', NULL),
('RM48', 'Vidhyarthi Printing Press', 'L-289, Shastri Nagar, Meerut', '250004', '8864675689', 'pressvidhya359@gmail.com'),
('SP28', 'Agarwal Printers', 'K-29, Arya Nagar, Ghaziabad', '201009', '9393563248', 'printers239@gmail.com');

-- Create Transaction_History table
CREATE TABLE Transaction_History (
    Centre_ID VARCHAR(5) NOT NULL,
    Centre_Name VARCHAR(25) NOT NULL,
    Book_ID VARCHAR(5) NOT NULL,
    Book_Name VARCHAR(50) NOT NULL,
    Quantity INT NOT NULL,
    Transaction_Date CHAR(10) NOT NULL
);

-- Insert data into Transaction_History table
INSERT INTO Transaction_History (Centre_ID, Centre_Name, Book_ID, Book_Name, Quantity, Transaction_Date) VALUES
('RM48', 'Vidhyarthi Printing Press', 'TTM', 'The Time Machine', 5, '18-02-2022'),
('DK92', 'Saraswati Publications', 'PKK', 'Panchtantra Ki Kaahaaniyaan', 15, '21-02-2022'),
('SP28', 'Agarwal Printers', 'HC1', 'Concepts of Physics: Part 1', 15, '21-02-2022'),
('SP28', 'Agarwal Printers', 'LTUSC', 'Let Us C', 10, '25-02-2022'),
('OD29', 'Arora Publications', 'TDOYG', 'The Diary of a Young Girl', 5, '23-02-2022');