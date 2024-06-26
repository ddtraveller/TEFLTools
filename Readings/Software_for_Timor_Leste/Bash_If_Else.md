# Bash Control Structures, Functions, and Error Handling

## I. Control Structures

### If-else statements
If-else statements allow you to execute different commands based on a condition. The basic syntax is as follows:

```bash
if [ condition ]; then
    # commands to execute if condition is true
else
    # commands to execute if condition is false
fi
```

You can also use `elif` to add additional conditions:

```bash
if [ condition1 ]; then
    # commands to execute if condition1 is true
elif [ condition2 ]; then
    # commands to execute if condition2 is true
else
    # commands to execute if all conditions are false
fi
```

Example:
```bash
age=25
if [ $age -lt 18 ]; then
    echo "You are a minor."
elif [ $age -ge 18 ] && [ $age -lt 65 ]; then
    echo "You are an adult."
else
    echo "You are a senior citizen."
fi
```

### Case statements
Case statements provide a way to match a value against multiple patterns and execute corresponding commands. The syntax is as follows:

```bash
case $variable in
    pattern1)
        # commands to execute if variable matches pattern1
        ;;
    pattern2)
        # commands to execute if variable matches pattern2
        ;;
    *)
        # default commands to execute if no match
        ;;
esac
```

Example:
```bash
day="Monday"
case $day in
    "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday")
        echo "It's a weekday."
        ;;
    "Saturday"|"Sunday")
        echo "It's the weekend."
        ;;
    *)
        echo "Invalid day."
        ;;
esac
```

### For loops
For loops allow you to iterate over a list of items and execute commands for each item. The syntax is as follows:

```bash
for item in list; do
    # commands to execute for each item
done
```

Example:
```bash
fruits=("apple" "banana" "orange")
for fruit in "${fruits[@]}"; do
    echo "I like $fruit."
done
```

### While loops
While loops execute a set of commands repeatedly as long as a condition is true. The syntax is as follows:

```bash
while [ condition ]; do
    # commands to execute while condition is true
done
```

Example:
```bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### Demonstration and practice exercises

1. Write a script that checks if a number is positive, negative, or zero.
2. Write a script that displays the name of the day based on a number (1-7).
3. Write a script that calculates the factorial of a given number using a for loop.
4. Write a script that prompts the user to enter a password until the correct password is entered.

## II. Functions and Error Handling

### Defining and calling functions
Functions are reusable blocks of code that can be defined and called within a Bash script. To define a function, use the following syntax:

```bash
function_name() {
    # commands to execute when the function is called
}
```

To call a function, simply use its name followed by parentheses:

```bash
function_name
```

Example:
```bash
greet() {
    echo "Hello, $1!"
}

greet "John"
greet "Alice"
```

### Return values
Functions can return values using the `return` statement followed by a number. The return value can be accessed using the `$?` variable after calling the function.

Example:
```bash
is_even() {
    if [ $((number % 2)) -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

number=4
is_even $number
if [ $? -eq 0 ]; then
    echo "$number is even."
else
    echo "$number is odd."
fi
```

### Basic error handling (exit codes, ||, &&)
Bash provides mechanisms for basic error handling:

- `exit` statement: Use `exit` followed by a number to terminate the script with a specific exit code (0 for success, non-zero for errors).
- `||` (OR) operator: Use `command1 || command2` to execute `command2` only if `command1` fails.
- `&&` (AND) operator: Use `command1 && command2` to execute `command2` only if `command1` succeeds.

Example:
```bash
# Check if a file exists
if [ -f "file.txt" ]; then
    echo "File exists."
else
    echo "File not found." >&2
    exit 1
fi

# Combining commands with || and &&
command1 && command2 || command3
```

### Debugging techniques (set -x)
Bash provides debugging options to help troubleshoot scripts:

- `set -x`: Enables trace mode, which prints each command before executing it.
- `set +x`: Disables trace mode.

Example:
```bash
set -x
# Commands to debug
set +x
```

## Practice Exercises

1. Write a function that takes a number as an argument and returns the square of that number.
2. Write a script that accepts a file name as an argument and checks if the file exists. If the file doesn't exist, display an error message and exit with a non-zero status.
3. Write a script that uses a while loop to read lines from a file and process them using a case statement based on the first character of each line.
4. Write a script that defines a function to calculate the average of an array of numbers. Use error handling to check if the array is empty and return an appropriate exit code.

## Conclusion

In this expanded guide, we covered Bash control structures, functions, and error handling. We explored if-else statements, case statements, for loops, and while loops, providing examples and practice exercises for each. We also learned how to define and call functions, return values from functions, and handle errors using exit codes and logical operators. Additionally, we discussed basic debugging techniques using `set -x`.

Mastering control structures, functions, and error handling is crucial for writing effective and robust Bash scripts. By utilizing these concepts, you can create scripts that make decisions based on conditions, reuse code through functions, and handle errors gracefully.

Remember to practice writing scripts that incorporate these concepts and test them thoroughly. Refer to the Bash manual (`man bash`) and online resources for further information and advanced techniques.

Happy scripting!