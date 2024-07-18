# Lesson Plan: Process Management in Linux

## 1. Resources Needed

- Linux computers or virtual machines for each student
- Projector for demonstrations
- Whiteboard and markers
- Handouts with key commands and concepts

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Explain the concept of processes in Linux
- Use tools like ps, top, and htop to monitor processes
- Manage background jobs and process priorities
- Write a basic shell script to monitor system processes

## 3. Warm-up Activity (10 minutes)

- Ask students to list applications currently running on their computers
- Discuss how these applications might appear to the operating system

## 4. Pre-teaching Key Vocabulary (10 minutes)

- Process
- PID (Process ID)
- Foreground vs Background jobs
- Nice value
- Zombie process

## 5. Main Lesson Content (40 minutes)

### 5.1 Introduction to Processes (10 minutes)
- Define what a process is in Linux
- Explain process states: running, sleeping, stopped, zombie

### 5.2 Process Monitoring Tools (15 minutes)
- Demonstrate the use of ps command
- Show real-time monitoring with top
- Introduce htop as an enhanced alternative

### 5.3 Job Control (15 minutes)
- Explain foreground and background processes
- Demonstrate job control commands: jobs, bg, fg
- Discuss process priorities and the nice command

## 6. Practice Activities (30 minutes)

### 6.1 Process Exploration
- Students use ps and top to explore processes on their systems
- Identify and record information about key system processes

### 6.2 Job Control Exercise
- Students practice starting processes, moving them to background, and bringing them back to foreground

## 7. Production Task (30 minutes)

- Students write a simple shell script that:
  1. Lists all processes
  2. Identifies the top 5 CPU-consuming processes
  3. Displays this information every 5 seconds

## 8. Wrap-up and Review (10 minutes)

- Recap key points about processes and job control
- Address any questions or misconceptions
- Preview the next lesson on user and group management

## 9. Homework Assignment

1. Research and write a short report on zombie processes and how to manage them
2. Enhance the monitoring script to include memory usage and write results to a log file
3. Experiment with changing process priorities using nice and renice, documenting the effects

## 10. Key Vocabulary Definitions

- Process: An instance of a running program
- PID: Process ID, a unique identifier for each process
- Foreground job: A process that has control of the terminal
- Background job: A process running without direct control of the terminal
- Nice value: A number that influences process scheduling priority
- Zombie process: A process that has completed execution but still has an entry in the process table