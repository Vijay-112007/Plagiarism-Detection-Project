#This is the integrated code of the database.py and preprocessing.py files
#the database.py is done by K.Vijaya sai and preprocessing.py is done by T.Guru charan
#The integration of both files is done by K.Vijaya Sai
#This is one of the main code which is related with the database and consists of the things related to the dbms
import mysql.connector
import random
import os
import math
import time
import re
import json
from collections import Counter

def seedGenerate(student_id,password):
    seedValue = str(student_id) + str(password)
    return seedValue

def keyGenerate(seedValue):
    random.seed(seedValue)
    key = random.randint(00000,99999)
    return key

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
        self.query = f"create table if not exists {table_name} (student_id int primary key,student_name varchar(60) not null,student_branch varchar(40) not null,student_filename varchar(50),student_marks double,student_seed varchar(50) unique not null)"
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
        self.query = f"insert into {table_name} (student_id,student_name,student_branch,student_filename,student_marks,student_seed) values(%s,%s,%s,%s,%s,%s)"
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
#first we need to give time to students to submit those assignments student is the extension of the Admin class
class Students(Admin):
    #Now we need to work in the student point of view
    """
    first we will ask the student for this id and password then we will perform authentication
    """
    def __init__(self,student_id,password):
        self.student_id = student_id
        self.password = password
        self.authentication = False
    def authentication_system(self,database_connection):
        #Now we will perform the authentication which is like checking the key and student_id from the database
        #First we need to connect to the database serve
        self.database_connection = database_connection
        #we need to get the key from the database for the comparison
        query = "select student_seed from studentsAssignments where student_id = %s"
        value = (self.student_id,)
        self.cursorb = self.database_connection.cursor()
        self.cursorb.execute(query,value)
        self.seed1 = seedGenerate(self.student_id,self.password)
        self.seed2 = self.cursorb.fetchone()
        if self.seed2 and keyGenerate(self.seed1) == keyGenerate(self.seed2[0]):
            self.authentication = True
        else:
            self.authentication = False
    #now after authentication the student can submit the files
    def submitFiles(self,file_path):
        #now we need to do two things first we need to store the files with content in the admin and then store the name of the file in the database
        if not self.authentication:
            print("Authentication is Required.Please Login first")
            return
        submission_directory = os.path.join(os.getcwd(),"submissions")
        if not os.path.exists(submission_directory):
            os.makedirs(submission_directory)
        #Now copy the file content in a new file which is createed in the directory
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(submission_directory,file_name)
        try:
            with open(file_path,'rb') as fd:
                content = fd.read()
            with open(destination_path,'wb') as fd:
                fd.write(content)
            print(f"File {file_name} is succesfully submitted")
        except Exception as e:
            print(f"Failed to submit the file: {e}")
            return
        #now update the database with the filename
        try:
            query = "UPDATE studentsAssignments SET student_filename = %s WHERE student_id = %s"
            values = (file_name, self.student_id)
            self.cursorb.execute(query, values)
            self.database_connection.commit()
            print("Database updated with submitted filename.")
        except Exception as e:
            print(f"Failed to update database: {e}")
            return

# ---------- PREPROCESSOR CLASS (SECOND CODE INTEGRATED) ----------
class Preprocessor(Admin):
    """
    This class handles the preprocessing of student submissions:
    - clean text
    - tokenize
    - count word frequency
    - store results in a separate table in the database
    """
    def __init__(self,password):
        super().__init__(password)
        self.submissions_folder = os.path.join(os.getcwd(),"submissions")

    # Method to clean the text
    def clean_text(self,text:str)->str:
        text = text.lower()
        text = re.sub(r"[^a-z\s]", " ", text)  # remove non-letter characters
        text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
        return text

    # Method to split text into tokens
    def tokenize(self,text:str):
        return text.split()

    # Method to count word frequency
    def word_freq(self,tokens):
        return Counter(tokens)

    # Convert Counter to JSON string
    def freq_to_json(self,counter:Counter)->str:
        return json.dumps(dict(counter), ensure_ascii=False)

    # Main preprocessing method
    def preprocess_files(self,source_table="studentsAssignments"):
        print("Starting preprocessing of student submissions...")

        # Ensure preprocessing table exists
        create_stmt = """
        CREATE TABLE IF NOT EXISTS preprocessed_submissions (
            student_id INT PRIMARY KEY,
            clean_text TEXT,
            word_freq_json LONGTEXT
        )
        """
        self.cursorObject.execute(create_stmt)
        self.dataBase.commit()

        # Fetch student rows from source table
        q = f"SELECT student_id, student_filename FROM {source_table}"
        self.cursorObject.execute(q)
        rows = self.cursorObject.fetchall()

        if not rows:
            print("No student records found.")
            return

        for sid, fname in rows:
            if not fname:
                continue
            path = os.path.join(self.submissions_folder, fname)
            if not os.path.exists(path):
                print(f"[missing] File for ID={sid} not found: {path}")
                continue

            try:
                with open(path,"r",encoding="utf-8") as f:
                    raw = f.read()
            except Exception as e:
                print(f"Error reading file {fname}: {e}")
                continue

            cleaned = self.clean_text(raw)
            tokens = self.tokenize(cleaned)
            freq = self.word_freq(tokens)
            freq_json = self.freq_to_json(freq)

            # Insert or update the preprocessing table
            upsert = """
            INSERT INTO preprocessed_submissions (student_id, clean_text, word_freq_json)
            VALUES (%s,%s,%s)
            ON DUPLICATE KEY UPDATE
              clean_text=VALUES(clean_text),
              word_freq_json=VALUES(word_freq_json)
            """
            self.cursorObject.execute(upsert,(sid,cleaned,freq_json))
            self.dataBase.commit()
            print(f"[ok] ID={sid} processed | tokens={len(tokens)} | unique={len(freq)}")

        print("Preprocessing completed.")

# ---------- TEST MAIN ----------
def main():
    # Pseudo test case simulation
    print("Please Submit those Assignments before the deadline")

    # Step 1: Create Admin and database
    Admin1 = Admin("Vijay@112007")
    Admin1.seeDatabases()
    Admin1.createDatabase("PlagiarismStudents")
    Admin1.seeDatabases()
    Admin1.useDatabase("PlagiarismStudents")
    Admin1.createTable("studentsAssignments")
    Admin1.seeValues("studentsAssignments")

    # Step 2: Add test student data
    try:
        Admin1.addValues("studentsAssignments", [(322, "VijaySai", "CSE", None, None, "KEY1")])
    except mysql.connector.errors.IntegrityError:
        print("[Warning] Student ID 322 already exists. Skipping insertion.")
    Admin1.seeValues("studentsAssignments")

    # Step 3: Run preprocessing
    Prep = Preprocessor("Vijay@112007")
    Prep.useDatabase("PlagiarismStudents")
    Prep.preprocess_files()

    # Step 4: Verification of preprocessed data
    Admin1.dataBase.commit()  # ensure all changes are committed
    Admin1.cursorObject.close()  # close old cursor
    Admin1.cursorObject = Admin1.dataBase.cursor()  # create new cursor

    Admin1.cursorObject.execute("SELECT * FROM preprocessed_submissions")
    rows = Admin1.cursorObject.fetchall()
    print("\n--- Preprocessed Data Verification ---")
    for row in rows:
        sid, clean_text, freq_json = row
        print(f"Student ID: {sid}")
        print(f"Cleaned Text: {clean_text}")
        print(f"Word Frequencies (JSON): {freq_json}\n")

    # Step 5: Cleanup for next run
    Admin1.deleteDatabase("PlagiarismStudents")

    # Step 6: Close connections
    Admin1.closeConnection()
    Prep.closeConnection()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
