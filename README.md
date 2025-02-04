# Time Calculator ⏳  
A Python function that adds a duration to a start time and returns the new time in 12-hour format, including the correct day if provided.

## Features  
- Supports **AM/PM format** with proper conversions.  
- Accepts an optional **starting day** to track the correct day of the week.  
- Handles **next-day and multiple-day calculations** automatically.  
- Returns a properly formatted **12-hour clock time**.

## Example Output 🖥️  
This script takes a start time and a duration, then calculates the new time.

### ✅ Python Code:
```python
from time_calculator import add_time

print(add_time("3:00 PM", "3:10"))           # "6:10 PM"
print(add_time("11:30 AM", "2:32", "Monday")) # "2:02 PM, Monday"
print(add_time("11:43 AM", "00:20"))         # "12:03 PM"
print(add_time("10:10 PM", "3:30"))          # "1:40 AM (next day)"
print(add_time("11:43 PM", "24:20", "Tuesday")) # "12:03 AM, Thursday (2 days later)"
print(add_time("6:30 PM", "205:12"))         # "7:42 AM (9 days later)"
```

### ✅ Expected Output:
```
6:10 PM
2:02 PM, Monday
12:03 PM
1:40 AM (next day)
12:03 AM, Thursday (2 days later)
7:42 AM (9 days later)
```

## How to Run the Script 🚀  
Clone the repository, navigate to the directory, and run the script.

```bash
# Clone the repository
git clone https://github.com/LeahLauniuvao/time-calculator-python.git

# Navigate to the directory
cd time-calculator-python

# Run the script
python time_calculator.py
```

## 🔬 Unit Testing (Optional but Recommended)  
To test the script, run:  
```bash
python test_time_calculator.py
```

## 🚀 Future Enhancements  
- Support for **24-hour format conversion**.  
- Implement a **CLI interface** for user input.  
- Add a **GUI version using Tkinter**. 
