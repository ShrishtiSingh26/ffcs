# University Management System

A Python program that manages student and faculty data for a university. The system allows you to:
- Load student and faculty details from CSV files.
- Get the class size for a given faculty member.
- Get a list of students for a given faculty.
- Retrieve the details of a student or faculty.
- Get the faculty member who teaches a particular subject.

## Features
- **Student Management:** Store student information, including electives and class numbers.
- **Faculty Management:** Store faculty information, including subjects they teach and their specialization.
- **Class Size Query:** Check the number of students enrolled in each subject taught by a faculty member.
- **Student List Query:** Get a list of students enrolled in a particular subject.
- **Student and Faculty Details Query:** Fetch detailed information about a specific student or faculty.
  
## Files
- **student.csv:** CSV file containing student information.
- **faculty.csv:** CSV file containing faculty information.

## Project Structure
```plaintext
.
├── faculty.csv          # Contains faculty details
├── student.csv          # Contains student details
├── university_system.py # Main Python program
└── README.md            # This file
```

## CSV File Format

### student.csv
The `student.csv` file should contain the following columns:
- **Student ID**: The unique ID of the student.
- **Name**: The name of the student.
- **Elective X**: The name of the elective subject the student has enrolled in (X is a number from 1 to 5).
- **Elective X Class Number**: The class number for each elective.

Example:
```csv
Student ID,Name,Elective 1,Elective 1 Class Number,Elective 2,Elective 2 Class Number
1,John Doe,Mathematics,101,Physics,102
2,Jane Smith,Chemistry,103,Mathematics,101
```

### faculty.csv
The `faculty.csv` file should contain the following columns:
- **ID**: The unique ID of the faculty member.
- **Name**: The name of the faculty member.
- **Specialization**: The specialization of the faculty member.
- **Subject X**: The name of the subject the faculty teaches (X is a number from 1 to 3).
- **Subject X Class Number**: The class number for each subject.

Example:
```csv
ID,Name,Specialization,Subject 1,Subject 1 Class Number,Subject 2,Subject 2 Class Number
101,Dr. Alice Brown,Physics,Physics,102,Mathematics,101
102,Dr. Bob White,Chemistry,Chemistry,103,Mathematics,101
```

## Requirements
- Python 3.x
- `csv` library (comes pre-installed with Python)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShrishtiSingh26/university-management-system.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd university-management-system
   ```

3. **Ensure you have the required CSV files:**
   Place `student.csv` and `faculty.csv` in the same directory as the script.

4. **Run the program:**
   ```bash
   python university_system.py
   ```

   The program will present a menu with options to choose from:
   1. Get class size for a faculty.
   2. Get the student list for a faculty.
   3. Get student details.
   4. Get faculty details.
   5. Quit the program.

## Example Usage

### Option 1: Get Class Size for a Faculty
- **Input:** `faculty ID`
- **Output:** The class size for each subject taught by that faculty.

### Option 2: Get Student List for a Faculty
- **Input:** `faculty ID`
- **Output:** A list of students enrolled in the subjects taught by the faculty.

### Option 3: Get Student Details
- **Input:** `student ID`
- **Output:** Student's name and a list of electives they are enrolled in, along with the name of the faculty member teaching the subject.

### Option 4: Get Faculty Details
- **Input:** `faculty ID`
- **Output:** Faculty's name, specialization, and the subjects they teach.

### Option 5: Quit
- Exits the program.


## Contributions
Contributions are welcome! Please fork the repository, create a new branch, make your changes, and submit a pull request.
