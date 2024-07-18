# Engaging Activities for Process Management in Linux

## Warm-up Activities

### 1. Process Guessing Game
- Students pair up and take turns describing a common computer task without naming it
- Partner tries to guess the task and then lists possible processes involved
- Class discusses the most interesting or surprising processes identified

### 2. Process Tree Visualization
- Students draw a simple tree diagram of processes they think might be running on their computer
- Compare drawings and discuss similarities and differences
- Instructor reveals an actual process tree using `pstree` command

## Main Lesson Activities

### 1. Process Detective
- Provide students with a list of common Linux processes (e.g., sshd, cron, apache2)
- Students use `ps` and `man` commands to investigate and report on each process's function

### 2. Top Trumps: Process Edition
- Create cards with process information (PID, CPU usage, memory usage, etc.)
- Students play in small groups, comparing process stats to "win" cards

### 3. Process State Charades
- Assign each student a process state (running, sleeping, stopped, zombie)
- Students act out their assigned state while others guess
- Discuss real-world scenarios where processes might enter each state

## Group Work or Pair Work Tasks

### 1. Process Management Scenarios
- Provide groups with different scenarios (e.g., unresponsive application, high CPU usage)
- Groups discuss and present their approach to managing the situation using process tools

### 2. Job Control Relay Race
- Set up terminals with long-running commands (e.g., `sleep 100`)
- Teams compete to correctly use job control commands (bg, fg, jobs) in a relay format

### 3. Process Priority Debate
- Assign each group a system role (e.g., web server, database, backup service)
- Groups argue for why their processes should have higher priority
- Class votes on final priority assignments

## Individual Practice Exercises

### 1. Process Scavenger Hunt
- Provide a list of criteria (e.g., "Find a process using more than 100MB of memory")
- Students use `ps`, `top`, or `htop` to find processes matching each criterion

### 2. Nice Value Experimentation
- Students run CPU-intensive commands (e.g., `yes > /dev/null`) with different nice values
- Record and graph the impact on system performance

### 3. Custom Process Monitoring
- Students write a simple shell script to monitor a specific process of their choice
- Script should alert when the process exceeds certain resource thresholds

## Cool-down or Wrap-up Activities

### 1. Process Management Jeopardy
- Create a Jeopardy-style game board with categories like "Commands", "Process States", "Job Control"
- Students compete in teams to answer questions and reinforce key concepts

### 2. One-Minute Process Paper
- Students have one minute to write down the most important thing they learned about process management
- Volunteers share their "one-minute papers" with the class

### 3. Process Management Memes
- Students create memes related to Linux process management concepts
- Share and vote on the most creative and accurate memes