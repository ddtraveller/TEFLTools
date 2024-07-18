# ## Learning Unit 7

## Learning Unit 7: Network Configuration and Security
- Objectives:
  * Configure basic network settings
  * Implement fundamental security practices
- Topics:
  * Network configuration tools (ip, nmcli)
  * Firewall basics (iptables, firewalld)
  * SSH configuration and key-based authentication
- Activities:
  * Configure network settings for a small office network
  * Set up SSH key-based authentication and disable password login

## Required Resources

- A computer capable of running Linux (either natively or in a virtual machine)
- Access to a Linux distribution (Ubuntu or CentOS recommended)
- "The Linux Command Line" by William Shotts
- "Linux Administration: A Beginner's Guide" by Wale Soyinka

## Suggested Items to Cover

- Linux distribution differences and choosing the right one for Timor Leste's needs
- Open source software licensing and its implications
- Linux community resources and support channels

## Practical Experience and Community Engagement

- Organize a "Linux Install Fest" for the local community
- Collaborate with local businesses to identify Linux-based solutions for their needs
- Participate in or organize a local Linux User Group (LUG)
- Contribute to the translation of Linux documentation into Tetum

## Additional Resources

- Linux Documentation Project (TLDP)
- Linux Academy online courses
- Local Linux community forums and mailing lists in Timor Leste
- Free and open source alternatives to common proprietary software used in Timor Leste

## Unit Resources

# Lecture Notes

## Network Configuration

### Using the `ip` Command

The `ip` command is a powerful tool for configuring network interfaces in Linux. Here are some common uses:

- View network interfaces: `ip link show`
- View IP addresses: `ip addr show`
- Add an IP address: `ip addr add 192.168.1.10/24 dev eth0`
- Delete an IP address: `ip addr del 192.168.1.10/24 dev eth0`
- Bring an interface up or down: `ip link set eth0 up` or `ip link set eth0 down`

### Using `nmcli`

NetworkManager's command-line interface, `nmcli`, provides a user-friendly way to manage network connections:

- List all connections: `nmcli connection show`
- Activate a connection: `nmcli connection up <connection-name>`
- Deactivate a connection: `nmcli connection down <connection-name>`
- Create a new connection: `nmcli connection add type ethernet con-name "My Connection" ifname eth0`
- Modify a connection: `nmcli connection modify "My Connection" ipv4.addresses 192.168.1.10/24`

## Firewall Basics

### iptables

iptables is a command-line firewall utility for Linux. Key concepts:

- Tables: filter, nat, mangle, raw
- Chains: INPUT, OUTPUT, FORWARD
- Rules: Consist of matches and targets

Basic iptables commands:

- List rules: `sudo iptables -L`
- Add a rule: `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
- Delete a rule: `sudo iptables -D INPUT 1`
- Set default policy: `sudo iptables -P INPUT DROP`

### firewalld

firewalld is a dynamic firewall manager for Linux. Key concepts:

- Zones: public, home, work, etc.
- Services: Predefined sets of rules for common applications
- Rich rules: Complex rules for advanced configurations

Basic firewalld commands:

- List zones: `firewall-cmd --get-zones`
- Add a service: `firewall-cmd --zone=public --add-service=http --permanent`
- Remove a service: `firewall-cmd --zone=public --remove-service=http --permanent`
- Reload firewall: `firewall-cmd --reload`

## SSH Configuration

### Generating SSH Keys

1. Generate a key pair: `ssh-keygen -t rsa -b 4096`
2. View the public key: `cat ~/.ssh/id_rsa.pub`
3. Copy the public key to a server: `ssh-copy-id user@host`

### Configuring SSH Server

Edit `/etc/ssh/sshd_config`:

1. Disable password authentication:
   ```
   PasswordAuthentication no
   ```
2. Allow only specific users:
   ```
   AllowUsers user1 user2
   ```
3. Change default port:
   ```
   Port 2222
   ```

Remember to restart the SSH service after making changes:
```
sudo systemctl restart sshd
```

# Discussion Questions

1. What are the advantages and disadvantages of using static IP addresses versus DHCP in a small office network?
2. How does implementing a firewall improve network security? What potential drawbacks might there be?
3. Why is key-based authentication considered more secure than password authentication for SSH?
4. How might the network configuration and security needs differ between a small business in Dili and a rural school in Timor Leste?
5. What challenges might you face when implementing these security measures in organizations with limited technical expertise?

# Writing Exercise Instructions

Write a 500-word guide explaining how to secure a Linux server for a small business in Timor Leste. Include steps for:

1. Basic network configuration
2. Setting up a firewall
3. Configuring SSH for secure remote access
4. Implementing regular security updates

Consider the local context, including potential limitations in internet connectivity and technical expertise. Provide clear, step-by-step instructions that a novice Linux administrator could follow.

# Assignment Details

## Network Configuration and Security Project

### Objective
Configure and secure a small office network using Linux.

### Requirements
1. Set up three virtual machines:
   - One server (Ubuntu Server)
   - Two client machines (Ubuntu Desktop)

2. Network Configuration:
   - Configure static IP addresses for all machines
   - Set up proper subnet mask and gateway
   - Ensure all machines can communicate with each other

3. Firewall Configuration:
   - Implement firewall rules on the server using iptables or firewalld
   - Allow SSH (port 22) and HTTP (port 80) traffic
   - Block all other incoming traffic by default

4. SSH Configuration:
   - Generate SSH key pairs for each client
   - Configure the server to accept key-based authentication only
   - Disable root login via SSH

5. Documentation:
   - Provide a network diagram
   - Document all configuration steps
   - Include a security analysis of your setup

### Submission
Submit a report including your network diagram, configuration documentation, and security analysis. Include screenshots of your completed setup and any challenges you faced during the process.

# Additional Materials

## Network Diagram Example

```
[Client 1]     [Client 2]
    |               |
    |               |
    |---------------|
           |
        [Switch]
           |
        [Server]
           |
        [Router]
           |
       [Internet]
```

## Sample iptables Rules

```bash
# Allow established connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Drop all other incoming traffic
iptables -P INPUT DROP

# Allow all outgoing traffic
iptables -P OUTPUT ACCEPT
```

## SSH Config File Example

```
# /etc/ssh/sshd_config

Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```