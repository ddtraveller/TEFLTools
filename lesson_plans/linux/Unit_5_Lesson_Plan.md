# Lesson Plan: System Logging and Monitoring

## 1. Resources Needed

- Linux machines or virtual machines for each student
- Access to system logs (e.g., /var/log/)
- Text editors (e.g., nano, vim)
- Monitoring tools (e.g., htop, iotop)
- Projector for demonstrations

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Explain the purpose and importance of system logging
- Navigate and interpret common log files
- Use basic log analysis tools
- Set up custom logging for applications
- Monitor system health and performance using command-line tools

## 3. Warm-up Activity (10 minutes)

- Group discussion: "Why is system logging important? What kinds of events might we want to log?"
- Write responses on the board and discuss as a class

## 4. Pre-teaching Key Vocabulary (10 minutes)

- Introduce and explain key terms:
  - Syslog
  - Journald
  - Log rotation
  - System load
  - I/O operations

## 5. Main Lesson Content (40 minutes)

### A. Introduction to System Logging (15 minutes)
- Explain the syslog protocol and its importance
- Discuss the role of journald in modern Linux systems
- Demonstrate how to view logs using journalctl and traditional log files

### B. Log Analysis Tools (15 minutes)
- Introduce common log analysis tools:
  - grep
  - awk
  - sed
- Demonstrate basic log searching and filtering techniques

### C. System Monitoring (10 minutes)
- Introduce key system monitoring tools:
  - top/htop
  - iotop
  - vmstat
- Explain how to interpret the output of these tools

## 6. Practice Activities (30 minutes)

### A. Log Analysis Exercise (15 minutes)
- Provide students with a sample log file containing various events
- Ask them to use grep, awk, and sed to extract specific information

### B. System Monitoring Exercise (15 minutes)
- Have students use top/htop to identify resource-intensive processes
- Ask them to interpret the output and suggest potential optimizations

## 7. Production Task (30 minutes)

- Scenario: "You are a system administrator for a small web hosting company. Set up custom logging for a web server and create a simple shell script to monitor its performance."
- Students should:
  1. Configure custom logging for the Apache or Nginx web server
  2. Write a shell script that checks server load and logs warnings if thresholds are exceeded

## 8. Wrap-up and Review (10 minutes)

- Recap key points of the lesson
- Address any questions or concerns
- Preview the next lesson on shell scripting basics

## 9. Homework Assignment

1. Analyze the auth.log or secure log on your system. Write a short report on:
   - Any failed login attempts
   - Successful sudo usage
   - Any other security-related events you find interesting

2. Create a simple shell script that checks system load every 5 minutes and appends the results to a custom log file.

## 10. Key Vocabulary Definitions

- Syslog: A standard for message logging, allowing separation of the software that generates messages from the system that stores them and the software that reports and analyzes them.
- Journald: A system service that collects and stores logging data, providing a centralized management solution for all system logging.
- Log rotation: The process of archiving and renewing log files to prevent them from consuming too much disk space.
- System load: A measure of the amount of computational work that a computer system performs.
- I/O operations: Input/Output operations, referring to the communication between a computer and its users, or between the computer and its own peripheral devices.