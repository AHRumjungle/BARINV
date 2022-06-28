from distutils.log import debug
from logging import error
import sqlite3 as sq
import os
import time

###########
## Put a SQLite database file path here:
url = 'data.db'
## Put the target table here:
table = 'item'
###########
debug = False
# Default: False
###########




# Check for file path
if (url==""):
    os.system('cls')
    print("! Plese put the file path for the '.db' file in the 'url' varible !")
    input()
    os.abort()



conn = sq.connect(url)
c = conn.cursor()


def DBSetup():
    global debug
    while True:
        os.system('cls')
        print("##########")
        print("'q' to quit")
        print("1 - Setup database table")
        print("9 - Turn on/off debug")
        print("##########")
        result = input()

        if (result == 'q'):
            break


        if (result == '9'):

            if(debug == False):
                debug = True
                print("debug = True")
                print("Debug Mode On")
                time.sleep(1)
                
            else:
                debug = False
                print("Debug Mode Off")
                time.sleep(1)


        if (result == '1'):
            if(isTableThere == True):
                os.system('cls')
                print("Table is already detected, do you want to continue:")
                print("Yes, No")

                result = input()

                if (result=='No'):
                    break


            querry = "CREATE TABLE "+str(table)+" (serial INTEGER, name TEXT, status TEXT)"
            if (debug==True): print(querry)


            try:
                c.execute(querry)
                print("Table Created")
                time.sleep(1)
                pass
            except:
                print("Somthing Whent Wrong!")
                time.sleep(1)






def add():
    while True:
        #main loop
        os.system('cls')
        print("##########")
        print("Enter 'q' to quit")
        print("Adding product to database")
        print("Scan product")
        print("##########")
        scan = input()
        if (scan == 'q'):
            break
        print("##########")
        print("Name of Product:")
        name = input()
        print("##########")
        print("Current Status:")
        status = input()
        print("##########")



        if(name == 'q'):
            break
        else:
            querry = "INSERT INTO "+str(table)+" VALUES ("+str(scan)+", '"+str(name)+"', '"+str(status)+"')"
            if (debug==True): print(querry)


            try:
                c.execute(querry)
                pass
            except:
                print("Somthing Went Wrong!")
                print(error)
                time.sleep(1)
            
            conn.commit()

            time.sleep(1)

def serLookup():
    while True:
        os.system('cls')
        print("##########")
        print("Enter 'q' to quit")
        print("Looking up product from database")
        print("Scan product:")
        print("#########")
        scan = input()
        

        if (scan=='q'):
            break

        querry = "SELECT * FROM "+str(table)+" WHERE serial = "+str(scan)
        if (debug==True): print(querry)

        try:
            c.execute(querry)
        except:
            print("Somthing Went Wrong!")
            time.sleep(1)
            break

        result = c.fetchall()

        print('')
        print('Serial | Name | Status')
        print('---------------------')
        for item in result:
            print(str(item[0])+" | "+str(item[1])+" | "+str(item[2]))
        input()


def nameLookup():
    while True:
        os.system('cls')
        print("##########")
        print("Enter 'q' to quit")
        print("Looking up product from database")
        print("Type name of product:")
        print("#########")
        scan = input()
        

        if (scan=='q'):
            break

        querry = "SELECT * FROM "+str(table)+" WHERE name LIKE '%"+str(scan)+"%'"
        if (debug==True): print(querry)


        c.execute(querry)

        result = c.fetchall()

        print('')
        print('Serial | Name | Status')
        print('---------------------')
        for item in result:
            print(str(item[0])+" | "+str(item[1])+" | "+str(item[2]))
        input()


def changeStatus():
    while True:
        os.system('cls')
        print("##########")
        print("Enter 'q' to quit")
        print("1 - Single Change")
        print("2 - Bulk Change")
        print("##########")
        result = input()

        if (result == 'q'): break



        #Single Change
        if (result == '1'):
            while True:
                os.system('cls')
                print("##########")
                print("Enter 'q' to quit")
                print('Scan Product Serial')

                result = input()
                if (result == 'q'): break

                print("##########")
                print('Enter new status')
                print("##########")
                status = input()
                if (status == 'q'): break

                

                querry = "UPDATE "+str(table)+" SET status = '"+str(status)+"' WHERE serial = "+str(result)
                if (debug == True): print(querry)

                try:
                    c.execute(querry)
                    conn.commit()
                    pass
                except:
                    print("Somthing Whent Wrong")
                    time.sleep(1)



        #Bulk change
        if (result == '2'):
            os.system('cls')
            print("##########")
            print("Enter 'q' to quit")
            print('Enter new status')
            print("##########")

            status = input()
            if (status == 'q'): break

            while True:
                os.system('cls')
                print("##########")
                print("Enter 'q' to quit")
                print("New status: "+str(status))
                print('Scan Product Serial')
                print("##########")
                result = input()
                
                if (status == 'q'): break

                querry = "UPDATE "+str(table)+" SET status = '"+str(status)+"' WHERE serial = "+str(result)

                try:
                    c.execute(querry)
                    conn.commit()
                    pass
                except:
                    print("Somthing Whent Wrong")
                    time.sleep(1)




# Main Menue Loop

while True:
    os.system('cls')
    #Check for table in DB
    c.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='item'")

    if (debug==True): print(c.fetchall())

    if(c.fetchall()=='[]'):
        isTableThere = False
    else:
        isTableThere = True


    
    print("##########")
    print("'q' to quit")
    print("1 - Add items to database")
    print("2 - Serial Lookup")
    print("3 - Name Lookup")
    print("4 - Change Status")
    print("9 - Options")


    if(isTableThere == False):
        print("! No sutible table in database. Set up a table in 'options' !")


    print("##########")
    inputR = input()

    if (inputR == '1'):
        add()
        
    if (inputR == '2'):
        serLookup()

    if (inputR == '3'):
        nameLookup()

    if (inputR == '4'):
        changeStatus()

    if (inputR == '9'):
        DBSetup()
    if (inputR == 'q'):
        break

conn.commit()
conn.close()