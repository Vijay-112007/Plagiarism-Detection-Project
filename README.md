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
<li>Like the thing above mentioned we will perform the test</li>
</ol>
