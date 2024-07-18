# ## Learning Unit 6

## Learning Unit 6: Shell Scripting Basics
- Objectives:
  * Understand shell scripting fundamentals
  * Create basic automation scripts
- Topics:
  * Shell script structure and syntax
  * Variables, loops, and conditionals
  * Command substitution and piping
- Activities:
  * Write a script to automate daily system checks
  * Create a backup script for important system files

## Unit Resources

# Shell Scripting Basics Resources

## Lecture Notes

### Shell Script Structure and Syntax

- Shell scripts are text files containing a series of commands
- First line typically starts with a shebang (#!) followed by the path to the interpreter
- Example: #!/bin/bash
- Comments start with #
- Commands are executed sequentially, one per line
- Can use \ for line continuation
- Scripts should have executable permissions (chmod +x script.sh)
- Run scripts with ./script.sh or bash script.sh

### Variables

- Declare variables: VARIABLE_NAME=value (no spaces around =)
- Access variables with $VARIABLE_NAME
- Use quotes for values with spaces: NAME="John Doe"
- Special variables:
  - $0: Script name
  - $1, $2, etc.: Command-line arguments
  - $#: Number of arguments
  - $@: All arguments as separate words
  - $?: Exit status of last command

### Loops and Conditionals

#### For loops
```bash
for item in list
do
    # commands
done
```

#### While loops
```bash
while [ condition ]
do
    # commands
done
```

#### If statements
```bash
if [ condition ]
then
    # commands
elif [ condition ]
then
    # commands
else
    # commands
fi
```

### Command Substitution and Piping

- Command substitution: $(command) or `command`
- Captures output of a command to use in script
- Piping: command1 | command2
- Sends output of command1 as input to command2

## Discussion Questions

1. How can shell scripting improve system administration tasks?
2. What are some potential security concerns when writing shell scripts?
3. How do variables in shell scripts differ from variables in other programming languages?
4. In what scenarios would you choose a for loop over a while loop, or vice versa?
5. How can command substitution and piping be combined to create powerful scripts?

## Writing Exercises

1. Write a shell script that prompts the user for their name and favorite color, then prints a personalized greeting using those inputs.

2. Create a script that checks if a given directory exists. If it does, list its contents; if not, create the directory.

3. Develop a script that reads a list of numbers from a file and calculates their sum and average.

## Assignment Details

### System Check Script

Create a shell script named `system_check.sh` that performs the following tasks:
1. Display the current system uptime
2. Show disk usage for all mounted filesystems
3. List all currently logged-in users
4. Print the current date and time

Requirements:
- Use appropriate commands (e.g., uptime, df, who, date)
- Format the output to be easily readable
- Add comments explaining each section of the script

### Backup Script

Develop a shell script named `backup.sh` that does the following:
1. Prompt the user for a directory path to backup
2. Create a timestamped backup of the specified directory
3. Compress the backup using tar and gzip

Requirements:
- Validate that the specified directory exists
- Use the current date in the backup file name (YYYY-MM-DD format)
- Provide feedback to the user about the backup process
- Handle errors gracefully (e.g., insufficient permissions)

## Additional Examples

### Basic Script Structure
```bash
#!/bin/bash

# This is a comment
echo "Hello, World!"

NAME="Alice"
echo "Hello, $NAME"
```

### Loop Example
```bash
#!/bin/bash

for file in *.txt
do
    echo "Processing $file"
    wc -l "$file"
done
```

### Conditional Example
```bash
#!/bin/bash

if [ -f /etc/passwd ]
then
    echo "The passwd file exists."
else
    echo "The passwd file is missing!"
fi
```

### Command Substitution Example
```bash
#!/bin/bash

CURRENT_DIR=$(pwd)
echo "The current directory is: $CURRENT_DIR"

FILES=$(ls)
echo "Files in this directory:"
echo "$FILES"
```