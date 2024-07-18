# ## Learning Unit 1

## Learning Unit 1: Introduction to Linux and the Command Line
- Objectives:
  * Understand the history and philosophy of Linux
  * Gain familiarity with the Linux command line interface
- Topics:
  * Overview of Linux distributions and their use in Timor Leste
  * Basic shell commands and navigation
- Activities:
  * Install a Linux distribution on a virtual machine
  * Complete a series of basic command line exercises

## Unit Resources

# Lecture Notes

## History and Philosophy of Linux

### Origins of Unix and Linux
- Unix developed at Bell Labs in 1969 by Ken Thompson and Dennis Ritchie
- Linus Torvalds created Linux kernel in 1991 as a free alternative to MINIX
- Richard Stallman's GNU Project provided essential tools for a complete OS

### Open Source Philosophy
- Free Software Foundation (FSF) established by Richard Stallman in 1985
- Four essential freedoms:
  1. Freedom to run the program for any purpose
  2. Freedom to study and modify the source code
  3. Freedom to redistribute copies
  4. Freedom to distribute modified versions
- Collaborative development model
- Transparency and peer review

### Linux Design Principles
- Modularity: Small, focused components that work together
- Everything is a file: Unified interface for device and system interactions
- Do one thing and do it well: Programs should have a single, well-defined purpose
- Plain text for data storage: Enhances interoperability and readability

## Linux Distributions

### What is a Distribution?
- Collection of software built on top of the Linux kernel
- Includes package management system, desktop environment, and pre-installed applications
- Tailored for specific use cases or user preferences

### Popular Distributions
- Ubuntu: User-friendly, based on Debian, suitable for beginners
- Fedora: Cutting-edge features, sponsored by Red Hat
- CentOS: Enterprise-focused, binary compatible with Red Hat Enterprise Linux
- Debian: Highly stable, community-driven
- Arch Linux: Minimalist, rolling release model

### Linux in Timor Leste
- Government initiatives for open-source adoption
- Educational institutions using Linux for cost-effective computing
- NGOs leveraging Linux for sustainable IT solutions
- Local businesses adopting Linux for servers and workstations

## Command Line Interface Basics

### CLI vs GUI
- CLI advantages: Efficiency, scriptability, remote access
- GUI advantages: User-friendly, visual representation, easier for beginners

### Terminal Emulators
- GNOME Terminal, Konsole, xterm
- How to open a terminal in different desktop environments

### Basic Command Structure
- Command [options] [arguments]
- Case sensitivity in Linux
- Using man pages for command documentation

### Essential Commands
- Navigation:
  - pwd: Print working directory
  - ls: List directory contents
  - cd: Change directory
- File and Directory Manipulation:
  - mkdir: Create directory
  - touch: Create empty file or update timestamp
  - cp: Copy files or directories
  - mv: Move or rename files and directories
  - rm: Remove files or directories
- System Information:
  - uname: Print system information
  - whoami: Print current user
  - date: Display or set system date and time

# Discussion Questions

1. How does the open-source philosophy of Linux differ from proprietary software models? What are the potential benefits and drawbacks of each approach?

2. In what ways could the adoption of Linux and open-source software benefit Timor Leste's technological development?

3. Compare and contrast the command line interface with graphical user interfaces. In what situations might each be preferable?

4. How might the modular design principle of Linux contribute to its stability and security?

5. Discuss the potential challenges and opportunities in transitioning from a Windows or macOS environment to Linux for personal or professional use.

6. How does the concept of "everything is a file" in Linux contribute to its flexibility and power as an operating system?

7. What role do you think Linux distributions play in making the operating system accessible to different types of users?

8. How might learning Linux and command line skills enhance your career prospects in the IT industry?

# Writing Exercise Instructions

## Reflective Essay: My First Linux Experience

Write a 500-word reflective essay about your first experience using Linux. Consider the following points:

1. Your initial impressions and expectations before using Linux
2. The installation process and any challenges you faced
3. Your experience navigating the file system using the command line
4. Comparisons with other operating systems you've used
5. Any surprising discoveries or features you found particularly useful
6. How you envision using Linux in your future personal or professional life

Structure your essay with an introduction, body paragraphs addressing the points above, and a conclusion summarizing your overall experience and future outlook.

# Assignment Details

## Linux Installation and Command Line Exercises

### Part 1: Linux Installation
- Choose a Linux distribution (Ubuntu recommended for beginners)
- Install the chosen distribution on a virtual machine or personal computer
- Document the installation process, including any challenges faced and how you overcame them

### Part 2: Command Line Exercises
Complete the following exercises using only the command line interface:

1. Create a directory structure for a mock project:
   ```
   project/
   ├── docs/
   ├── src/
   │   ├── main/
   │   └── test/
   └── resources/
   ```

2. Navigate to the `src/main/` directory and create three empty files: `app.js`, `config.json`, and `README.md`

3. List the contents of the `src` directory, including hidden files

4. Move the `README.md` file from `src/main/` to the root `project/` directory

5. Copy the `config.json` file from `src/main/` to `src/test/`

6. Create a new file in the `docs/` directory called `project_overview.txt` and add the text "This is a mock project for learning Linux commands" to it using the command line

7. Display the contents of `project_overview.txt` using a command line tool

8. Find all `.json` files in the project directory structure

9. Count the number of directories in the project structure

10. Create a compressed archive of the entire project directory

Submit a text file with the commands you used to complete each task and any output or observations.

# Additional Materials

## Basic Linux Commands Cheat Sheet

| Command | Description | Example |
|---------|-------------|---------|
| pwd     | Print working directory | `pwd` |
| ls      | List directory contents | `ls -la` |
| cd      | Change directory | `cd Documents` |
| mkdir   | Make directory | `mkdir new_folder` |
| touch   | Create empty file | `touch newfile.txt` |
| cp      | Copy files or directories | `cp file.txt backup/` |
| mv      | Move or rename files | `mv oldname.txt newname.txt` |
| rm      | Remove files or directories | `rm -r directory/` |
| cat     | Display file contents | `cat file.txt` |
| grep    | Search text using patterns | `grep "error" logfile.txt` |
| chmod   | Change file permissions | `chmod 755 script.sh` |
| sudo    | Execute command as superuser | `sudo apt update` |

## Linux Distribution Comparison Table

| Distribution | Base | Package Manager | Default Desktop | Target Audience |
|--------------|------|-----------------|------------------|-----------------|
| Ubuntu       | Debian | APT | GNOME | General users, beginners |
| Fedora       | Independent | DNF | GNOME | Developers, cutting-edge users |
| CentOS       | RHEL | YUM/DNF | GNOME | Servers, enterprise |
| Debian       | Independent | APT | GNOME | Stability-focused users |
| Arch Linux   | Independent | Pacman | None (DIY) | Advanced users, minimalists |

## Recommended Reading

- "The Linux Command Line" by William Shotts (Chapter 1: What Is The Shell?)
- "Linux Administration: A Beginner's Guide" by Wale Soyinka (Chapter 1: Introduction to Linux)