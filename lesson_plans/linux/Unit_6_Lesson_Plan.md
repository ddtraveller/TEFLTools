# Lesson Plan: Shell Scripting Basics

## 1. Resources Needed

- Computers with Linux installed (one per student or pair)
- Projector for demonstrations
- Whiteboard and markers
- Handouts with basic shell scripting syntax reference
- Sample scripts for analysis

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Explain the basic structure and syntax of a shell script
- Use variables, loops, and conditionals in shell scripts
- Implement command substitution and piping in scripts
- Write simple automation scripts for system tasks

## 3. Warm-up Activity (10 minutes)

- Quick quiz on basic Linux commands covered in previous lessons
- Brief discussion on repetitive tasks students perform on their computers that could be automated

## 4. Pre-teaching Key Vocabulary (10 minutes)

Introduce and explain key terms:
- Shebang
- Variables
- Conditionals (if, else, elif)
- Loops (for, while)
- Command substitution
- Piping

## 5. Presentation of Main Lesson Content (30 minutes)

### Shell Script Structure
- Explain the purpose and structure of shell scripts
- Demonstrate creating a simple "Hello, World!" script

### Variables and User Input
- Show how to declare and use variables
- Demonstrate reading user input with `read` command

### Conditionals
- Explain `if`, `else`, and `elif` statements
- Demonstrate file and string comparisons

### Loops
- Introduce `for` and `while` loops
- Show examples of iterating over files and numbers

### Command Substitution and Piping
- Explain command substitution syntax `$(command)`
- Demonstrate piping output between commands in a script

## 6. Practice Activities (30 minutes)

- Students write a script that asks for their name and greets them
- Students create a script that checks if a file exists and is writable
- Students write a loop to process multiple files in a directory

## 7. Production Tasks (40 minutes)

### Task 1: System Check Script
Students write a script that:
- Checks system uptime
- Displays disk usage
- Shows current logged-in users

### Task 2: Backup Script
Students create a script that:
- Asks for a directory to backup
- Creates a timestamped backup of the directory
- Compresses the backup

## 8. Wrap-up and Review (10 minutes)

- Quick recap of key concepts covered
- Address any questions or challenges encountered
- Preview of how these skills will be applied in future lessons

## 9. Homework Assignment

1. Enhance the system check script to include memory usage and CPU load
2. Create a script that organizes files in a directory based on their extension
3. Read Chapter 3 of "The Linux Command Line" by William Shotts

## 10. Key Vocabulary Definitions

- **Shebang**: The characters "#!" at the beginning of a script, specifying the interpreter
- **Variables**: Named storage locations for data in a script
- **Conditionals**: Statements that perform different actions based on whether a condition is true or false
- **Loops**: Constructs that allow a set of instructions to be repeated multiple times
- **Command substitution**: The process of replacing a command with its output in a script
- **Piping**: Sending the output of one command as input to another command