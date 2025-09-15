#This is one of the main code which is related with the database and consists of the things related to the dbms
import mysql.connector
import random
import os
import math
import time
#first we need to give time to students to submit those assignments
class Students:
    pass
class User:
    def __init__(self,password):
        self.dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = password,
        )
        self.cursorObject = self.dataBase.cursor() 
    def createDatabase(self,name):
        self.query = "create database " + name + " ;"
        self.cursorObject.execute(self.query)
        self.dataBase.commit()
        self.query = "use " + name + " ;"
        self.cursorObject.execute(self.query)
        return (f"Database {name} is Created and Shifted to use")
    def seeDatabases(self):
        self.query = "show databases"
        self.cursorObject.executemany(self.query)
        self.results = self.cursorObject.fetchall()
        for x in self.results:
            print(x)
    def createTable(self,table_name):
        print(f"---Creating a Table with Name {table_name}---")
        self.query = "create table" + " " + table_name + " " + "(student_id int primary key,student_name varchar(60) not null,student_branch varchar(40) not null,student_filename varchar(50),student_marks double)"
        self.cursorObject.execute(self.query)
        self.dataBase.commit()
        return f"Table was created Successfully"
    def addValues(self,table_name,values):
        #first we will ask the user to enter connect the database if connected no need
        print(f"-----Printing the Table before Adding the Values----")
        self.query = "select*from" + " " + table_name + ";"
        self.cursorObject.execute(self.query)
        self.results = self.cursorObjectfetchall()
        for x in self.results:
            print(x)
        print(f"----Adding the Values----")
        self.query = "insert into " + table_name + " (student_id,student_name,student_branch,student_filename,student_marks) values(%s,%s,%s,%s,%s)"
        self.cursorObject.executemany(self.query,values)
        self.dataBase.commit()
        print("---Insertion Successfull---")
    def seeValues(self,table_name):
        #TO see the values or the entire table with the tuples 
        self.query = "select*from" + " " + table_name + ";"
        self.cursorObject.execute(self.query)
        self.results = self.cursorObject.fetchall()
        for x in self.results:
            print(x)
        print("===Values===")
    #Upto now this is the starting one
    
def main():
    print(f"Please Submit those Assignments before the deadline")
    #first we will create a database which consists of the students and then ask the students to enter their id and password
