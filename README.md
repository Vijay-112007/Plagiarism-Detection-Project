# Plagiarism-Detection-Project
## Collaborators should create a new branch and make pull requests in order to maintain the data privacy and security
## DATABASE THING
*This is a mini project based on **DSA (BASIC)** which consists of the plagiarism detection tool and displays the results of the plagiarism*
<u><b>Main Thing About the Project </b> </u>
<p>First we need to create a database which consists of the information about the students</p>
<ul>The table consists of the following items
<li>student_id which is a primary key</li>
<li>student_name</li>
<li>student_branch</li>
<li>student_marks which consists of the student marks</li>
<li>student_file_name which consists of the name of the student file</li>
</ul>
<u><b>Now Working with the Database</b></u>
<ol>
<li>We need to take each and every student file from the database and perform the plagiarism detection</li> 
<li>It should be like we need to select one student and perform plagiarism like and selecting all other students one by one but reverse is not possible</li>
<li>If that particular first selected student <b>file doesnt had plagiarism or had only a small percentage of plagiarism</b> ,then it should be marked accordingly</li>
<li>If there is any plagiarism thing between two students,then <b>both should be marked as accordingly</b></li>
<li>While selecting the student from the database the student_marks column of that particular student should be <b>NULL</b> to avoid multiple tests on one student</li>
<li>The students with more the <b>85% to 90%</b> will be marked least</li>
</ol>
<p><u><b>Now we need to create two point of views</b></u></p>
<ol>
<li>Student</li>
<li>Admin</li>
</ol>
<u><b>Process</b></u>
<ol>
<li>We need to give access to students to submit their files</li>
<li>Then we need to perform the test after getting all the files(Say as Assignments) from the students</li>
<li>First we need to create a database to store the information about the students</li>
<li>The student file should be starting with his name (optional) where we can create a seed and store it in dbms for easy access which can be like candidate key</li>
<li>After all the submissions we will perform the test</li>

<li>hello</li>
<li>Like the thing mentioned above we will perform the test</li>
</ol>

PHASE 2: ALGORITHMS TO DETECT PLAGIARISM IN PYTHON 
## PREPROCESSOR CLASS
## PHASE 1: TEXT PREPROCESSING

## PREPROCESSOR CLASS

The `Preprocessor` class handles the preprocessing of student submissions:
- Clean text by removing special characters and normalizing
- Tokenize text into individual words  
- Count word frequency using Counter
- Store results as JSON in the database

## PREPROCESSING WORKFLOW

### Step 1: Initialize Preprocessor
- Connect to database using Admin credentials
- Set up submissions folder path
- Pre-compile regex patterns for performance

### Step 2: Ensure Preprocessed Column
- Check if `preprocessed_data` column exists in table
- Create column if it doesn't exist
- Handle table recreation if needed

### Step 3: Retrieve Student Files
- Fetch all student records with filenames from database
- Validate that files exist in submissions directory

### Step 4: Text Processing Pipeline
For each student file:
1. Read file content with UTF-8 encoding
2. Clean text: lowercase, remove non-alpha characters, normalize spaces
3. Tokenize: split into individual words
4. Count frequency: using Collections.Counter
5. Convert to JSON: for database storage

### Step 5: Batch Database Update
- Store all processed data in batch
- Update `preprocessed_data` column for each student
- Handle individual updates if batch fails

### Step 6: Status Reporting
- Generate comprehensive processing report
- Show success/error counts
- Display processing time statistics

### KEY METHODS

- `clean_text()`: Normalizes and cleans raw text input
- `tokenize()`: Splits clean text into tokens/words
- `word_freq()`: Counts frequency of each token
- `freq_to_json()`: Converts Counter to JSON string
- `ensure_preprocessed_column()`: Manages database schema
- `preprocess_files()`: Main processing workflow controller

### PERFORMANCE FEATURES

- Pre-compiled regex patterns for faster text cleaning
- Batch database updates to reduce connection overhead
- UTF-8 encoding support for international characters
- Comprehensive error handling and logging
- Memory-efficient processing of large files

##  ALGORITHMS USED 

This Program integrates and uses three classical algorithms from the world of Data Structures and Algorithms(DSA)

#### Knuth–Morris–Pratt (KMP)
- USE Prefix Table to skip repeated comparisons
- DETECT matching substrings with linear time complexity O(n)

####  Boyer–Moore
- Works backwards
- Uses the PATTERN of bad character and good suffix 
- Super fast for large texts
  

#### Rabin–Karp
- Uses the famous rolling hash technique to find substring matches based on hash values.  
- Allows quick detection of identical sequences across documents.

Each of the algorithms returns the number of substrings, and then we find the average of those three to get the final result


### DATA STRUCTURES USED 

- PREFIX TABLE (KMP) : We use **list** to store the prefix or suffix to overlap lengths for efficient pattern skipping
- Boyer Moore : We use **Array** to store the last occurrence index of the characters
- Rabin Karp: **Hash values** are used as we use rolling hash to make it efficient for large data sets we can use larger hash values 
- Records from SQL : **Dictionary** is used as it allows easy access of records and fields 
- Pairwise Comparison: **List of Tuples** are used to store unique records 





### WORKFLOW 

1. **Step 1:** Connect to the existing database **`PlagiarismStudents`**.  
2. **Step 2:** Fetch all records from the **`preprocessed_submissions`** table.  
3. **Step 3:** Generate all possible unique pairs of students using `itertools.combinations`.  
4. **Step 4:** For each pair:  
   - Extract their `clean_text`. 
   - Compute similarity using **KMP**, **Boyer–Moore**, and **Rabin–Karp**.  
   - Average the results.  
5. **Step 5:** Print results and optionally save them back to SQL

## WORK PROGRESS OF EACH CONTRIBUTOR OF THIS PROJECT
1. GOWTHAN KUMAR C :- Total - 23 Commits
   
<ol>
<li>
  <img width="1915" height="892" alt="Screenshot 2025-10-23 212855" src="https://github.com/user-attachments/assets/19b48547-7a43-44ad-bf75-d63bb0392df4" />
</li>

<li>
  <img width="1907" height="895" alt="Screenshot 2025-10-23 212917" src="https://github.com/user-attachments/assets/337c0d7c-f44b-4446-93be-d05b03c0b1ed" />
</li>

<li>
  <img width="1902" height="808" alt="Screenshot 2025-10-23 212928" src="https://github.com/user-attachments/assets/a9b2c0ba-ad0a-47ca-9ca4-7a2f289e10a3" />
</li>
</ol>
2. K. VIJAYA SAI :- Total - 22 Commits
<ol>

<li>
  <img width="1909" height="692" alt="Screenshot 2025-10-23 213349" src="https://github.com/user-attachments/assets/7ddc459e-afb3-4d21-a07d-e442d3398dac" />
</li>

<li>
  <img width="1915" height="797" alt="Screenshot 2025-10-23 213403" src="https://github.com/user-attachments/assets/0a51d721-e14c-4c42-805b-77e89c1883c8" />
</li>

<li>
  <img width="1795" height="786" alt="Screenshot 2025-10-23 213416" src="https://github.com/user-attachments/assets/2d9d912e-da35-4b64-bab4-191a47f615c3" />
</li>

</ol>

3.T. GURU CHARAN :- Total - 2 Commits
<ol>
  <li>
    <img width="1766" height="492" alt="Screenshot 2025-10-23 214150" src="https://github.com/user-attachments/assets/dc6e7d1b-20b7-4e83-be5a-87a30c3645f1" />
  </li>
</ol>

4. V. Sooraj :- Total - 1 Commits
<ol>
  <li>
    <img width="1715" height="243" alt="Screenshot 2025-10-23 214524" src="https://github.com/user-attachments/assets/ac974122-e9f2-44cb-a526-1fe0b2716636" />
  </li>
</ol>
