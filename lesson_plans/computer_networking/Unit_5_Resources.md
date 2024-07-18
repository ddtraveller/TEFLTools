# ## Learning Unit 5

## Learning Unit 5: IP Addressing and Subnetting
- Objectives:
  * Understand IP addressing (IPv4 and IPv6)
  * Learn basic subnetting techniques
- Topics:
  * IP address classes
  * Subnet masks
  * CIDR notation
- Activities:
  * IP addressing and subnetting exercises
  * Analyze IP allocation in Timor-Leste's government networks

## Unit Resources

# Lecture Notes

## Introduction to IP Addressing

### Purpose of IP Addresses
- IP addresses are unique identifiers for devices on a network
- Allow devices to send and receive data across networks
- Essential for routing packets to their correct destinations

### IPv4 vs IPv6
- IPv4: 32-bit addresses, written as four octets (e.g., 192.168.1.1)
- IPv6: 128-bit addresses, written in hexadecimal (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
- IPv6 developed to address IPv4 address exhaustion

## IPv4 Address Structure

### 32-bit Addresses
- Composed of 32 binary digits (0s and 1s)
- Divided into four 8-bit octets

### Dotted Decimal Notation
- Each octet represented as a decimal number (0-255)
- Four numbers separated by dots (e.g., 192.168.1.1)

## IP Address Classes

### Class A
- First bit always 0
- Range: 0.0.0.0 to 127.255.255.255
- Default subnet mask: 255.0.0.0

### Class B
- First two bits always 10
- Range: 128.0.0.0 to 191.255.255.255
- Default subnet mask: 255.255.0.0

### Class C
- First three bits always 110
- Range: 192.0.0.0 to 223.255.255.255
- Default subnet mask: 255.255.255.0

### Class D and E
- Class D: Multicast addresses (224.0.0.0 to 239.255.255.255)
- Class E: Reserved for experimental use (240.0.0.0 to 255.255.255.255)

## Subnet Masks

### Purpose
- Determine which portion of an IP address refers to the network and which to the host
- Used in conjunction with an IP address to define a network

### Default Subnet Masks
- Class A: 255.0.0.0
- Class B: 255.255.0.0
- Class C: 255.255.255.0

## CIDR Notation

### Definition
- Classless Inter-Domain Routing
- More flexible method of allocating IP addresses

### Representation
- IP address followed by a forward slash and a number (e.g., 192.168.1.0/24)
- Number represents the number of bits in the network portion of the address

### Examples
- 192.168.1.0/24 (equivalent to 255.255.255.0 subnet mask)
- 10.0.0.0/8 (equivalent to 255.0.0.0 subnet mask)

## Basic Subnetting Concepts

### Purpose of Subnetting
- Divide large networks into smaller, more manageable subnetworks
- Improve network performance and security
- Optimize IP address allocation

### Creating Subnets
- Borrow bits from the host portion of the IP address
- Increase the network portion, decrease the host portion
- Calculate new subnet mask based on borrowed bits

# Discussion Questions

1. How does the structure of IPv4 addresses differ from IPv6 addresses, and why was IPv6 developed?
2. What are the practical implications of different IP address classes for network design?
3. How does subnetting help in efficient network management, and what are its potential drawbacks?
4. In what ways might CIDR notation be more flexible than traditional IP address classes?
5. How might the transition from IPv4 to IPv6 affect network infrastructure in Timor-Leste?
6. What security considerations should be taken into account when designing an IP addressing scheme?
7. How does understanding IP addressing and subnetting contribute to better network troubleshooting?
8. What challenges might Timor-Leste face in implementing efficient IP addressing schemes across its developing infrastructure?

# Writing Exercise Instructions

## IP Addressing Scheme Proposal

Write a 500-word proposal for an IP addressing scheme for a new government office complex in Dili, Timor-Leste. Your proposal should include:

1. An introduction explaining the importance of proper IP addressing for the office complex.
2. A suggested IP address range and justification for your choice.
3. A subnetting plan that allows for future growth and separates different departments.
4. An explanation of how your scheme will enhance network security and performance.
5. Consideration of both IPv4 and IPv6 implementation.
6. A conclusion summarizing the benefits of your proposed scheme.

Use proper terminology and demonstrate your understanding of IP addressing concepts throughout your proposal.

# Assignment Details

## IP Allocation Analysis in Timor-Leste's Government Networks

1. Research the current IP address allocation in at least three different government departments in Timor-Leste.
2. Analyze the efficiency of their current IP addressing schemes.
3. Identify potential issues or areas for improvement in their allocation.
4. Propose solutions to optimize their IP address usage, considering future growth and security.
5. Create a report (1000-1500 words) detailing your findings and recommendations.
6. Include network diagrams to illustrate current and proposed IP schemes.

Submission requirements:
- Word document or PDF format
- Proper citations for any sources used
- Clear section headings and professional formatting
- Due date: [Instructor to specify]

# Additional Materials

## IP Addressing Cheat Sheet

| Class | First Octet Range | Default Subnet Mask | CIDR Notation |
|-------|-------------------|---------------------|---------------|
| A     | 1-126             | 255.0.0.0           | /8            |
| B     | 128-191           | 255.255.0.0         | /16           |
| C     | 192-223           | 255.255.255.0       | /24           |

## Subnetting Practice Problems

1. Given the network 192.168.10.0/24, create 4 subnets.
   - What is the new subnet mask?
   - What are the network addresses for each subnet?
   - How many usable host addresses are in each subnet?

2. You have been assigned the IP range 172.16.0.0/16. Create a subnetting scheme that accommodates the following requirements:
   - 1 subnet with 4000 hosts
   - 2 subnets with 2000 hosts each
   - 4 subnets with 500 hosts each
   Provide the network address and subnet mask for each subnet.

3. Convert the following IP addresses and subnet masks to CIDR notation:
   a) 10.0.0.0 with subnet mask 255.255.0.0
   b) 172.16.50.0 with subnet mask 255.255.255.192
   c) 192.168.1.0 with subnet mask 255.255.255.240

## Online Resources

- [IP Subnet Calculator](https://www.calculator.net/ip-subnet-calculator.html)
- [IPv6 Address Planner](https://www.gestioip.net/cgi-bin/subnet_calculator.cgi)
- [Cisco's IP Addressing and Subnetting for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)