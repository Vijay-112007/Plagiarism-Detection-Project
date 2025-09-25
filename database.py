#This is one of the main code which is related with the database and consists of the things related to the dbms
import mysql.connector
import random
import os
import math
import time
#first we need to give time to students to submit those assignments
class Students:
    #Please see the main(function before working with the code)
    pass
class Admin:
    #First we need to connect to mysql server
    def __init__(self,password):
        self.dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = password,
        )
        self.cursorObject = self.dataBase.cursor()
        print(f"Connect to SQL language Successfully!")
    #Then we need to make the admin to create a database for the Project 
    def createDatabase(self,name):
        self.query = f"create database if not exists {name}"
        self.cursorObject.execute(self.query)
        #Here we switch to the created database so that the Admin no need to switch seperately
        self.query = f"use {name}"
        self.cursorObject.execute(self.query)
        print(f"Database {name} is Created and Shifted to use")
        self.dataBase.commit()
        print("-------------------------------------------------")
    #Here Admin can able to see all the existing databases
    def seeDatabases(self):
        self.query = "show databases"
        self.cursorObject.execute(self.query)
        self.results = self.cursorObject.fetchall()
        for x in self.results:
            print(x)
        print("-------------------------------------------------")
    #Here the Admin can use a Particular Database
    def useDatabase(self,database_name):
        self.query = f"use {database_name}"
        self.cursorObject.execute(self.query)
        print(f"Successfully Shifted to {database_name} Database")
        self.dataBase.commit()
        print("-------------------------------------------------")
    #Here Admin can create a table for the students
    def createTable(self,table_name):
        print(f"---Creating a Table with Name {table_name}---")
        self.query = f"create table if not exists {table_name} (student_id int primary key,student_name varchar(60) not null,student_branch varchar(40) not null,student_filename varchar(50),student_marks double,student_key varchar(50) unique not null)"
        self.cursorObject.execute(self.query)
        print(f"Table {table_name} was created Successfully")
        self.dataBase.commit()
        print("-------------------------------------------------")
    #Here the Admin can add values to the table based on the folders table
    def addValues(self,table_name,values):
        #first we will ask the user to enter connect the database if connected no need
        print(f"-----Printing the Table before Adding the Values----")
        self.query = f"select*from {table_name}"
        self.cursorObject.execute(self.query)
        self.results = self.cursorObject.fetchall()
        print("-------------------------------------------------")
        for x in self.results:
            print(x)
        print("-------------------------------------------------")
        print(f"----Adding the Values----")
        self.query = f"insert into {table_name} (student_id,student_name,student_branch,student_filename,student_marks,student_key) values(%s,%s,%s,%s,%s,%s)"
        self.cursorObject.executemany(self.query,values)
        self.dataBase.commit()
        print("---Insertion Successfull---")
        print("-------------------------------------------------")
    #Here the Admin can see all the values in the table
    def seeValues(self,table_name):
        #TO see the values or the entire table with the tuples 
        self.query = f"select*from {table_name}"
        self.cursorObject.execute(self.query)
        self.results = self.cursorObject.fetchall()
        for x in self.results:
            print(x)
        print("-------------------------------------------------")
    #Now the Admin want update one attribute in the table like when he want to add the marks something like that
    def updateValues(self,attribute_name1,attribute_name2,table_name,value1,value2):
        self.query = f"UPDATE {table_name}  SET {attribute_name1} = %s WHERE {attribute_name2} = %s"
        self.cursorObject.execute(self.query,(value1,value2))
        self.dataBase.commit()
        print(f"Updated the table successfully")
        print("-------------------------------------------------")
    #This is for deleting the database
    def deleteDatabase(self,name):
        self.query = f"drop database {name}"
        self.cursorObject.execute(self.query)
        self.dataBase.commit()
        print(f"Database {name} is Deleted succesfully and the remaining databases are below")
        self.seeDatabases()  
        print(f"Successfully completed")
        print("-------------------------------------------------")
    def closeConnection(self):
        self.cursorObject.close()
        self.dataBase.close()
        print(f"Successfully Disconnected from the Database")
        print("-------------------------------------------------")
#Now we will create a test case as manupulating with the database
def main():
    #THesee are only the pseudo test cases you are allowed to change these test cases as the code progresses
    print(f"Please Submit those Assignments before the deadline")
    #first we will create a database which consists of the students and then ask the students to enter their id and password
    Admin1 = Admin(#Enter the password here)
    Admin1.seeDatabases()
    Admin1.createDatabase("PlagiarismStudents")
    Admin1.seeDatabases()
    Admin1.useDatabase("Plagiarismstudents")
    Admin1.createTable("studentsAssignments")
    Admin1.seeValues("studentsAssignments")
    Admin1.addValues("studentsAssignments",[(322,"VijaySai","CSE",None,None,"KEY1")])
    Admin1.seeValues("studentsAssignments")
    Admin1.deleteDatabase("Plagiarismstudents")
    Admin1.closeConnection()

if __name__ == "__main__":
    main()
