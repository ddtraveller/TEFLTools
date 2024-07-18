# ## Learning Unit 5

## Learning Unit 5: System Logging and Monitoring
- Objectives:
  * Understand Linux logging systems
  * Learn to monitor system health and performance
- Topics:
  * Syslog and journald
  * Log analysis tools
  * System monitoring utilities
- Activities:
  * Analyze log files to troubleshoot a simulated system issue
  * Set up custom logging for a specific application

## Unit Resources

# Lecture Notes

## Introduction to System Logging

### Purpose of System Logging
- Provides a record of system events and activities
- Crucial for troubleshooting, security auditing, and performance analysis
- Helps in compliance with regulations and policies

### Syslog Protocol
- Standard protocol for message logging
- Allows separation of software generating messages from systems storing them
- Typically uses port 514 for UDP (historically) or 6514 for TCP with TLS

### Journald
- Part of systemd, a system and service manager for Linux
- Collects and stores logging data in a structured, indexed format
- Provides powerful querying capabilities

### Viewing Logs
- Traditional log files: typically stored in /var/log/
- Journalctl command: used to query and display logs from journald

## Log Analysis Tools

### Grep
- Searches text using patterns
- Basic syntax: `grep [options] pattern [file...]`
- Useful options:
  - `-i`: case-insensitive search
  - `-v`: invert match (show lines that don't match)
  - `-r`: recursive search in directories

### Awk
- Powerful text-processing tool
- Can filter and transform text
- Basic syntax: `awk 'pattern {action}' [file...]`
- Useful for extracting specific fields from log entries

### Sed
- Stream editor for filtering and transforming text
- Basic syntax: `sed [options] 'command' [file...]`
- Commonly used for search and replace operations

## System Monitoring

### Top/Htop
- Interactive process viewers
- Display system summary and list of processes
- Key information:
  - CPU usage
  - Memory usage
  - Load average

### Iotop
- I/O monitoring tool
- Shows I/O usage information for processes
- Useful for identifying processes causing high disk activity

### Vmstat
- Reports information about processes, memory, paging, block I/O, traps, and CPU activity
- Provides a concise overview of system performance

# Discussion Questions

1. Why is system logging important for both system administrators and regular users?
2. How does the syslog protocol differ from journald? What are the advantages and disadvantages of each?
3. In what scenarios would you use grep over awk or sed, and vice versa?
4. How can system monitoring tools help in identifying and resolving performance issues?
5. What ethical considerations should system administrators keep in mind when logging and monitoring user activities?

# Writing Exercise Instructions

## Exercise 1: Log Analysis Report
Write a detailed report analyzing the auth.log or secure log on your system. Your report should include:

1. An introduction explaining the purpose of the log file you're analyzing.
2. A summary of the key events you've identified, including:
   - Failed login attempts (if any)
   - Successful sudo usage
   - Any other security-related events you find interesting
3. An analysis of any patterns or trends you've noticed in the log entries.
4. Recommendations for improving system security based on your findings.
5. A conclusion summarizing the importance of regular log analysis.

Your report should be 500-750 words and include specific examples from the log file to support your analysis.

## Exercise 2: System Monitoring Script Documentation
Write documentation for the shell script you created to check system load. Your documentation should include:

1. A brief description of the script's purpose
2. An explanation of how to use the script
3. A breakdown of each major section of the script, explaining what it does and why
4. Any limitations or potential improvements for the script
5. Examples of the script's output and how to interpret it

Your documentation should be clear and concise, suitable for other system administrators who might use your script.

# Assignment Details

## Custom Logging and Monitoring Setup

### Objective
Set up custom logging for a web server and create a simple shell script to monitor its performance.

### Requirements
1. Configure custom logging for Apache or Nginx web server:
   - Create a new log file specifically for tracking server performance
   - Log relevant information such as request processing time, server load at time of request, and memory usage

2. Write a shell script that:
   - Checks server load every 5 minutes
   - Logs warnings if CPU usage exceeds 80% or if available memory falls below 20%
   - Emails the system administrator if these thresholds are exceeded for more than 15 minutes continuously

### Deliverables
1. Configuration file snippets showing custom logging setup
2. The complete shell script for monitoring
3. A brief report (300-500 words) explaining your setup, any challenges faced, and how this monitoring solution could be improved or expanded

### Evaluation Criteria
- Correctness of custom logging configuration
- Functionality and efficiency of the monitoring script
- Clarity and completeness of the report

# Additional Resources

## Sample Log Entries

```
May 15 14:30:05 webserver sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2
May 15 14:35:10 webserver sudo: johndoe : TTY=pts/0 ; PWD=/home/johndoe ; USER=root ; COMMAND=/usr/bin/apt update
May 15 14:40:15 webserver kernel: [UFW BLOCK] IN=eth0 OUT= MAC=00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd SRC=10.0.0.1 DST=10.0.0.2 LEN=52 TOS=0x00 PREC=0x00 TTL=117 ID=62266 DF PROTO=TCP SPT=56789 DPT=80 WINDOW=8192 RES=0x00 SYN URGP=0
```

## Example Monitoring Script

```bash
#!/bin/bash

LOG_FILE="/var/log/system_monitor.log"
ADMIN_EMAIL="admin@example.com"
THRESHOLD_CPU=80
THRESHOLD_MEM=20
CHECK_INTERVAL=300  # 5 minutes in seconds

log_system_status() {
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    mem_available=$(free | grep Mem | awk '{print $7/$2 * 100.0}')
    
    echo "$timestamp - CPU: $cpu_usage%, Mem Available: $mem_available%" >> $LOG_FILE
    
    if (( $(echo "$cpu_usage > $THRESHOLD_CPU" | bc -l) )); then
        echo "$timestamp - WARNING: High CPU usage: $cpu_usage%" >> $LOG_FILE
    fi
    
    if (( $(echo "$mem_available < $THRESHOLD_MEM" | bc -l) )); then
        echo "$timestamp - WARNING: Low memory available: $mem_available%" >> $LOG_FILE
    fi
}

while true; do
    log_system_status
    sleep $CHECK_INTERVAL
done
```

## Useful Commands for Log Analysis

- Search for failed SSH login attempts:
  ```
  grep "Failed password" /var/log/auth.log
  ```

- Count occurrences of a specific event:
  ```
  grep "Failed password" /var/log/auth.log | wc -l
  ```

- Extract IP addresses of failed login attempts:
  ```
  grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr
  ```

- Monitor log file in real-time:
  ```
  tail -f /var/log/auth.log
  ```