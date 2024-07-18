# Lesson Plan: User and Group Management

## 1. Resources Needed

- Linux systems (one per student or pair)
- Whiteboard and markers
- Handouts with user/group management commands
- Projector for demonstrations

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Explain the concepts of users and groups in Linux
- Use basic user management commands (useradd, usermod, userdel)
- Configure and use sudo for administrative tasks
- Set up user accounts for a small office scenario

## 3. Warm-up Activity (10 minutes)

- Class discussion: "Why do we need different user accounts on a computer system?"
- List student responses on the whiteboard

## 4. Pre-teaching Key Vocabulary (10 minutes)

Introduce and explain:
- User
- Group
- Permissions
- Sudo
- Authentication

## 5. Presentation of Main Lesson Content (30 minutes)

### User and Group Concepts
- Explain the purpose of users and groups
- Discuss the relationship between users and groups
- Show the structure of /etc/passwd and /etc/group files

### User Management Commands
- Demonstrate useradd, usermod, and userdel
- Explain common options for each command
- Show how to set and change passwords with passwd

### Sudo Configuration
- Explain the purpose of sudo
- Demonstrate basic sudo usage
- Show how to edit the sudoers file safely with visudo

## 6. Practice Activities (30 minutes)

- Students practice creating, modifying, and deleting users
- Students experiment with adding users to groups
- Students use sudo to perform basic administrative tasks

## 7. Production Task (40 minutes)

Small Office Scenario:
- Students set up user accounts for a fictional small office
- Create appropriate groups for different departments
- Configure sudo access for specific administrative tasks

## 8. Wrap-up and Review (15 minutes)

- Quick quiz on key concepts covered
- Address any questions or difficulties encountered
- Recap the importance of proper user and group management

## 9. Homework Assignment

- Research and write a short report on best practices for user account security
- Create a shell script that automates the creation of multiple user accounts

## 10. Key Vocabulary Definitions

- User: An account on a Linux system that represents a person or service
- Group: A collection of users with shared permissions or characteristics
- Permissions: Rules that determine who can access files and resources
- Sudo: A command that allows users to run programs with the security privileges of another user
- Authentication: The process of verifying the identity of a user or process