# ## Learning Unit 4

## Learning Unit 4: User and Group Management
- Objectives:
  * Learn to manage users and groups
  * Understand user authentication and sudo
- Topics:
  * User and group concepts
  * User management commands (useradd, usermod, userdel)
  * Sudo configuration and best practices
- Activities:
  * Set up user accounts for a small office scenario
  * Configure sudo access for specific administrative tasks

## Unit Resources

# Lecture Notes

## User and Group Concepts

### Users in Linux
- Definition: A user is an entity that can access and interact with the system
- Each user has a unique identifier (UID) and username
- Users can own files and processes
- User information stored in /etc/passwd

### Groups in Linux
- Definition: A group is a collection of users with shared permissions
- Each group has a unique identifier (GID) and group name
- Users can belong to multiple groups
- Primary group vs. supplementary groups
- Group information stored in /etc/group

### Relationship between Users and Groups
- Every user belongs to at least one group (primary group)
- Users can be members of multiple groups
- Groups are used for organizing users and managing permissions
- Example: all users in the "developers" group might have access to certain project directories

### Structure of /etc/passwd
- Format: username:x:UID:GID:GECOS:home_directory:shell
- Example: john:x:1001:1001:John Doe:/home/john:/bin/bash
- Fields explanation:
  * username: Login name
  * x: Placeholder for encrypted password (stored in /etc/shadow)
  * UID: User ID number
  * GID: Primary group ID number
  * GECOS: Full name and other details
  * home_directory: User's home directory
  * shell: Default shell for the user

### Structure of /etc/group
- Format: group_name:x:GID:user_list
- Example: developers:x:1002:john,jane,bob
- Fields explanation:
  * group_name: Name of the group
  * x: Placeholder for group password (rarely used)
  * GID: Group ID number
  * user_list: Comma-separated list of users in the group

## User Management Commands

### useradd
- Purpose: Create a new user account
- Basic syntax: useradd [options] username
- Common options:
  * -m: Create home directory
  * -s: Specify login shell
  * -G: Add to supplementary groups
- Example: useradd -m -s /bin/bash -G developers john

### usermod
- Purpose: Modify an existing user account
- Basic syntax: usermod [options] username
- Common options:
  * -l: Change username
  * -g: Change primary group
  * -G: Set supplementary groups
  * -a -G: Add to supplementary groups without removing from others
- Example: usermod -a -G admins john

### userdel
- Purpose: Delete a user account
- Basic syntax: userdel [options] username
- Common options:
  * -r: Remove home directory and mail spool
- Example: userdel -r john

### passwd
- Purpose: Set or change user passwords
- Basic syntax: passwd [username]
- If no username is specified, changes the current user's password
- Example: passwd john

## Sudo Configuration

### Purpose of sudo
- Allows users to run commands with elevated privileges
- Provides finer-grained control than giving full root access
- Logs commands executed with sudo for accountability

### Basic sudo usage
- Syntax: sudo command
- Example: sudo apt update
- Users must enter their own password (not root password)
- Configurable timeout for password caching

### Editing sudoers file
- Located at /etc/sudoers
- Should only be edited using visudo command
- visudo checks for syntax errors before saving
- Basic structure:
  * user/group specification
  * host specification
  * command specification
- Example: john ALL=(ALL:ALL) ALL
  * Allows user john to run any command as any user on any host

### Best practices for sudo configuration
- Use groups for easier management
- Limit sudo access to specific commands when possible
- Use NOPASSWD sparingly
- Regularly audit sudo configurations

# Discussion Questions

1. Why is it important to have separate user accounts on a Linux system instead of everyone using the root account?

2. How do groups enhance user management and system security in Linux?

3. What are the potential security implications of granting a user sudo access? How can these risks be mitigated?

4. In what scenarios might you want to create a user account without a home directory? When would you want to create a system user?

5. How does the concept of least privilege apply to user and group management in Linux?

6. Discuss the pros and cons of using LDAP or Active Directory for user management in a large organization compared to local user accounts.

7. What are some best practices for password policies in Linux? How would you implement and enforce these policies?

8. How can you use groups to simplify file and directory permissions management?

9. What are some potential issues that could arise from deleting a user account? How can you ensure a clean and safe removal of a user?

10. How does sudo differ from su in terms of security and usability? In what situations would you prefer one over the other?

# Writing Exercise Instructions

## Exercise 1: User Management Policy

Write a comprehensive user management policy for a small software development company. Your policy should cover:

1. User account creation process
2. Password requirements and expiration policies
3. Group structure for different departments (e.g., developers, QA, management)
4. sudo access guidelines
5. Account termination procedures

Your policy should be clear, concise, and easy to understand. Consider both security and usability in your recommendations.

## Exercise 2: Troubleshooting Scenario

Write a short story or dialogue describing a scenario where a system administrator needs to troubleshoot a user access issue. Include the following elements:

1. A user complaining about not being able to access a specific resource
2. The system administrator's step-by-step process to identify the problem
3. At least two potential causes for the issue
4. The resolution of the problem
5. A brief explanation to the user about what happened and how to prevent it in the future

Be creative with your scenario while ensuring it remains realistic and educational.

# Assignment Details

## Small Office User Management Setup

### Scenario
You are the system administrator for a small marketing agency called "CreativeEdge." The company has just migrated to a Linux-based infrastructure and needs you to set up user accounts and groups for their employees.

### Requirements

1. Create the following groups:
   - marketing
   - design
   - admin
   - finance

2. Create user accounts for the following employees:
   - John Smith (Marketing Director)
   - Sarah Johnson (Senior Designer)
   - Mike Brown (System Administrator)
   - Emily Davis (Financial Analyst)
   - Alex Wong (Marketing Specialist)
   - Lisa Chen (Junior Designer)

3. Assign users to appropriate groups:
   - All users should be in their respective department groups
   - John Smith and Mike Brown should also be in the admin group

4. Set up sudo access:
   - Members of the admin group should have full sudo access
   - Members of the finance group should have sudo access only for specific financial software (simulate this with a placeholder command)

5. Create a shared directory for each department in /home/shared/ with appropriate permissions:
   - Only members of the respective groups should have read/write access to their department's shared directory

6. Implement a password policy:
   - Minimum password length of 10 characters
   - Passwords must contain at least one uppercase letter, one lowercase letter, one number, and one special character
   - Passwords must be changed every 90 days

7. Create a shell script that automates the creation of new user accounts, including:
   - Creating the user
   - Setting an initial password
   - Adding the user to the appropriate group(s)
   - Creating a home directory

### Deliverables

1. A text file containing all commands used to complete the setup
2. The shell script for automating new user account creation
3. A brief report (300-500 words) explaining your setup choices and any potential security considerations

### Bonus Challenge

Implement a log rotation policy for system logs, ensuring that logs are archived and compressed after reaching a certain size or age.

# Additional Resources

## Man Pages
- man useradd
- man usermod
- man userdel
- man passwd
- man sudo
- man visudo

## Online Documentation
- [Ubuntu User Management Documentation](https://ubuntu.com/server/docs/security-users)
- [CentOS User Management Documentation](https://docs.centos.org/en-US/centos/admin-guide/users-groups/)
- [Sudo Manual](https://www.sudo.ws/man/1.8.27/sudo.man.html)

## Video Tutorials
- [Linux User Administration (YouTube)](https://www.youtube.com/watch?v=19WOD84JFxA)
- [Sudo Configuration Explained (YouTube)](https://www.youtube.com/watch?v=YSSIm0g00m4)

## Books
- "Linux Administration: A Beginner's Guide" by Wale Soyinka (Chapter on User Account Management)
- "The Linux Command Line" by William Shotts (Chapter on User Account Management)

## Practice Environments
- [Katacoda Linux Playground](https://www.katacoda.com/courses/linux)
- [Linux Survival](https://linuxsurvival.com/) (Interactive online tutorial)