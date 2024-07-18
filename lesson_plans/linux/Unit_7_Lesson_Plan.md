# Lesson Plan: Network Configuration and Security

## 1. Resources Needed

- Computers with Linux installed (1 per student or pair)
- Whiteboard and markers
- Projector for demonstrations
- Handouts with network configuration commands and firewall rules
- SSH key generation guide

## 2. Lesson Objectives

By the end of this lesson, students will be able to:
- Configure basic network settings using ip and nmcli
- Implement fundamental firewall rules using iptables or firewalld
- Set up SSH key-based authentication and disable password login

## 3. Warm-up Activity (10 minutes)

- Quick quiz on basic networking concepts (IP addresses, subnets, ports)
- Discussion: Why is network security important for businesses in Timor Leste?

## 4. Pre-teaching Key Vocabulary (10 minutes)

- Review key terms: IP address, subnet mask, gateway, firewall, SSH, authentication
- Introduce new terms: iptables, firewalld, public key, private key

## 5. Presentation of Main Lesson Content (30 minutes)

### Network Configuration
- Demonstrate using ip command to view and set network interfaces
- Show how to use nmcli to manage network connections
- Explain the importance of proper network configuration for security

### Firewall Basics
- Introduce iptables and firewalld
- Explain basic firewall concepts (chains, rules, targets)
- Demonstrate setting up simple firewall rules

### SSH Configuration
- Explain the benefits of key-based authentication over passwords
- Demonstrate SSH key generation and distribution
- Show how to configure SSH to disable password authentication

## 6. Practice Activities (40 minutes)

- Students configure network settings on their machines using ip and nmcli
- In pairs, students set up basic firewall rules to allow/block specific ports
- Individually, students generate SSH key pairs and configure SSH to use them

## 7. Production Tasks (30 minutes)

- Students design and implement a network configuration for a small office scenario
- They create a set of firewall rules to secure the office network
- Students set up SSH key-based authentication between their machines

## 8. Wrap-up and Review (15 minutes)

- Quick recap of key points covered
- Q&A session to address any confusion or difficulties
- Brief discussion on how these skills apply to real-world scenarios in Timor Leste

## 9. Homework Assignment

- Research and write a short report on common network security threats in Timor Leste
- Create a step-by-step guide for setting up SSH key-based authentication in Tetum
- Configure home router firewall settings and document the process

## 10. Key Vocabulary Definitions

- IP address: A unique identifier for a device on a network
- Subnet mask: Defines the range of IP addresses in a network
- Gateway: A device that routes traffic between different networks
- Firewall: A security system that monitors and controls network traffic
- SSH (Secure Shell): A protocol for secure remote login and other network services
- iptables: A command-line firewall utility for Linux
- firewalld: A dynamic firewall manager for Linux
- Public key: The shareable part of an asymmetric encryption key pair
- Private key: The secret part of an asymmetric encryption key pair
- Authentication: The process of verifying the identity of a user or system