import time
import pymysql
import mysql.connector as ms
from datetime import date

def wait():
    time.sleep(1)
    print()
    print("Press enter to continue")
    i=input()

def login():
    print()
    print("1. Login as administrator")
    print("2. Login as user")
    print()
    time.sleep(0.5)
    ch=int(input("Enter your choice: "))
    time.sleep(0.2)
    if ch==1:
        key=input("Enter the admin access key: ")
        time.sleep(0.1)
        if key=='Admin@12345':
            print()
            print("-"*10,"Welcome to the Library","-"*10)
            print()
            time.sleep(0.4)
            admin_menu()
        else:
            print()
            print("ERROR: The entered admin access key is wrong!")
            time.sleep(1)
            login()
    elif ch==2:
        user_entry()
    else:
        print("ERROR: Invalid Choice!")
        time.sleep(1)
        login()

def user_entry():
    print()
    print("1. Login")
    print("2. Register")
    print()
    time.sleep(0.7)
    ch=int(input("Enter your choice: "))
    time.sleep(0.7)
    if ch==1:
        print()
        user=input("Enter the user ID: ")
        pwd=input("Enter the password: ")
        time.sleep(0.4)
        mycursor.execute("select Password,User_Name from Users where User_ID="+user)
        key=mycursor.fetchall()
        if mycursor.rowcount==1:
            if str(key[0][0])==pwd:
                print()
                print("Welcome back,",key[0][1],"!")
                time.sleep(1)
                user_menu(user)
            else:
                print()
                print("ERROR: The entered password is wrong!")
                time.sleep(1)
                user_entry()
        else:
            print()
            print("ERROR: The user ID",user,"does not exist!")
            time.sleep(1)
            user_entry()
    elif ch==2:
        print()
        print("-"*10,"Registration Forum for Library Management System","-"*10)
        print()
        time.sleep(0.4)
        name=input("Enter the Name: ").title()
        dob=input("Enter the Date of Birth (DD-MM-YYYY): ")
        gender=input("Enter the Gender (M/F): ")
        if gender=='M':
            gender='Male'
        else:
            gender='Female'
        mob=input("Enter the Mobile Number: ")
        email=input("Enter the Email ID: ")
        mycursor.execute("select max(User_ID) from Users")
        data=mycursor.fetchone()
        userid=int(data[0])+1
        time.sleep(0.6)
        print()
        print("SUCCESS: You have been allotted the User ID "+str(userid)+"!")
        time.sleep(0.4)
        print()
        p1=input("Create a password: ")
        p2=input("Re-enter the password: ")
        while p1!=p2:
            print("ERROR: The passwords entered do not match!")
            p1=input("Create a password: ")
            p2=input("Re-enter the password: ")
        k="insert into Users values ("+str(userid)+",'"+p1+"','"
        mycursor.execute(k+name+"','"+dob+"','"+gender+"','"+mob+"','"+email+"')")
        mycon.commit()
        time.sleep(0.4)
        print()
        print("SUCCESS: Your account has been created!")
        print()
        time.sleep(0.3)
        print("You can now login to the system through your user ID and password")
        time.sleep(1.2)
        user_entry()
    else:
        print("ERROR: Invalid Choice!")
        time.sleep(1)
        user_entry()

def user_menu(x):
    while True:
        print()
        print("1. Display your issue history")
        print("2. Search for a book")
        print("3. Update your personal details")
        print("4. Delete your account")
        print("5. Logout")
        print()
        ch=int(input("Enter your choice: "))
        time.sleep(0.7)
        if ch==1:
            user_issue_history(x)
            wait()
        elif ch==2:
            user_search(x)
            wait()
        elif ch==3:
            user_update(x)
            wait()
        elif ch==4:
            delete=user_delete(x)
            wait()
            if delete==1:
                break
        elif ch==5:
            break
        else:
            print("ERROR: Invalid Choice")
    time.sleep(0.5)
    print("You have successfully logged out")
    time.sleep(0.7)
    print()
    print("-"*10,"THANKS FOR THE VISIT","-"*10)

def user_issue_history(x):
    k="select Issue_ID,Book_ID,Book_Name,Issue_Date,Due_Date,Submission_Date,Fine,"
    mycursor.execute(k+"Fine_paid,Fine_due from Issues where User_ID="+x+" order by Issue_Date desc")
    data=mycursor.fetchall()
    print()
    if mycursor.rowcount==0:
        print("No issue history found")
    else:
        print("%10s"%"Issue_ID","%10s"%"Book ID","%40s"%"Book Name",\
        "%15s"%"Issue Date","%15s"%"Due Date","%15s"%"Submission Date",\
        "%5s"%"Fine","%10s"%"Fine paid","%10s"%"Fine due")
        print("-"*145)
        total=0
        for row in data:
            print("%10s"%row[0], "%10s"%row[1], "%40s"%row[2], "%15s"%row[3], \
            "%15s"%row[4], "%15s"%row[5], "%5s"%row[6], "%10s"%row[7], "%10s"%row[8])
            if row[8]!=None:
                total+=row[8]
        print()
        time.sleep(1)
        print("Total due fine: Rs",total)

def user_search(x):
    print()
    print("1. Display all available books")
    print("2. Display books according to the category")
    print("3. Display books according to the rental price")
    print("4. Display books according to the author name")
    print("5. Search for a book by its name")
    print()
    time.sleep(1.5)
    ch=int(input("Enter your choice: "))
    if ch==1:
        k="select Book_ID,Book_Name,Author,Category,"
        mycursor.execute(k+"Price,Rental_Price from Books where Quantity>0")
        show_books(x)
    elif ch==2:
        ctg=input("Enter the category of books to be displayed: ")
        k="select Book_ID,Book_Name,Author,Category,Price,"
        mycursor.execute(k+"Rental_Price from Books where Category='"+ctg+"'")
        show_books(x)
    elif ch==3:
        a=input("Enter the minimum rental price: ")
        b=input("Enter the maximum rental price: ")
        k="select Book_ID,Book_Name,Author,Category,Price,"
        mycursor.execute(k+"Rental_Price from Books where Rental_Price>="+a+" and Rental_Price<="+b)
        show_books(x)
    elif ch==4:
        author=input("Enter the author name for the books to be displayed: ")
        k="select Book_ID,Book_Name,Author,Category,"
        mycursor.execute(k+"Price,Rental_Price from Books where Author='"+author+"'")
        show_books(x)
    elif ch==5:
        name=input("Enter the name of the book: ")
        k="select Book_ID,Book_Name,Author,Category,Price,"
        mycursor.execute(k+"Rental_Price from Books where Book_Name like'"+name+"%'")
        show_books(x)
    else:
        print("ERROR: Invalid Choice!")
        time.sleep(1)
        user_search(x)

def show_books(x):
    data=mycursor.fetchall()
    time.sleep(1)
    if mycursor.rowcount==0:
        print("No books available right now")
    else:
        print("%10s"%"Book ID", "%40s"%"Book Name", "%20s"%"Author",\
        "%25s"%"Category", "%10s"%"Price", "%15s"%"Rental Price")
        print("-"*125)
        books=[]
        for row in data:
            print("%10s"%row[0], "%40s"%row[1], "%20s"%row[2], "%25s"%row[3], "%10s"%row[4], "%15s"%row[5])
            books.append(str(row[0]))
        print()
        order=input("Do you want to issue a book? (Y/N): ").upper()
        time.sleep(0.3)
        if order=='Y':
            book=input("Enter the Book ID of the book you want to issue: ")
            time.sleep(0.3)
            while book not in books:
                print("ERROR: Enter a Book ID from the ones displayed above")
                time.sleep(0.5)
                book=input("Enter the Book ID of the book you want to issue: ")
            mycursor.execute("select Book_Name from Issues where User_ID="+x+" and Submission_Date is null")
            data=mycursor.fetchone()
            if mycursor.rowcount==1:
                print("You cannot issue another book until you return the book",data[0])
            else:
                mycursor.execute("select User_Name,Mob_No from Users where User_ID="+x)
                data=mycursor.fetchone()
                user,mob=data[0],data[1]
                mycursor.execute("select Book_Name from Books where Book_ID='"+book+"'")
                data=mycursor.fetchone()
                bname=data[0]
                today=str(date.today())
                issuedate=today[8:10]+'-'+today[5:7]+'-'+today[0:4]
                mycursor.execute("select max(Issue_ID) from Issues")
                data=mycursor.fetchone()
                issueid=int(data[0])+1
                k1="insert into Issues(Issue_ID,User_ID,User_Name,Mob_No,"
                k2="Book_ID,Book_Name,Issue_Date) values ("
                k3=str(issueid)+",'"+x+"','"+user+"','"+mob+"','"+book+"','"+bname+"','"+issuedate+"')"
                mycursor.execute(k1+k2+k3)
                mycon.commit()
                mycursor.execute("update Books set Quantity=Quantity-1 where Book_ID='"+book+"'")
                mycon.commit()
                print("SUCCESS: You have been issued the book titled",bname,"!")

def user_update(x):
    print()
    print("1. Update your password")
    print("2. Update your mobile number")
    print("3. Update your email ID")
    print()
    time.sleep(0.5)
    ch=int(input("Enter your choice: "))
    time.sleep(0.7)
    if ch==1:
        a=input("Enter the new password: ")
        b=input("Re-enter the new password: ")
        time.sleep(0.3)
        while a!=b:
            print("ERROR: The entered passwords do not match!")
            print()
            a=input("Enter the new password: ")
            b=input("Re-enter the new password: ")
        mycursor.execute("update Users set Password='"+a+"' where User_ID="+x)
        mycon.commit()
        print("SUCCESS: Your password has been reset!")
    elif ch==2:
        mob=input("Enter the new mobile number: ")
        mycursor.execute("update Users set Mob_No='"+mob+"' where User_ID="+x)
        mycon.commit()
        print("SUCCESS: Your mobile number has been updated!")
    elif ch==3:
        email=input("Enter the new email ID: ")
        mycursor.execute("update Users set Email_ID='"+email+"' where User_ID="+x)
        mycon.commit()
        print("SUCCESS: Your email ID has been updated!")
    else:
        print("ERROR: Invalid Choice")
        time.sleep(1)
        user_update(x)

def user_delete(x):
    print()
    mycursor.execute("select sum(Fine_due) from Issues where User_ID="+x)
    due=mycursor.fetchone()
    if due[0]==0:
        mycursor.execute("select Book_Name from Issues where User_ID="+x+" and Submission_Date is null")
        data=mycursor.fetchall()
        if mycursor.rowcount==0:
            mycursor.execute("delete from Users where User_ID="+x)
            mycon.commit()
            print("SUCCESS: Your account has been removed")
            return 1
        else:
            print("You have not yet returned the book",data[0][0])
            print("Your account cannot be deleted until the book is returned")
            return 0
    else:
        print("You have a payable fine of Rs.",due[0])
        print("Your account cannot be deleted until the due fine is cleared")
        return 0

def admin_menu():
    while True:
        print()
        print("1. Display the list of registered users")
        print("2. Delete a user's account")
        print("3. Display the list of users having pending fine")
        print("4. Display the list of available books")
        print("5. Update the quantity of a book")
        print("6. Add a new book to the library")
        print("7. Remove an existing book from the library")
        print("8. Display the issue history of all users")
        print("9. Update the return status of an issued book")
        print("10. Display the list of book supplying centres")
        print("11. Add a new book supplying centre")
        print("12. Update the details of an existing supplying centre")
        print("13. Remove an existing book supplying centre")
        print("14. Display the transaction history of books supplied")
        print("15. Logout")
        print()
        time.sleep(0.5)
        ch=int(input("Enter your choice: "))
        time.sleep(0.6)
        if ch==1:
            admin_display_users()
            wait()
        elif ch==2:
            x=input("Enter the User ID of the user whose account is to be deleted: ")
            admin_delete_user(x)
            wait()
        elif ch==3:
            admin_display_fine()
            wait()
        elif ch==4:
            admin_display_books()
            wait()
        elif ch==5:
            admin_update_book()
            wait()
        elif ch==6:
            admin_add_book()
            wait()
        elif ch==7:
            admin_remove_book()
            wait()
        elif ch==8:
            admin_display_issues()
            wait()
        elif ch==9:
            admin_update_return()
            wait()
        elif ch==10:
            admin_display_centres()
            wait()
        elif ch==11:
            admin_add_centre()
            wait()
        elif ch==12:
            print()
            cid=input("Enter the Centre ID of the centre whose details are to be updated: ")
            admin_update_centre(cid)
            wait()
        elif ch==13:
            admin_remove_centre()
            wait()
        elif ch==14:
            admin_display_transactions()
            wait()
        elif ch==15:
            break
        else:
            print("ERROR: Invalid Choice")
            time.sleep(0.5)
    time.sleep(0.5)
    print("You have successfully logged out")
    time.sleep(0.7)
    print()
    print("-"*10,"THANKS FOR THE VISIT","-"*10)

def admin_display_users():
    mycursor.execute("select * from Users")
    data=mycursor.fetchall()
    print()
    print("%10s"%"User ID","%15s"%"Password","%20s"%"User Name","%15s"%"Date of Birth",\
    "%10s"%"Gender","%15s"%"Mobile No.","%30s"%"Email ID")
    print("-"*130)
    for row in data:
        print("%10s"%row[0],"%15s"%row[1],"%20s"%row[2],"%15s"%row[3],\
        "%10s"%row[4],"%15s"%row[5],"%30s"%row[6])

def admin_delete_user(x):
    mycursor.execute("delete from Users where User_ID="+x)
    mycon.commit()
    print()
    print("SUCCESS: The account with the user ID",x,"has been deleted!")

def admin_display_fine():
    mycursor.execute("select User_ID from Users")
    data=mycursor.fetchall()
    users=[]
    for row in data:
        users.append(str(row[0]))
    fine={}
    for i in users:
        mycursor.execute("select sum(Fine_due) from Issues where User_ID="+i)
        data=mycursor.fetchone()
        fine[i]=data[0]
    details={}
    for i in fine:
        if fine[i] not in (0,None):
            mycursor.execute("select User_Name,Mob_No,Email_ID from Users where User_ID="+i)
            data=mycursor.fetchone()
            details[i]=[data[0],fine[i],data[1],data[2]]
    print()
    if len(details)==0:
        print("No Users found with pending fine")
    else:
        print("%10s"%"User ID", "%20s"%"User Name", "%5s"%"Fine", "%15s"%"Mobile No.", "%30s"%"Email ID")
        print("-"*90)
        for i in details:
            print("%10s"%i,"%20s"%details[i][0], "%5s"%details[i][1],\
            "%15s"%details[i][2], "%30s"%details[i][3])

def admin_display_books():
    mycursor.execute("select * from Books")
    data=mycursor.fetchall()
    print()
    print("%10s"%"Book ID", "%50s"%"Book Name", "%25s"%"Author", "%35s"%"Category",\
    "%10s"%"Price", "%15s"%"Rental Price", "%15s"%"Quantity")
    print("-"*175)
    for row in data:
        print("%10s"%row[0], "%50s"%row[1], "%25s"%row[2], "%35s"%row[3],\
        "%10s"%row[4], "%15s"%row[5], "%15s"%row[6])

def admin_update_book():
    print()
    book=input("Enter the Book ID of the book whose quantity is to be updated: ")
    mycursor.execute("select Quantity from Books where Book_ID='"+book+"'")
    old=mycursor.fetchone()
    time.sleep(0.3)
    print("Current quantity of the book with Book ID",book,"is:",old[0])
    time.sleep(0.4)
    new=input("Enter the updated quantity of the book: ")
    mycursor.execute("update Books set Quantity="+new+" where Book_ID='"+book+"'")
    mycon.commit()
    time.sleep(0.3)
    print("SUCCESS: The quantity of this book has been updated!")

def admin_add_book():
    print()
    bid=input("Enter the Book ID: ")
    bname=input("Enter the Book Name: ")
    author=input("Enter the Author Name: ")
    ctg=input("Enter the Category: ")
    price=int(input("Enter the Price: "))
    qty=int(input("Enter the Quantity: "))
    rp=price/10
    k="insert into Books values ('"+bid+"', '"+bname+"', '"
    mycursor.execute(k+author+"', '"+ctg+"', "+str(price)+", "+str(rp)+", "+str(qty)+")")
    mycon.commit()
    time.sleep(0.4)
    print("SUCCESS: A new book has been added to the library!")

def admin_remove_book():
    print()
    bid=input("Enter the Book ID of the book to be removed: ")
    mycursor.execute("delete from Books where Book_ID='"+bid+"'")
    mycon.commit()
    print("SUCCESS: The book has been removed from the library!")

def admin_display_issues():
    mycursor.execute("select * from Issues")
    data=mycursor.fetchall()
    print()
    print("%10s"%"Issue ID", "%10s"%"User ID", "%20s"%"User Name", "%15s"%"Mobile No", \
    "%10s"%"Book ID", "%40s"%"Book Name", "%14s"%"Issue Date", "%14s"%"Due Date", \
    "%15s"%"Submission Date", "%5s"%"Fine", "%10s"%"Fine paid", "%10s"%"Fine due")
    print("-"*185)
    for row in data:
        print("%10s"%row[0], "%10s"%row[1], "%20s"%row[2], "%15s"%row[3], \
        "%10s"%row[4], "%40s"%row[5], "%14s"%row[6], "%14s"%row[7], \
        "%15s"%row[8], "%5s"%row[9], "%10s"%row[10], "%10s"%row[11])

def admin_update_return():
    print()
    issueid=input("Enter the Issue ID of the book which has been returned: ")
    date=input("Enter the Return Date (DD-MM-YYYY): ")
    fine=int(input("Enter the Fine (Enter 0 if none): "))
    finepaid=int(input("Enter the Fine paid (Enter 0 if none): "))
    finedue=fine-finepaid
    k="update Issues set Submission_Date='"+date+"', Fine="+str(fine)+", Fine_paid="
    mycursor.execute(k+str(finepaid)+", Fine_due="+str(finedue)+" where Issue_ID="+issueid)
    mycon.commit()
    mycursor.execute("select Book_ID from Issues where Issue_ID="+issueid)
    bid=mycursor.fetchone()
    mycursor.execute("update Books set Quantity = Quantity+1 where Book_ID='"+bid[0]+"'")
    mycon.commit()
    print("SUCCESS: The return status of this book has been updated!")

def admin_display_centres():
    mycursor.execute("select * from Book_Centres")
    data=mycursor.fetchall()
    print()
    print("%10s"%"Centre ID", "%30s"%"Centre Name", "%45s"%"Address",\
    "%10s"%"PIN CODE", "%15s"%"Mobile No.", "%25s"%"Email ID")
    print("-"*150)
    for row in data:
        print("%10s"%row[0], "%30s"%row[1], "%45s"%row[2], "%10s"%row[3], "%15s"%row[4], "%25s"%row[5])

def admin_add_centre():
    print()
    cid=input("Enter the Centre ID: ")
    cname=input("Enter the Centre Name: ")
    adrs=input("Enter the Address: ")
    pin=input("Enter the PIN CODE: ")
    mob=input("Enter the Mobile Number: ")
    email=input("Enter the Email ID: ")
    k="insert into Book_Centres values ('"+cid+"', '"
    mycursor.execute(k+cname+"', '"+adrs+"', '"+pin+"', '"+mob+"', '"+email+"')")
    mycon.commit()
    print("SUCCESS: A new book supplying centre has been added to the library!")

def admin_update_centre(cid):
    print()
    time.sleep(0.3)
    print("1. Update the Address")
    print("2. Update the PIN CODE")
    print("3. Update the Mobile Number")
    print("4. Update the Email ID")
    print()
    time.sleep(0.5)
    ch=int(input("Enter your choice: "))
    time.sleep(0.2)
    if ch==1:
        adrs=input("Enter the updated Address: ")
        mycursor.execute("update Book_Centres set Address='"+adrs+"' where Centre_ID='"+cid+"'")
        mycon.commit()
        print("SUCCESS: The address of the book supplying centre has been updated!")
    elif ch==2:
        pin=input("Enter the updated PIN CODE: ")
        mycursor.execute("update Book_Centres set PIN_CODE='"+pin+"' where Centre_ID='"+cid+"'")
        mycon.commit()
        print("SUCCESS: The PIN CODE of the book supplying centre has been updated!")
    elif ch==3:
        mob=input("Enter the updated Mobile Number: ")
        mycursor.execute("update Book_Centres set Mob_No='"+mob+"' where Centre_ID='"+cid+"'")
        mycon.commit()
        print("SUCCESS: The mobile number of the book supplying centre has been updated!")
    elif ch==4:
        email=input("Enter the updated Email ID: ")
        mycursor.execute("update Book_Centres set Email_ID='"+email+"' where Centre_ID='"+cid+"'")
        mycon.commit()
        print("SUCCESS: The email ID of the book supplying centre has been updated!")
    else:
        print("ERROR: Invalid Choice!")
        admin_update_centre(cid)

def admin_remove_centre():
    print()
    cid=input("Enter the Centre ID of the book centre to be removed: ")
    mycursor.execute("delete from Book_Centres where Centre_ID='"+cid+"'")
    mycon.commit()
    print("SUCCESS: The book supplying centre has been removed from the library!")

def admin_display_transactions():
    mycursor.execute("select * from Transaction_History")
    data=mycursor.fetchall()
    print()
    print("%10s"%"Centre ID", "%30s"%"Centre Name", "%10s"%"Book ID", \
    "%40s"%"Book Name", "%15s"%"Quantity", "%25s"%"Transaction Date")
    print("-"*150)
    for row in data:
        print("%10s"%row[0], "%30s"%row[1], "%10s"%row[2], "%40s"%row[3], "%15s"%row[4], "%25s"%row[5])

mycon=pymysql.connect(host='localhost',user='root',password='root',db='Library',port=3306,connect_timeout=5)
mycursor=mycon.cursor()
print()
print("-"*10,"WELCOME TO LIBRARY MANAGEMENT SYSTEM","-"*10)
login()