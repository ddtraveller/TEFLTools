# ## Learning Unit 2

## Learning Unit 2: File System Navigation and Management
- Objectives:
  * Master file system navigation and manipulation
  * Understand file permissions and ownership
- Topics:
  * Linux file system hierarchy
  * File manipulation commands (cp, mv, rm, etc.)
  * File permissions and ownership concepts
- Activities:
  * Create a directory structure for a mock project
  * Set appropriate permissions for different user roles

## Unit Resources

# Lecture Notes

## Linux File System Hierarchy

### Introduction
- The Linux file system is organized in a hierarchical tree-like structure
- Everything in Linux is considered a file, including directories and devices
- The root directory (/) is the top-level directory from which all other directories branch

### Key Directories
1. / (root):
   - The top-level directory
   - All other directories and files are contained within it

2. /home:
   - Contains user home directories
   - Each user typically has their own subdirectory (e.g., /home/username)

3. /etc:
   - System configuration files
   - Contains settings for system-wide applications and services

4. /var:
   - Variable data files
   - Includes log files, temporary files, and spool directories

5. /usr:
   - User binaries, libraries, documentation, and source code
   - Contains most of the applications and utilities used by users

6. /tmp:
   - Temporary files
   - Contents are typically cleared on system reboot

### Navigation Commands
- pwd: Print Working Directory
- cd: Change Directory
- ls: List directory contents

## File Manipulation Commands

### cp (copy)
- Syntax: cp [options] source destination
- Examples:
  - cp file1 file2
  - cp -r dir1 dir2 (recursive copy for directories)

### mv (move/rename)
- Syntax: mv [options] source destination
- Examples:
  - mv file1 file2 (rename file1 to file2)
  - mv file1 /path/to/directory/ (move file1 to specified directory)

### rm (remove)
- Syntax: rm [options] file(s)
- Examples:
  - rm file1
  - rm -r directory (recursive removal for directories)

### mkdir (make directory)
- Syntax: mkdir [options] directory_name
- Example: mkdir new_directory

### touch (create empty file)
- Syntax: touch file_name
- Example: touch new_file.txt

## File Permissions and Ownership

### Understanding Permissions
- Three types: read (r), write (w), execute (x)
- Three categories: user (u), group (g), others (o)
- Represented as: rwxrwxrwx

### Viewing Permissions
- Use ls -l command
- Example output: -rw-r--r-- 1 user group 4096 Jan 1 12:00 file.txt

### Changing Permissions
- chmod command
- Syntax: chmod [options] mode file(s)
- Examples:
  - chmod u+x file.txt (add execute permission for user)
  - chmod 755 file.txt (set rwx for user, rx for group and others)

### Changing Ownership
- chown command
- Syntax: chown [options] user[:group] file(s)
- Example: chown newuser:newgroup file.txt

# Discussion Questions

1. Why is understanding the file system hierarchy important for system administrators?
2. How does the Linux file system differ from other operating systems you've used?
3. What are some potential security risks associated with improper file permissions?
4. In what situations might you need to use the 'sudo' command when manipulating files?
5. How can proper organization of the file system improve system performance and maintenance?
6. What are some best practices for naming files and directories in Linux?
7. How might file permissions be used to implement the principle of least privilege?
8. What are some potential issues that could arise from incorrect use of the 'rm' command?
9. How does the concept of file ownership contribute to system security?
10. In what scenarios might you need to use relative paths versus absolute paths?

# Writing Exercise Instructions

## File System Navigation Story

Write a short story (300-500 words) from the perspective of a system administrator navigating through a complex Linux file system to solve a critical issue. Your story should incorporate at least five different file system navigation or manipulation commands, and explain the thought process behind each action. Be creative with the scenario, but ensure it reflects a realistic system administration task.

Include the following elements in your story:
1. A clear problem that needs to be solved
2. Use of at least five different commands (e.g., cd, ls, cp, mv, rm, chmod)
3. Navigation through multiple directories
4. A file permission or ownership change
5. A brief explanation of why each command was chosen

# Assignment Details

## Project: Create a Web Development Directory Structure

### Objective
Design and implement a directory structure for a web development project, incorporating proper file organization and permissions.

### Requirements
1. Create a main project directory named "webproject"
2. Within "webproject", create the following subdirectories:
   - html
   - css
   - js
   - images
   - docs
3. In each subdirectory, create at least two placeholder files
4. Set appropriate permissions for different user roles:
   - Developer: Full access (read, write, execute) to all directories and files
   - Designer: Read and write access to html, css, and images; read-only access to js
   - Client: Read-only access to html and images

### Steps
1. Use mkdir to create the directory structure
2. Use touch to create placeholder files
3. Use chmod to set the required permissions
4. Use ls -R to display the final directory structure with permissions

### Submission
Submit a shell script that automates the creation of this directory structure with the required permissions, along with a brief explanation (100-200 words) of your design choices and permission settings.

# Additional Materials

## File System Hierarchy Diagram

```
/
├── bin
├── boot
├── dev
├── etc
├── home
│   ├── user1
│   └── user2
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
│   ├── bin
│   ├── lib
│   └── local
└── var
    ├── log
    └── www
```

## Permission Calculator Table

| Octal | Binary | File Mode |
|-------|--------|-----------|
| 0     | 000    | ---       |
| 1     | 001    | --x       |
| 2     | 010    | -w-       |
| 3     | 011    | -wx       |
| 4     | 100    | r--       |
| 5     | 101    | r-x       |
| 6     | 110    | rw-       |
| 7     | 111    | rwx       |

## Common File Operations Cheat Sheet

| Operation | Command | Example |
|-----------|---------|---------|
| Copy file | cp | cp file1.txt file2.txt |
| Move file | mv | mv file1.txt /home/user/ |
| Remove file | rm | rm file1.txt |
| Create directory | mkdir | mkdir new_folder |
| Remove directory | rmdir | rmdir empty_folder |
| Remove non-empty directory | rm -r | rm -r full_folder |
| Change permissions | chmod | chmod 755 script.sh |
| Change ownership | chown | chown user:group file.txt |
| View file contents | cat | cat file.txt |
| Edit file | nano or vim | nano file.txt |