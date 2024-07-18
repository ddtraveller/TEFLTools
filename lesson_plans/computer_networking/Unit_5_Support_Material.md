Here's the support material for the IP Addressing and Subnetting lesson, formatted in Markdown:

# Support Material for IP Addressing and Subnetting Lesson

## 1. Key Vocabulary List with Definitions

- **IP Address**: A unique numerical label assigned to each device in a computer network
- **IPv4**: The fourth version of the Internet Protocol, using 32-bit addresses
- **IPv6**: The sixth version of the Internet Protocol, using 128-bit addresses
- **Subnet**: A logical subdivision of an IP network
- **Subnet Mask**: A 32-bit number that masks an IP address, dividing it into network and host portions
- **CIDR (Classless Inter-Domain Routing)**: A method for allocating IP addresses and routing IP packets
- **Network ID**: The portion of an IP address that identifies the network
- **Host ID**: The portion of an IP address that identifies a specific device on the network
- **Octet**: A group of eight bits, used in IPv4 addressing
- **Broadcast Address**: A special address used to send data to all devices on a network

## 2. Visual Aids or Diagrams

1. IPv4 Address Structure Diagram:
   ```
   [Octet 1] . [Octet 2] . [Octet 3] . [Octet 4]
   [8 bits]    [8 bits]    [8 bits]    [8 bits]
   ```

2. IP Address Classes Table:
   ```
   Class | First Octet Range | Default Subnet Mask
   ------|-------------------|---------------------
   A     | 1-126             | 255.0.0.0
   B     | 128-191           | 255.255.0.0
   C     | 192-223           | 255.255.255.0
   D     | 224-239           | (Multicast)
   E     | 240-255           | (Reserved)
   ```

3. Subnetting Diagram:
   ```
   Original Network: 192.168.1.0/24
   Subnets:
   [192.168.1.0/26] [192.168.1.64/26] [192.168.1.128/26] [192.168.1.192/26]
   ```

## 3. Handouts or Worksheets

1. IP Address Classification Exercise:
   - List of 10 IP addresses for students to classify (Class A, B, C, D, or E)
   - Space for students to write the class and explain their reasoning

2. Subnet Mask Matching:
   - Table with network sizes and corresponding subnet masks to match

3. CIDR Notation Conversion:
   - List of IP addresses with traditional subnet masks to convert to CIDR notation
   - List of IP addresses in CIDR notation to convert to traditional subnet masks

4. Subnetting Worksheet:
   - Given network address and required number of subnets, students calculate:
     * Subnet mask
     * Number of host addresses per subnet
     * Subnet addresses
     * First and last usable host addresses for each subnet
     * Broadcast addresses for each subnet

## 4. Additional Resources for Further Reading or Practice

1. Online IP Subnet Calculator: https://www.calculator.net/ip-subnet-calculator.html
2. Cisco's "IP Addressing and Subnetting for New Users" Guide: https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html
3. "Understanding IP Addressing and CIDR Charts" by RIPE NCC: https://www.ripe.net/about-us/press-centre/understanding-ip-addressing
4. Interactive IP Subnetting Practice: https://subnettingpractice.com/
5. Video Tutorial: "IP Addressing & Subnetting" by PowerCert Animated Videos on YouTube

## 5. Tips for Teachers on Potential Challenges and How to Address Them

1. **Challenge**: Students struggling with binary-to-decimal conversion
   - **Solution**: Provide a binary-to-decimal conversion chart and practice exercises

2. **Challenge**: Difficulty understanding the concept of subnetting
   - **Solution**: Use physical analogies, such as dividing a large office space into smaller rooms

3. **Challenge**: Confusion between IPv4 and IPv6 addressing
   - **Solution**: Focus primarily on IPv4 for basic understanding, introduce IPv6 as an advanced topic

4. **Challenge**: Students having trouble with subnet calculations
   - **Solution**: Encourage the use of online subnet calculators to check work, provide step-by-step guides

5. **Challenge**: Relating IP addressing to real-world scenarios in Timor-Leste
   - **Solution**: Use examples of local businesses or government offices when creating practice scenarios

6. **Challenge**: Limited access to networking hardware for demonstrations
   - **Solution**: Utilize network simulation software or online virtual labs if available

7. **Challenge**: Varying levels of prior knowledge among students
   - **Solution**: Provide additional resources for advanced students and extra support for those who need it

8. **Challenge**: Students struggling to see the relevance of IP addressing in their daily lives
   - **Solution**: Discuss how IP addressing affects internet access and future technological development in Timor-Leste