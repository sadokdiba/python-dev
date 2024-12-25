# Grading Program

## Overview

This program takes in a dictionary of student names and their corresponding exam scores. It converts the scores into grades according to the specified grading criteria and returns a new dictionary with student names as keys and their respective grades as values.

## Requirements

- **Do not modify lines 1-7**: You are given a dictionary called `student_scores` containing student names as keys and their exam scores as values.
- The program must convert each student's score into a corresponding grade based on the following criteria:

  - **Scores 91 - 100**: Grade = `"Outstanding"`
  - **Scores 81 - 90**: Grade = `"Exceeds Expectations"`
  - **Scores 71 - 80**: Grade = `"Acceptable"`
  - **Scores 70 or lower**: Grade = `"Fail"`

## Program Description

1. **Input**: A dictionary called `student_scores` where:
   - Keys: Student names (strings)
   - Values: Student exam scores (integers)
   
2. **Processing**: Convert each score into a grade using the specified grading criteria:
   - If the score is between 91 and 100 (inclusive), the grade will be `"Outstanding"`.
   - If the score is between 81 and 90 (inclusive), the grade will be `"Exceeds Expectations"`.
   - If the score is between 71 and 80 (inclusive), the grade will be `"Acceptable"`.
   - If the score is 70 or below, the grade will be `"Fail"`.

3. **Output**: A new dictionary called `student_grades`, where:
   - Keys: Student names (same as `student_scores`)
   - Values: The corresponding grade for each student based on their score.

## Example

### Input:
```python
student_scores = {
    "John": 85,
    "Emma": 92,
    "Liam": 78,
    "Sophia": 65,
    "James": 88,
    "Olivia": 95
}
```

### Output:
```python
student_grades = {
    "John": "Exceeds Expectations",
    "Emma": "Outstanding",
    "Liam": "Acceptable",
    "Sophia": "Fail",
    "James": "Exceeds Expectations",
    "Olivia": "Outstanding"
}