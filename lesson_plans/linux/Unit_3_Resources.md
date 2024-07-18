# ## Learning Unit 3

## Learning Unit 3: Process Management
- Objectives:
  * Understand process concepts in Linux
  * Learn to monitor and control processes
- Topics:
  * Process states and lifecycle
  * Process monitoring tools (ps, top, htop)
  * Job control and background processes
- Activities:
  * Write a shell script to monitor system processes
  * Experiment with running and controlling background jobs

## Unit Resources

# Lecture Notes

## Introduction to Processes

### What is a Process?
- A process is an instance of a running program
- Each process has its own memory space and system resources
- Processes are managed by the Linux kernel

### Process States
1. Running: Currently executing on the CPU
2. Sleeping: Waiting for a resource or event
3. Stopped: Suspended, usually by a signal
4. Zombie: Terminated but still has an entry in the process table

### Process Attributes
- Process ID (PID): Unique identifier for each process
- Parent Process ID (PPID): ID of the process that spawned it
- User ID (UID): Owner of the process
- Priority: Determines scheduling order

## Process Monitoring Tools

### ps Command
- Basic syntax: `ps [options]`
- Common options:
  - `ps aux`: Show all processes for all users
  - `ps -ef`: Full-format listing
  - `ps -u username`: Show processes for a specific user

### top Command
- Real-time, dynamic view of system processes
- Updates periodically (default: every 3 seconds)
- Interactive commands:
  - 'q': Quit
  - 'k': Kill a process
  - 'r': Renice a process

### htop Command
- Enhanced version of top
- Color-coded, user-friendly interface
- Additional features:
  - Tree view of processes
  - Horizontal and vertical scrolling
  - Mouse support

## Job Control

### Foreground vs Background Processes
- Foreground: Process that has control of the terminal
- Background: Process running without direct terminal control

### Job Control Commands
- `jobs`: List current jobs
- `bg [job_spec]`: Move job to background
- `fg [job_spec]`: Move job to foreground
- `&`: Run a command in the background

### Process Priorities
- Nice values range from -20 (highest priority) to 19 (lowest priority)
- Default nice value is 0
- `nice` command: Start a process with a specific nice value
- `renice` command: Change the nice value of a running process

# Discussion Questions

1. How does the concept of processes relate to the applications we use daily on our computers?
2. Why is it important to monitor system processes? What potential issues can be identified through process monitoring?
3. How might you use job control in a real-world scenario? Provide an example.
4. What are the ethical considerations of changing process priorities on a shared system?
5. How do zombie processes occur, and why might they be problematic?
6. Compare and contrast the use of `ps`, `top`, and `htop`. In what situations would you prefer one over the others?
7. How does the Linux process management system contribute to the overall stability and security of the operating system?

# Writing Exercise Instructions

Write a short essay (300-500 words) on the following topic:

"The Role of Process Management in System Administration"

Your essay should cover:
- The importance of understanding processes in Linux systems
- How process management tools aid in troubleshooting and performance optimization
- Real-world scenarios where process management skills are crucial
- The potential consequences of poor process management

Use specific examples and terminology from the lecture to support your points.

# Assignment Details

## Process Monitoring Script

Create a shell script that monitors system processes. The script should:

1. List all current processes
2. Identify and display the top 5 CPU-consuming processes
3. Display this information every 5 seconds
4. Run continuously until interrupted by the user

Requirements:
- Use appropriate commands (e.g., `ps`, `top`, or `awk`) to gather process information
- Format the output to be easily readable
- Include comments explaining each section of your script
- Handle user interruption gracefully (e.g., display a message when the script is terminated)

Bonus:
- Add an option to log the output to a file
- Include memory usage information for each process

Submit your script file along with a brief explanation of how it works and any challenges you encountered while creating it.

# Additional Resources

## Man Pages
- `man ps`
- `man top`
- `man htop`
- `man nice`
- `man renice`

## Online Resources
- [Linux Process Management](https://www.kernel.org/doc/html/latest/admin-guide/pm/)
- [The /proc Filesystem](https://www.kernel.org/doc/html/latest/filesystems/proc.html)

## Book Excerpts
- Chapter 11: "Managing Processes" from "The Linux Command Line" by William Shotts
- Chapter 6: "Process Management" from "Linux Administration: A Beginner's Guide" by Wale Soyinka

## Example Process Monitoring Script

```bash
#!/bin/bash

# Simple process monitoring script

while true; do
    clear
    echo "Current system processes:"
    echo "------------------------"
    ps aux | head -n 5
    
    echo -e "\nTop 5 CPU-consuming processes:"
    echo "--------------------------------"
    ps aux --sort=-%cpu | head -n 6
    
    sleep 5
done
```

This script provides a basic framework that students can build upon for their assignment.