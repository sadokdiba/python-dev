# Love Calculator 💖

## Overview
The Love Calculator is a fun little program that calculates the compatibility between two names. It works by counting the occurrences of the letters in the words "TRUE" and "LOVE" in both names, and then calculates a two-digit love score based on the sum of those occurrences.

## How It Works
The `calculate_love_score()` function checks for the number of occurrences of each letter in the words "TRUE" and "LOVE" in the two given names, and then forms a two-digit number by combining the counts.

### Steps:
1. **TRUE Calculation:** The function checks how many times each letter from the word "TRUE" appears in both names.
   - Count the occurrences of 'T', 'R', 'U', 'E' in both names and add them together to form a total score.
   
2. **LOVE Calculation:** The function then checks how many times each letter from the word "LOVE" appears in both names.
   - Count the occurrences of 'L', 'O', 'V', 'E' in both names and add them together to form a second total score.

3. **Love Score:** Combine the two totals to form a two-digit love score. The first digit comes from the "TRUE" total, and the second digit comes from the "LOVE" total.

### Example
If you call the function `calculate_love_score("Kanye West", "Kim Kardashian")`, the calculation would look something like this:

- TRUE Calculation: 
    - T occurs 1 time
    - R occurs 1 time
    - U occurs 1 time
    - E occurs 2 times
    - Total for "TRUE" = 1 + 1 + 1 + 2 = 5
    
- LOVE Calculation:
    - L occurs 1 time
    - O occurs 1 time
    - V occurs 0 times
    - E occurs 2 times
    - Total for "LOVE" = 1 + 1 + 0 + 2 = 4

The final love score would be `54`.

### Example Output:
```python
calculate_love_score("Kanye West", "Kim Kardashian")
# Output: 54
