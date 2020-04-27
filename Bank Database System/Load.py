# -*- coding: utf-8 -*-
"""
Name: Yash Patel
Student ID: 100621177
Purpose: This program will create a database and then drop, create, and populate tables from the database.

"""
import sqlite3


def drop_tables():
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    drop = open('./create_populate/drop_tables.sql')
    drop_tables = drop.read()
    c.executescript(drop_tables)
    
    conn.commit()
    conn.close()
    print("Tables mentioned in the SQL file are dropped! \n")

def create_tables():
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()
    
    create1 = open('./create_populate/drop_tables.sql')
    drop_tables = create1.read()
    c.executescript(drop_tables)
    conn.commit()

    create2 = open('./create_populate/create_tables.sql')
    create_tables = create2.read()
    c.executescript(create_tables)
    
    conn.commit()
    conn.close()
    print("New tables are created! \n") 


def populate_tables():
    conn = sqlite3.connect('./db/WorldBank.db')
    c = conn.cursor()

    populate = open('./create_populate/populate_tables.sql')
    populate_tables = populate.read()
    c.executescript(populate_tables)
    
    conn.commit()
    conn.close()
    print("Finished populating all the tables! \n") 


def main():
    print("-------------- WELCOME----------")
    print("This program will drop, create, and populate tables in the database.\n")

    print("Dropping tables...")
    drop_tables()

    print("Creating tables...")
    create_tables()

    print("Populating tables...")
    populate_tables()





if __name__ == '__main__':
    main()

    
