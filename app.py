from logging import error
import sqlite3 as sq
import os
import time
import numpy as np

############
##-BARINV-##
############
# 6/27/2022
############
## Put a SQLite database file path here:
url = 'data.db'
## Put the target table here:
table = 'item'
############
debug = False
# Default: False
############
## TO DO: ##
## 
############



# Check for file path to database
if (url==""):
    os.system('cls')
    print("! Plese put the file path for the '.db' file in the 'url' varible !")
    input()
    os.abort()



conn = sq.connect(url)
c = conn.cursor()






# Main Menue Loop
def mainMenue():
    
    while True:

        global isTableThere

        #Check for table in DB
        c.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='"+str(table)+"'")

        if(c.fetchall()==[]):
            isTableThere = False
        else:
            isTableThere = True

        if (debug==True): 
            print("Table: "+str(isTableThere))

            time.sleep(1)




        os.system('cls')
        
        print("#-BARINV-#")
        print("q - quit")
        print("1 - Add product to database")
        print("2 - Lookup")
        print("3 - Change Status")
        print("4 - Remove Product from database")
        print("9 - Options")
        print("0 - About")

        if(isTableThere == False):
            print("! No sutible table in database. Set up a table in 'options' !")

        print("##########")

        inputR = input()


        if (inputR == '1'):
            add()

        if (inputR == '2'):
           
           lookup()


        if (inputR == '3'):
            changeStatus()

        if (inputR == '4'):
            removeItem()

        if (inputR == '9'):
            DBSetup()
        
        if (inputR == '0'):
            #About
            os.system('cls')
            print("--BARINV--")
            print("##########")
            print("6/27/2022")
            print("TIP: Set the barcode scanner to have the suffix to be the 'ENTER' key for faster scanning")
            print("##########")
            input()

        if (inputR == 'q'):
            break


def DBSetup():
    global debug
    while True:
        os.system('cls')
        print("#-Setup-#")
        print("q - quit")
        print("1 - Setup database table")
        print("9 - Turn on/off debug")
        print("#########")
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


            querry = "CREATE TABLE "+str(table)+" (serial INTEGER UNIQUE, name TEXT, status TEXT)"
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
        os.system('cls')
        print("#-Add a Product-#")
        print("q - quit")
        print("1 - Single Add")
        print("2 - Bulk Add")
        print("#################")
        result = input()

        if (result == 'q'): break

        #Add one
        if(result == '1'):
            while True:
                os.system('cls')
                print("#-Add a single Product-#")
                print("Enter 'q' to quit")
                print("Scan product")
                print("########################")
                scan = input()
                if (scan == 'q'): break
                print("########################")
                print("Name of Product:")
                name = input()
                print("########################")
                print("Current Status:")
                status = input()
                print("########################")



                if(name == 'q'):
                    break
                else:
                    querry = "INSERT INTO "+str(table)+" VALUES ("+str(scan)+", '"+str(name)+"', '"+str(status)+"')"
                    if (debug==True): print(querry)


                    try:
                        c.execute(querry)
                        print("Added!")
                        pass
                    except:
                        print("Somthing Went Wrong!")
                        print(error)
                        time.sleep(1)

                    conn.commit()
                    time.sleep(1)


        #Bulk add
        if (result == '2'):
            os.system('cls')
            print("#-Bulk Add-#")
            print("Enter 'q' to quit")
            print("Name of Product:")
            print("##########")

            name = input()
            if (name == 'q'): break

            print("##########")
            print("Current Status:")
            print("##########")

            status = input()
            if (status == 'q'): break
            
            print("##########")
            print("Scan product")
            print("##########")
            
            
            while True:

                scan = input()

                if (scan == 'q'): break

                querry = "INSERT INTO "+str(table)+" VALUES ("+str(scan)+", '"+str(name)+"', '"+str(status)+"')"
                if (debug==True): print(querry)


                try:
                    c.execute(querry)
                    print("Added!")
                    pass
                except:
                    print("Somthing Went Wrong!")
                    print(error)
                    time.sleep(1)

                conn.commit()


def lookup():

    while True:
            os.system('cls')
            print("#-Look Up-#")
            print("q - quit")
            print("1 - Serial Lookup")
            print("2 - Name Lookup")
            print("3 - Custom SQL Lookup")
            print("###########")

            result = input()

            if (result == 'q'): break



            #Serial Look Up
            if (result == '1'):
                    while True:
                        os.system('cls')
                        print("#-Serial Number Lookup-#")
                        print("Enter 'q' to quit")
                        print("Scan product:")
                        print("########################")
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
                        print('# | Serial | Name | Status')
                        print('---------------------')
                        
                        #Lookup
                        rowCount = 0
                        for items in result:
                            length = np.size(items)
                            count = 0
                            row = ""
                            rowCount += 1
                            row += str(rowCount)+" | "
                            for parts in items:
                                count += 1
                                row += str(parts)
                                if(count != length):
                                    row += " | "
                            print(row)
                        input()



            #Name Look Up
            if(result == '2'):
                    while True:
                        os.system('cls')
                        print("#-Name Lookup-#")
                        print("Enter 'q' to quit")
                        print("Type name of product:")
                        print("###############")
                        scan = input()


                        if (scan=='q'):
                            break
                        
                        querry = "SELECT * FROM "+str(table)+" WHERE name LIKE '%"+str(scan)+"%'"
                        if (debug==True): print(querry)


                        c.execute(querry)

                        result = c.fetchall()

                        print('')
                        print('# | Serial | Name | Status')
                        print('---------------------')
                        

                        #Lookup
                        rowCount = 0
                        for items in result:
                            length = np.size(items)
                            count = 0
                            row = ""
                            rowCount += 1
                            row += str(rowCount)+" | "
                            for parts in items:
                                count += 1
                                row += str(parts)
                                if(count != length):
                                    row += " | "
                            print(row)
                        input()




            #SQL querry
            if(result == '3'):
                while True:
                    os.system('cls')
                    print("#-SQL Lookup-#")
                    print("Enter 'q' to quit")
                    print("Enter SQL commands too querry")
                    print("##############")

                    result = input()

                    if (result == 'q'): break

                    try:
                        c.execute(result)
                        pass
                    except:
                        print("Somthing Whent Wrong!")
                        time.sleep(1)

                    querry = c.fetchall()

                    if (debug==True): print(querry)

                    print("")
                    #print('Serial | Name | Status')
                    print('---------------------')



                    for items in querry:
                        length = np.size(items)
                        count = 0
                        row = ""
                        for parts in items:
                            count += 1
                            row += str(parts)
                            if(count != length):
                                row += " | "

                        
                        print(row)
                    
                    input()



def changeStatus():
    while True:
        os.system('cls')
        print("#-Change Status-#")
        print("q - quit")
        print("1 - Single Change")
        print("2 - Bulk Change")
        print("#################")
        result = input()

        if (result == 'q'): break



        #Single Change
        if (result == '1'):
            while True:
                os.system('cls')
                print("#-Single Change-#")
                print("Enter 'q' to quit")
                print('Scan Product Serial')
                print("#################")

                result = input()
                if (result == 'q'): break

                print("#################")
                print('Enter new status')
                print("#################")
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
            print("#-Bulk Change-#")
            print("Enter 'q' to quit")
            print('Enter new status')
            print("###############")

            status = input()
            if (status == 'q'): break

            while True:
                os.system('cls')
                print("#-Bulk Change-#")
                print("Enter 'q' to quit")
                print("New status: "+str(status))
                print('Scan Product Serial')
                print("###############")
                result = input()
                
                if (result == 'q'): break

                querry = "UPDATE "+str(table)+" SET status = '"+str(status)+"' WHERE serial = "+str(result)

                try:
                    c.execute(querry)
                    conn.commit()
                    pass
                except:
                    print("Somthing Whent Wrong")
                    time.sleep(1)


def removeItem():
    while True:
        os.system('cls')
        print("#-Remove Product-#")
        print("Enter 'q' to quit")
        print("Scan the prodcut that you would like to remove")
        print("##################")

        scan = input()

        if (scan == 'q'): break

        querry = "DELETE FROM item WHERE serial = '"+str(scan)+"'"

        try:
            c.execute(querry)
            conn.commit()
            print("removed")
        except:
            print("Somthing Whent Wrong!")
            time.sleep(1)



mainMenue()

conn.commit()
conn.close()