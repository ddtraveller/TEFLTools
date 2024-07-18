Here's the support material for the lesson on Process Management in Linux, formatted in Markdown:

# Support Material for Process Management in Linux

## 1. Key Vocabulary List with Definitions

- **Process**: An instance of a running program in Linux.
- **PID (Process ID)**: A unique numerical identifier assigned to each process.
- **Foreground job**: A process that has direct control of the terminal and receives input from the user.
- **Background job**: A process running without direct control of the terminal, allowing other processes to run simultaneously.
- **Nice value**: A number that influences process scheduling priority, ranging from -20 (highest priority) to 19 (lowest priority).
- **Zombie process**: A process that has completed execution but still has an entry in the process table.
- **Daemon**: A background process that runs continuously, often providing services to other processes.
- **Thread**: A lightweight process that shares resources with its parent process.
- **Context switch**: The act of saving the state of a process and loading the saved state of a different process.
- **Process state**: The current condition of a process (e.g., running, sleeping, stopped, zombie).

## 2. Visual Aids or Diagrams

1. Process Lifecycle Diagram:
   - A flowchart showing the states of a process (New, Ready, Running, Waiting, Terminated)
   - Arrows between states indicating possible transitions

2. Process Hierarchy Tree:
   - A tree structure showing the parent-child relationships between processes
   - Root of the tree is the init process (PID 1)
   - Branches show how processes spawn child processes

3. Top Command Output Explanation:
   - A labeled screenshot of the top command output
   - Annotations explaining key fields like PID, USER, %CPU, %MEM, COMMAND

## 3. Handouts or Worksheets

1. Process Management Command Cheat Sheet:
   - A table listing essential commands (ps, top, htop, kill, nice, renice) with their common options and brief descriptions

2. Process Exploration Worksheet:
   - Step-by-step instructions for students to identify and record information about key system processes
   - Tables for students to fill in with process information (PID, name, CPU usage, memory usage, state)

3. Job Control Exercise Guide:
   - Instructions for starting processes, moving them to background, and bringing them back to foreground
   - Practice scenarios for students to work through

## 4. Additional Resources for Further Reading or Practice

1. "Linux Process Management" chapter from "The Linux Command Line" by William Shotts
2. Online tutorial: "Understanding Linux Process States" on Linux.com
3. Man pages for ps, top, htop, and nice commands
4. "Linux Processes and Signals" article on DigitalOcean
5. Interactive Linux process management simulator: Terminus (terminal-based game)

## 5. Tips for Teachers on Potential Challenges and How to Address Them

1. Challenge: Students struggling with the concept of processes vs. programs
   - Tip: Use real-world analogies, like a recipe (program) vs. cooking the meal (process)

2. Challenge: Difficulty understanding process states
   - Tip: Use the process lifecycle diagram and relate states to everyday situations (e.g., sleeping state as a person napping)

3. Challenge: Confusion about nice values and process priorities
   - Tip: Demonstrate the effects of changing nice values on process behavior with a simple CPU-intensive script

4. Challenge: Students overwhelmed by the amount of information in ps or top output
   - Tip: Start with simplified views (e.g., ps aux | head) and gradually introduce more complex options

5. Challenge: Trouble writing the shell script for the production task
   - Tip: Provide a skeleton script with comments indicating where students should add their code

6. Challenge: Difficulty identifying important system processes
   - Tip: Create a list of common essential processes (e.g., systemd, sshd, cron) with brief explanations of their functions

Remember to adapt these materials to the specific needs and context of your students in Timor Leste, incorporating local examples and use cases where possible.