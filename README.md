# Plagiarism-Detection-Project
## Collaborators should create a new branch and make pull requests in order to maintain the data privacy and security
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

###  ALGORITHMS USED 

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
1. GOWTHAN KUMAR C
   

<img width="1915" height="892" alt="Screenshot 2025-10-23 212855" src="https://github.com/user-attachments/assets/19b48547-7a43-44ad-bf75-d63bb0392df4" />
<img width="1907" height="895" alt="Screenshot 2025-10-23 212917" src="https://github.com/user-attachments/assets/337c0d7c-f44b-4446-93be-d05b03c0b1ed" />
<img width="1902" height="808" alt="Screenshot 2025-10-23 212928" src="https://github.com/user-attachments/assets/a9b2c0ba-ad0a-47ca-9ca4-7a2f289e10a3" />
2. K. VIJAYA SAI

