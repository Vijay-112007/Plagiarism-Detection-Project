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
    if not snippet or not document:  # handle empty strings
        return 0
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

def boyer_moore_match_count(document, snippet):
    if not snippet or not document:  # handle empty strings
        return 0
    m = len(snippet)
    n = len(document)
    if m == 0:
        return 0

    bad_char_table = [-1] * 256
    for i in range(m):
        bad_char_table[ord(snippet[i])] = i

    shift = 0
    found = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and snippet[j] == document[shift + j]:
            j -= 1

        if j < 0:
            found += 1
            if shift + m < n:
                shift += m - bad_char_table[ord(document[shift + m])]
            else:
                shift += 1
        else:
            shift += max(1, j - bad_char_table[ord(document[shift + j])])

    return found
def rabin_karp_match_count(document,snippet,prime_val=101):
    if not snippet or not document:  # handle empty strings
        return 0
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
def build_prefix_table(pattern, prefix):
    index = 1
    length = 0
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        else:
            if length != 0:
                length = prefix[length - 1]
            else:
                prefix[index] = 0
                index += 1

def kmp_match_count(document, snippet):
    if not snippet or not document:
        return 0
    prefix = [0] * len(snippet)
    build_prefix_table(snippet, prefix)
    i = j = total = 0
    while i < len(document):
        if snippet[j] == document[i]:
            i += 1
            j += 1
        if j == len(snippet):
            total += 1
            j = prefix[j - 1]
        elif i < len(document) and snippet[j] != document[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return total

def boyer_moore_match_count(document, snippet):
    m = len(snippet)
    n = len(document)
    if m == 0 or n == 0 or m > n:
        return 0
    bad_char_table = [-1] * 256
    for i in range(m):
        bad_char_table[ord(snippet[i])] = i
    shift = 0
    found = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and snippet[j] == document[shift + j]:
            j -= 1
        if j < 0:
            found += 1
            shift += (m - bad_char_table[ord(document[shift + m])] if shift + m < n else 1)
        else:
            shift += max(1, j - bad_char_table[ord(document[shift + j])])
    return found

def rabin_karp_match_count(document, snippet, prime_val=101):
    d = 256
    m = len(snippet)
    n = len(document)
    if m == 0 or m > n:
        return 0
    h = pow(d, m - 1) % prime_val
    hash_snippet = 0
    hash_doc = 0
    occurrences = 0
    for i in range(m):
        hash_snippet = (d * hash_snippet + ord(snippet[i])) % prime_val
        hash_doc = (d * hash_doc + ord(document[i])) % prime_val
    for i in range(n - m + 1):
        if hash_snippet == hash_doc and document[i:i + m] == snippet:
            occurrences += 1
        if i < n - m:
            hash_doc = (d * (hash_doc - ord(document[i]) * h) + ord(document[i + m])) % prime_val
            if hash_doc < 0:
                hash_doc += prime_val
    return occurrences

def similarity_score(doc1, doc2, algo="kmp"):
    snippet_len = min(30, len(doc2))
    snippet = doc2[:snippet_len]
    if algo == "kmp":
        matches = kmp_match_count(doc1, snippet)
    elif algo == "bm":
        matches = boyer_moore_match_count(doc1, snippet)
    elif algo == "rk":
        matches = rabin_karp_match_count(doc1, snippet)
    else:
        raise ValueError("Unknown algorithm")
    return round((matches / max(1, len(doc1))) * 1000, 2)

def fetch_texts():
    conn = mysql.connector.connect(**DB_SETTINGS)
    cur = conn.cursor()
    cur.execute(f"SELECT student_id, clean_text FROM {TABLE_NAME}")
    data = cur.fetchall()
    conn.close()
    return data

def run_detection():
    data = fetch_texts()
    if len(data) < 2:
        print("Not enough preprocessed submissions for comparison.")
        return
    print(f"\nRunning Plagiarism Detection on {len(data)} submissions...\n")
    results = []
    for (id1, text1), (id2, text2) in itertools.combinations(data, 2):
        kmp_score = similarity_score(text1, text2, "kmp")
        bm_score = similarity_score(text1, text2, "bm")
        rk_score = similarity_score(text1, text2, "rk")
        avg_score = round((kmp_score + bm_score + rk_score) / 3, 2)
        results.append((id1, id2, kmp_score, bm_score, rk_score, avg_score))
        print(f"[{id1} vs {id2}]  KMP={kmp_score}%  BM={bm_score}%  RK={rk_score}%  → Avg={avg_score}%")
    print("\nDetection completed.\n")
    return results

if __name__ == "__main__":
    run_detection()

    





    
        
