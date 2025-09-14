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
        self.query = "create database" + " " + name + " ;"
        self.dataBase.commit()
        self.cursorObject.execute(self.query)
        self.query = "use " + name + " ;"
        return (f"Database {name} is Created and Shifted to use")
    def seeDatabases(self):
        self.query = "show databases"
        self.cursorObject.executemany(self.query)
        self.results = self.cursorObject.fetchall()
        for x in self.results:
            print(x)
    def createTable(self,table_name):
        print(f"Creating a Table with Name {table_name}")
        self.query = "create table" + " " + table_name + " " + "(student_id int primary key,student_name varchar(60) not null,student_branch varchar(40) not null,student_filename varchar(50),student marks double) values (%s,%s,%s,%s,%s)"
        self.cursorObject.execute(self.query)
        return f"Table was created Successfully"
    def addValues(self,values):
        pass
    #Upto now this is the starting one
    
def main():
    print(f"Please Submit those Assignments before the deadline")
    #first we will create a database which consists of the students and then ask the students to enter their id and password
