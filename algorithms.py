import mysql.connector 
import re
import itertools

DB_CONFIG = {
    "host": "localhost",
    "user": "root",           
    "password": "PASSWORD",   
    "database": "PlagiarismStudents"
}

TABLE_NAME= "preprocessed_submissions"


def kmp_match_count(document,snippet):
    prefix=[0]*len(snippet)
    build_prefix_table(snippet,prefix)
    i=j=total=0

   while i<len(document):
       if snippet[j]==document[i]
       i=i+1
       j=j+1

   if j==len(snippet)
      total = total + 1
      j=prefix[j-1]
   elif i < len(document) and snippet[j] != document[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return total

   
    
