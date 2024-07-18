# ## Learning Unit 2

## Learning Unit 2: Network Models and Protocols
- Objectives:
  * Explain the OSI and TCP/IP models
  * Understand the function of different protocol layers
- Topics:
  * OSI model layers
  * TCP/IP model
  * Common protocols (HTTP, FTP, SMTP)
- Activities:
  * Compare OSI and TCP/IP models
  * Analyze a network packet using Wireshark (if resources allow)

## Unit Resources

# Lecture Notes

## OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework used to describe the functions of a networking system. The model uses layers to help give a visual description of what is going on with a particular networking system.

### The 7 Layers of the OSI Model

1. Physical Layer
   - Deals with the physical connection between devices
   - Defines specifications for cables, connectors, and network interface cards
   - Responsible for transmitting raw bits over a physical medium

2. Data Link Layer
   - Provides node-to-node data transfer
   - Detects and possibly corrects errors that may occur in the physical layer
   - Defines how data is formatted for transmission and how access to the network is controlled

3. Network Layer
   - Provides routing and switching technologies
   - Manages addressing, tracking, and determining the best path for data transfer

4. Transport Layer
   - Provides transparent transfer of data between end systems
   - Responsible for end-to-end error recovery and flow control

5. Session Layer
   - Establishes, manages, and terminates connections between applications
   - Provides for full-duplex, half-duplex, or simplex operation

6. Presentation Layer
   - Ensures that the information sent by the application layer of one system is readable by the application layer of another system
   - Manages data encryption, compression, and format conversions

7. Application Layer
   - Provides network services directly to end-users or applications
   - Includes protocols like HTTP, FTP, SMTP, etc.

### Encapsulation in the OSI Model

Encapsulation is the process by which data is packaged as it moves down the OSI layers:
1. User data is passed from the application layer down through the layers
2. Each layer adds its own header (and sometimes trailer) information
3. By the time data reaches the physical layer, it has been encapsulated into a frame

## TCP/IP Model

The TCP/IP model is a more practical, condensed version of the OSI model, used in real-world networking.

### The 4 Layers of the TCP/IP Model

1. Network Access Layer (combines OSI Physical and Data Link layers)
   - Handles the physical infrastructure and how data is sent over the network

2. Internet Layer (equivalent to OSI Network layer)
   - Manages addressing and routing of data packets

3. Transport Layer (equivalent to OSI Transport layer)
   - Ensures reliable data transmission

4. Application Layer (combines OSI Session, Presentation, and Application layers)
   - Handles high-level protocols, representation, and control functions

### Comparison with OSI Model

- TCP/IP is simpler, combining several OSI layers
- TCP/IP is more practical and widely used in real networks
- Both models use the concept of layering and encapsulation

## Common Protocols

### HTTP (Hypertext Transfer Protocol)
- Used for transmitting web pages over the internet
- Operates at the Application layer of both OSI and TCP/IP models
- Uses client-server model: client sends requests, server responds with web content

### FTP (File Transfer Protocol)
- Used for transferring files between computers over a network
- Also operates at the Application layer
- Supports both anonymous and authenticated access to file servers

### SMTP (Simple Mail Transfer Protocol)
- Used for sending email messages between servers
- Another Application layer protocol
- Works in conjunction with other protocols like POP3 or IMAP for email retrieval

# Discussion Questions

1. How does the layered approach in both OSI and TCP/IP models benefit network design and troubleshooting?

2. Compare and contrast the OSI and TCP/IP models. Which do you think is more relevant for modern networking, and why?

3. How does encapsulation work in the context of network models? Provide an example of how data might be encapsulated as it moves through the layers.

4. Discuss the role of protocols in networking. How do protocols like HTTP, FTP, and SMTP facilitate communication between different systems?

5. In the context of Timor-Leste's developing technological landscape, which layers of the OSI or TCP/IP model do you think are most critical for improvement? Why?

6. How might understanding these network models and protocols benefit IT professionals in Timor-Leste?

7. Considering the common protocols we've discussed (HTTP, FTP, SMTP), can you think of any specific applications or services in Timor-Leste that rely heavily on these protocols?

8. How do you think the evolution of network protocols has impacted global connectivity, and how might it affect Timor-Leste's integration into the global digital economy?

# Writing Exercise Instructions

Write a 500-word essay comparing the OSI and TCP/IP models. Your essay should:

1. Briefly introduce both models and their purposes
2. Compare the layers of each model, highlighting similarities and differences
3. Discuss the strengths and weaknesses of each model
4. Explain which model is more commonly used in practice and why
5. Conclude with your thoughts on the relevance of these models in understanding modern networking, particularly in the context of Timor-Leste's developing IT infrastructure

Your essay should demonstrate a clear understanding of both models and use specific examples to illustrate your points. Be sure to use proper citation if you reference any external sources.

# Assignment Details

## Packet Analysis Assignment

### Objective
To gain practical experience in analyzing network traffic and understanding how protocols operate at different layers of the network model.

### Instructions
1. Download and install Wireshark on your computer (if not already available in your lab).
2. Capture network traffic for 5 minutes while performing various online activities (browsing websites, sending an email, etc.).
3. Analyze the captured traffic and identify packets from at least three different protocols (e.g., HTTP, DNS, TCP).
4. For each identified protocol:
   a. Determine which layer of the OSI and TCP/IP models it operates on
   b. Explain the purpose of the protocol
   c. Describe the key information found in the packet headers
5. Create a report (2-3 pages) detailing your findings, including screenshots of relevant packet information.

### Submission
Submit your report as a PDF document, including any necessary screenshots or diagrams.

### Grading Criteria
- Correct identification of protocols: 30%
- Accurate mapping to OSI and TCP/IP layers: 20%
- Clear explanation of protocol purposes: 20%
- Detailed analysis of packet headers: 20%
- Overall report quality and presentation: 10%

# Additional Materials

## OSI Model Mnemonic Device

To help remember the seven layers of the OSI model in order (from bottom to top), use this mnemonic:

"Please Do Not Throw Sausage Pizza Away"

- Physical
- Data Link
- Network
- Transport
- Session
- Presentation
- Application

## TCP/IP Protocol Suite Diagram

```
           +---------------------+
           |    Application      |
           |   (HTTP, FTP, DNS)  |
           +---------------------+
           |      Transport      |
           |     (TCP, UDP)      |
           +---------------------+
           |      Internet       |
           |        (IP)         |
           +---------------------+
           |    Network Access   |
           | (Ethernet, Wi-Fi)   |
           +---------------------+
```

This diagram illustrates the four layers of the TCP/IP model and examples of protocols at each layer.

## Real-world Protocol Example: HTTP Request

Here's an example of a simple HTTP request:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
```

This request demonstrates:
- The HTTP protocol operating at the Application layer
- Key information like the requested resource, host, and user agent
- How protocols structure data for communication between systems