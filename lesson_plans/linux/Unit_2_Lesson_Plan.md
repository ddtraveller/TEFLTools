# Lesson Plan: File System Navigation and Management

## 1. Resources Needed

- Computers with Linux installed (1 per student or pair)
- Whiteboard and markers
- Handouts with Linux file system hierarchy diagram
- Projector for demonstrations

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Navigate the Linux file system using command-line tools
- Explain the purpose of key directories in the Linux file system hierarchy
- Use basic file manipulation commands (cp, mv, rm, mkdir, etc.)
- Set and modify file permissions and ownership

## 3. Warm-up Activity (10 minutes)

- Quick quiz: Students match common file operations (copy, move, delete) with their Linux command equivalents
- Brief discussion on why understanding file systems is crucial for system administration

## 4. Pre-teaching Key Vocabulary (10 minutes)

- File system
- Directory
- Path (absolute vs. relative)
- Permission
- Ownership
- Root directory

## 5. Presentation of Main Lesson Content (30 minutes)

### Linux File System Hierarchy
- Explain the concept of a hierarchical file system
- Walk through the main directories: /, /home, /etc, /var, /usr, /tmp
- Demonstrate navigation using cd, pwd, and ls commands

### File Manipulation Commands
- Introduce and demonstrate:
  - cp (copy)
  - mv (move/rename)
  - rm (remove)
  - mkdir (make directory)
  - touch (create empty file)

### File Permissions and Ownership
- Explain read, write, and execute permissions
- Demonstrate ls -l output
- Introduce chmod and chown commands

## 6. Practice Activities (40 minutes)

1. File System Navigation Race
   - Students race to navigate to specific directories using cd and verify with pwd

2. File Manipulation Challenge
   - Provide a list of file operations for students to perform (create, copy, move, delete)

3. Permission Puzzle
   - Give students various scenarios and ask them to set appropriate permissions using chmod

## 7. Production Task (30 minutes)

Create a Directory Structure for a Mock Project:
- Students design and create a directory structure for a web development project
- Must include directories for HTML, CSS, JavaScript, and images
- Set appropriate permissions for different user roles (developer, designer, client)

## 8. Wrap-up and Review (10 minutes)

- Quick recap of key commands and concepts
- Q&A session for any lingering questions
- Brief discussion on real-world applications of today's lessons

## 9. Homework Assignment

1. Research and write a short report on the differences between ext4 and other file systems (e.g., NTFS, FAT32)
2. Create a shell script that sets up a standard project directory structure with appropriate permissions

## 10. Key Vocabulary Definitions

- File system: The way in which files are named and where they are placed logically for storage and retrieval
- Directory: A file system cataloging structure which contains references to other files and directories
- Path: The unique location of a file or directory in a file system
- Permission: Rules associated with a file or directory that control user access (read, write, execute)
- Ownership: The user and group assigned as owners of a file or directory
- Root directory: The top-level directory of a file system, denoted by /