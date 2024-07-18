# Warm-up Activities

## Network Security Quiz
1. Create a quick 5-question quiz on basic networking concepts:
   - What is an IP address?
   - What is the purpose of a subnet mask?
   - Name three common network ports and their uses.
   - What is the difference between a firewall and antivirus software?
   - Why is SSH more secure than Telnet?

## Security Scenario Discussion
2. Present a scenario: "A small business in Dili has been experiencing frequent network outages and suspects a security breach. What steps should they take to investigate and secure their network?"
   - Have students discuss in small groups for 5 minutes.
   - Share ideas with the class and create a list of potential actions on the whiteboard.

# Main Lesson Activities

## IP Configuration Demonstration
1. Demonstrate using the `ip` command to view and configure network interfaces:
   - Show current IP configuration: `ip addr show`
   - Add a new IP address: `ip addr add 192.168.1.10/24 dev eth0`
   - Remove an IP address: `ip addr del 192.168.1.10/24 dev eth0`

## Firewall Rule Creation
2. Walk through the process of creating basic firewall rules:
   - For iptables: `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
   - For firewalld: `firewall-cmd --zone=public --add-port=22/tcp --permanent`

## SSH Key Generation and Configuration
3. Guide students through:
   - Generating an SSH key pair: `ssh-keygen -t rsa -b 4096`
   - Copying the public key to a server: `ssh-copy-id user@server`
   - Configuring SSH to disable password authentication

# Group Work or Pair Work Tasks

## Network Design Challenge
1. In pairs, design a network layout for a small office in Timor Leste:
   - Draw the network diagram
   - Assign IP addresses and subnets
   - List required firewall rules
   - Present your design to another pair and discuss differences

## Firewall Rule Implementation
2. In groups of three, implement a set of firewall rules to:
   - Allow incoming SSH (port 22)
   - Allow outgoing HTTP and HTTPS (ports 80 and 443)
   - Block all other incoming traffic
   - Test the rules and verify they work as expected

# Individual Practice Exercises

## Network Configuration
1. Configure your machine's network settings:
   - Set a static IP address using `ip` or `nmcli`
   - Configure the default gateway
   - Set up DNS servers

## SSH Key Setup
2. Generate an SSH key pair and set up key-based authentication:
   - Create the key pair
   - Configure your SSH client to use the key
   - Disable password authentication in the SSH server config

## Firewall Configuration
3. Implement a basic firewall configuration:
   - Allow incoming traffic on ports 22, 80, and 443
   - Block all other incoming traffic
   - Allow all outgoing traffic
   - Save the configuration to persist after reboot

# Cool-down or Wrap-up Activities

## Security Best Practices Brainstorm
1. In small groups, create a list of network security best practices for businesses in Timor Leste:
   - Consider local challenges and constraints
   - Think about both technical and non-technical aspects
   - Share with the class and compile a master list

## Reflection and Q&A
2. Individual reflection:
   - Write down one new thing you learned today
   - Note any concepts you're still unsure about
3. Open Q&A session:
   - Address questions from the reflection
   - Discuss real-world applications of today's lesson in Timor Leste

## Quick Configuration Challenge
4. Race against the clock:
   - Set a 5-minute timer
   - Students attempt to configure a network interface, set up a basic firewall rule, and generate an SSH key pair
   - Discuss challenges faced and strategies used