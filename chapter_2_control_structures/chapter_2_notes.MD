# Chapter 2 Notes

## What are Conditional Statements?
- Conditional statements are used to execute code only when a certain condition is true. They allow you to control the flow of your program.
    - Basics Syntax 
        1. if condition: code block executed if condition is true
        2. elif another_condition: code block executed if the second condition is true
        3. else: code block executed if no condition are true

## How It Works: 
1. if Statement: 
    - The if statement checks a condition. If the condition evaluates to True, the code block indented beneath it runs.
2. elif Statement (optional):
    - Stands for "else if." It allows you to check multiple conditions.
3. else Statement (optional):
    - If none of the if or elif conditions are met, the else block runs.
4. For Loops:
    - Looping through lists, tuples, and ranges.
    - Practical examples: Iterating over data
5. While Loops:
    - Syntax: Reapeating a block of code while a condition is True.

## Example Code
temp = 45  

if temp < 50:  
    print("It's cold outside!")  
elif temp == 50:  
    print("It's exactly 50 degrees.")  
else:  
    print("It's warm outside!")  

## Comparison Operators 
- ==: Equal to
- !=: not equal to
- .> Greater than
- .< Less than
- .>= Greater than or equal to
- .<= Less than or equal to

## Logical Operators 
- and: Returns True if both conditions are true
- or: Returns True if at least one conditions is true.
- not: Negates the condition. 

