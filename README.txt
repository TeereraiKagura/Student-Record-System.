===========================================================
PROJECT: STUDENT RECORD SYSTEM (MERGE SORT)
DEVELOPER:Teererai Kagura
DATE: 10 MARCH 2026   
===========================================================

1. PROJECT OVERVIEW
-------------------
This is a python desktop-based Student Record System developed to 
efficiently manage, store, and rank student data. The 
application is designed with a focus on Algorithm Efficiency 
and Data Persistence.

2. CORE FEATURES
----------------
* Data Persistence: Uses a JSON database (students.json) to 
  ensure records are saved permanently.
* Advanced Sorting: Implements a custom Merge Sort algorithm 
  to organize data by Name or Marks.
* Ranking System: Automatically calculates and displays class 
  rankings (1st, 2nd, 3rd) based on performance.
* User-Friendly GUI: Built with Python's Tkinter for a clean, 
  professional interface.

3. FILE STRUCTURE
-----------------
* main.py        - The primary script that runs the GUI and 
                   coordinates the system.
* merge_sort.py  - Contains the custom "Divide and Conquer" 
                   sorting logic.
* database.py    - Handles all reading/writing operations 
                   to the JSON file.
* students.json  - The local database file where student 
                   records are stored.

4. TECHNICAL SPECIFICATIONS
---------------------------
* Language: Python 3.x
* Algorithm: Merge Sort (Time Complexity: O(n log n))
* Data Format: JSON (JavaScript Object Notation)
* UI Library: Tkinter (with ttk Treeview)

5. HOW TO RUN
-------------
1. Ensure Python 3 is installed on your machine.
2. Place all 4 project files in the same folder.
3. Open your terminal or command prompt in that folder.
4. Run the command:  python main.py

6. NOTES FOR THE EVALUATOR
--------------------------
The system has been pre-loaded with four initial records 
(Privilege, Nyarie, Agnes, and Titus) to demonstrate the 
sorting and ranking capabilities immediately upon startup. 
New records can be added seamlessly during the demonstration.

===========================================================
Designed for academic demonstration and efficiency.
===========================================================
