import mysql.connector 
import re
import itertools
from main1 import Preprocessor
from collections import Counter

DB_SETTINGS = {
    "host": "localhost",
    "user": "root",           
    "password": "Vijay@112007",   
    "database": "PlagiarismStudents"
}

TABLE_NAME= "preprocessed_submissions"


def kmp_match_count(document,snippet):
    prefix=[0]*len(snippet)
    build_prefix_table(snippet,prefix)
    i=0
    j=0
    total=0

    while i<len(document):
        if snippet[j]==document[i]:
            i=i+1
            j=j+1

        if j==len(snippet):
        total = total + 1
        j=prefix[j-1]
        elif i < len(document) and snippet[j] != document[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return total

   
    
def build_prefix_table(pattern,prefix):
    index=1
    length=0
    while index<len(pattern):
        if pattern[index]==pattern[length]:
            length= length + 1
            prefix[index] = length
            index = index + 1
        else:
            if length!=0:
                length = prefix[length - 1]
            else:
                prefix[index]=0
                index = index + 1

def boyer_moore_match_count(document,snippet):
    m=len(snippet)
    n=len(document)
    if m == 0: 
        return 0
    bad_char_table= [-1]*256
    for i in range(m):
        bad_char_table[ord(snippet[i])]=i

    shift=0
    found=0
    while shift <= n-m:
        j = m-1
        while j>=0 and snippet[j]== document[shift + j]:
            j= j -1
        if j<0:
            found+=1
            if shift + m < n:        # 🔹 Explicit check instead of ternary
                shift += m - bad_char_table[ord(document[shift + m])]
            else:
                shift += 1
        else:
            shift += max(1, j - bad_char_table[ord(document[shift + j])])
    return found


def rabin_karp_match_count(document,snippet,prime_val=101):
    d=256
    m=len(snippet)
    n=len(document)
    if m>n:
        return 0
    h=pow(d,m-1) % prime_val
    hash_snippet=0
    hash_doc=0
    occurrences=0
    
    for i in range(m):
        hash_snippet=(d*hash_snippet + ord(snippet[i])) % prime_val 
        hash_doc=(d*hash_doc + ord(document[i])) % prime_val
    for i in range(n-m+1):
        if hash_snippet == hash_doc and document[i:i+m]==snippet:
            occurrences +=1
        if i < n - m:
            hash_doc = (d * (hash_doc - ord(document[i]) * h) + ord(document[i + m])) % prime_val
            
            if hash_doc <0: 
              hash_doc += prime_val 
    return occurrences

    


    





    
        
