Here's the support material for the lesson plan on Network Configuration and Security, formatted in Markdown:

# Support Material for Network Configuration and Security Lesson

## 1. Key Vocabulary List with Definitions

- **IP address**: A unique numerical identifier assigned to each device on a computer network.
- **Subnet mask**: A 32-bit number that masks an IP address, dividing it into network and host portions.
- **Gateway**: A network node that serves as an access point to another network, often connecting a local network to the internet.
- **Firewall**: A network security system that monitors and controls incoming and outgoing network traffic.
- **SSH (Secure Shell)**: A cryptographic network protocol for operating network services securely over an unsecured network.
- **iptables**: A user-space utility program that allows a system administrator to configure the IP packet filter rules of the Linux kernel firewall.
- **firewalld**: A dynamic firewall manager that uses zones to manage groups of rules for different trust levels.
- **Public key**: The publicly shareable component of a pair of cryptographic keys used for asymmetric encryption.
- **Private key**: The secret component of a pair of cryptographic keys used for asymmetric encryption.
- **Authentication**: The process of verifying the identity of a user or system.

## 2. Visual Aids or Diagrams

1. Network Configuration Diagram:
   - A simple network diagram showing a router, switch, and several computers.
   - Labels for IP addresses, subnet mask, and gateway.
   - Arrows indicating the flow of traffic.

2. Firewall Concept Diagram:
   - A visual representation of a firewall between the internal network and the internet.
   - Arrows showing allowed and blocked traffic.
   - Icons representing different types of traffic (web, email, etc.).

3. SSH Key Authentication Flowchart:
   - A flowchart showing the process of SSH key-based authentication.
   - Steps include: key generation, public key distribution, connection attempt, key verification, and successful login.

## 3. Handouts or Worksheets

1. Network Configuration Commands Cheat Sheet:
   - List of common ip and nmcli commands with brief explanations.
   - Examples of how to view and set IP addresses, subnet masks, and gateways.

2. Firewall Rules Worksheet:
   - Table for students to fill in with columns for: Rule Number, Action (Allow/Deny), Source IP, Destination IP, Port, and Protocol.
   - Space for students to write the corresponding iptables or firewalld commands.

3. SSH Key Generation and Configuration Guide:
   - Step-by-step instructions for generating SSH key pairs.
   - Commands for copying the public key to a remote server.
   - Configuration steps to disable password authentication in SSH.

## 4. Additional Resources for Further Reading or Practice

1. Online tutorials:
   - DigitalOcean's "Introduction to Linux Firewall" series
   - Red Hat's "Getting started with firewalld" guide

2. Books:
   - "Linux Network Administrator's Guide" by Tony Bautts, Terry Dawson, and Gregor N. Purdy
   - "SSH Mastery: OpenSSH, PuTTY, Tunnels and Keys" by Michael W. Lucas

3. Practice environments:
   - Katacoda's interactive Linux scenarios
   - TryHackMe's Linux fundamentals rooms

4. Local resources:
   - List of Timor Leste IT forums or user groups
   - Contact information for local Linux experts or mentors

## 5. Tips for Teachers

1. Potential Challenges and Solutions:
   - Students struggling with command syntax:
     * Provide a command reference sheet
     * Encourage pair programming during practice activities
   - Difficulty understanding network concepts:
     * Use physical analogies (e.g., postal system for IP addressing)
     * Incorporate more visual aids and hands-on demonstrations
   - Limited English proficiency:
     * Provide key terms in both English and Tetum
     * Allow students to explain concepts to each other in Tetum

2. Adaptation for Different Skill Levels:
   - For beginners: Focus on basic network configuration and simple firewall rules
   - For advanced students: Introduce more complex firewall scenarios and VPN configuration

3. Emphasizing Real-World Applications:
   - Invite local IT professionals to share their experiences with Linux networking
   - Assign projects based on actual network setups in Timor Leste businesses

4. Troubleshooting Common Issues:
   - Prepare a list of common error messages and their solutions
   - Demonstrate the use of man pages and online documentation for problem-solving

5. Encouraging Collaboration:
   - Set up a class forum or chat group for sharing tips and asking questions
   - Organize study groups for peer-to-peer learning outside of class time