# CMSC414-SQL-Injection

SQL Injection
Michael Joyner & Nathaniel Ekanem

Objective or main idea of the project
SQL Injection is a technique used to gain access to unauthorized information from a hospital database, such as passwords, medical history, payment information, etc. Allows attackers to spoof identity and tamper with existing data
The attack exploits the vulnerabilities of the database software
How to Prevent SQL Injection:
The best way to prevent SQL injection attacks seems to be input validations and parameterized queries including prepared statements.
The Database has to be made robust enough to care for potential malicious code elements like single quotes.
Turn off visibility of database errors on production side
List of tasks along with their description, and execution and completion timeline
Proposal Submission Deadline: Feb 24 
Research databases, SQL injections and solutions 
Outline Project
Progress Report Deadline: March 31
Build database
Build SQL injection
Build fix
Write Report
Project Submission Deadline: April 26
Test SQL injection & fix
Create presentation and Demo video


Evaluation approach of the prototype to verify that your attack or solution works
When entering the SQL injection we expect to be able to see passwords for hospital staff, and sensitive patient information such as social security numbers, medical history, and any payment methods they have with the hospital.
After confirming that our SQL injection works, we will then update our database with our “fixed” code and attempt to run our SQL injection again. This time we should fail to receive any user passwords or sensitive patient information.
Create SQL test files to test for potential vulnerabilities before the attack


Name and student IDs of group members
Michael Joyner V00802791
Nathaniel Ekanem V00826653
Role and work scope of each group member
Michael
Research SQL injections and solutions
Build SQL injection & fix
Test SQL fix
Create presentation
Write up Progress Report 
Nathaniel
Research SQL injections and solutions
Build database & fix
Test SQL injection
Create demo
Write up Progress Report

