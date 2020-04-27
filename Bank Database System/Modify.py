# -*- coding: utf-8 -*-
"""
Name: Yash Patel
Student ID: 100621177
Purpose: This program will query, insert, update, and delete data from the tables in the database.

"""
import sqlite3

def selection_queries():
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    print("This selection query will find all customers names and how many times they have deposited money in their account. \n")
 
    
    c.execute("""SELECT customer_name, COUNT(Deposit_amount), FK_Account_type
                 FROM Customers, Money_deposit 
                 WHERE Customers.customer_id = Money_deposit.FK_customer_id
                 GROUP BY Deposit_amount;""")
      
    data = c.fetchall()
    
    for i in data:
        print(i)

    conn.close()

def selection1_queries():
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    print("\n This selection query will find customers with a credit card. \n")
 
    c.execute("""SELECT customer_id,customer_name,customer_postal_code,customer_city,customer_phone_number
                 FROM Customers, Has_account
                 WHERE (Customers.customer_id IN (Has_account.FK_customer_id)) AND ((Has_account.FK_Account_number) IN (SELECT FK_account_number FROM Has_credit_card));""")    
    data = c.fetchall()
    
    for i in data:
        print(i)

    conn.close()

def insert(ID, name, postalCode, city, phoneNumber):
    try:
        conn = sqlite3.connect('./db/WorldBank.db')
        c = conn.cursor()
        
        
     
        c.execute("INSERT INTO Customers (customer_id,customer_name,customer_postal_code, customer_city, customer_phone_number) VALUES ('" + ID + "','" + name + "','" + postalCode + "','" + city + "','" + phoneNumber + "')")
        data = c.fetchall()

        print("\n This INSERT query will add a customer to customer table. \n")
        
        for i in data:
            print(i)
        conn.commit()
        
        c.execute("Select * from Customers;")
          
        data1 = c.fetchall()
        
        for j in data1:
            print(j)
        conn.close()
    except sqlite3.IntegrityError:
        print("\nPlease make sure values which are primary key much be unique.\n")
        main()
    
    


def update(amount):
    
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    print("\nThese are all credit cards which are active and inactive. You will see all active credit card's limit has changed. \n")
 
    c.execute("UPDATE Creditcard set Card_limit = " + amount + " WHERE credit_card_number IN (SELECT FK_credit_card_number FROM Has_credit_card);")    
    data = c.fetchall()
    
    for i in data:
        print(i)

   
    conn.commit()

    c.execute("Select * from Creditcard;")
      
    data1 = c.fetchall()
    
    for j in data1:
        print(j)
    conn.close()

def delete():
    
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    print("\nThis output will show you that users with no account are deleted. \n")
    print("\n Users with an inactive account. \n")
    c.execute("SELECT * FROM Customers WHERE Customers.customer_id NOT IN (SELECT FK_customer_id FROM Has_account);")    
    
    data2 = c.fetchall()
    for has_account in data2:
        print(has_account)

    print("\n Users without an active account are deleted. \n")
    c.execute("DELETE FROM Customers WHERE Customers.customer_id NOT IN (SELECT FK_customer_id FROM Has_account);")    
    data = c.fetchall()
    
    for i in data:
        print(i)

   
    conn.commit()

    c.execute("Select * from Customers;")
      
    data1 = c.fetchall()
    
    for j in data1:
        print(j)
    conn.close()




def main():

    print("-------------- WELCOME----------")
    print("This user interface will allow you to query, insert, update, and delete the data from database.\n")

    print("1): Would you like to play with some insert queries?")
    print("2): Would you like to update some data in the database?")
    print("3): Would you like to delete some unwanted data?")
    print("4): Would you like to see some example of selection queries?")

    print("\nTo apply any of the options above please enter the corresponding option number.")
    option = input("Option #: ")

    if(option == "1"):
        print("\n This INSERT query will allow you to insert. Please make sure customer id is unique.\n")
        ID = input("Enter customer id: ")
        name = input("Enter customer name: ")
        phoneNumber = input("Enter customer phone number: ")
        city = input("Enter customer city: ")
        postalCode = input("Enter customer postal code: ")
        insert(ID, name, postalCode, city, phoneNumber)
        
    elif(option == "2"):
        print("\n This UPDATE query will allow you to change credit card limit for every user. \n")
        amount = input("Enter a amount to change credit limit for all users: ")
        update(amount)
        
    elif(option == "3"):
        print("\n This DELETE query will delete customers who does not have an account \n")
        delete()

    elif(option == "4"):
        print("Let's try to query some data from database... \n")
        selection_queries()
        selection1_queries()

    else:
        
        print("\nInvalid Input! Please try again.\n")
        main()


if __name__ == '__main__':
    main()
