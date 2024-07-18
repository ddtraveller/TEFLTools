# ## Learning Unit 3

## Learning Unit 3: Network Devices and Their Functions
- Objectives:
  * Identify common network devices
  * Explain the functions of hubs, switches, and routers
- Topics:
  * Hubs and repeaters
  * Switches and bridges
  * Routers and gateways
- Activities:
  * Hands-on exercise: Setting up a small LAN using available devices
  * Research on network devices used in Timorese institutions

## Unit Resources

# Lecture Notes

## Hubs and Repeaters

### Definition and Basic Function
- A hub is a basic networking device that operates at the physical layer (Layer 1) of the OSI model
- It serves as a central connection point for devices in a network
- Hubs simply broadcast incoming data to all connected devices

### Data Transmission Through a Hub
- When a device sends data through a hub:
  1. The hub receives the data on one port
  2. It regenerates the signal to maintain signal strength
  3. The data is then sent out to all other ports
- This process is called "flooding"

### Limitations of Hubs
- Collisions: Multiple devices can transmit simultaneously, causing data collisions
- Single collision domain: All ports on a hub share the same collision domain
- Bandwidth sharing: All connected devices share the total bandwidth
- Security concerns: Data is sent to all devices, even if not intended for them

### Repeaters
- Similar to hubs, but typically used to extend the range of a network
- Amplify and regenerate signals to overcome signal degradation over long distances

## Switches and Bridges

### Definition and Basic Function
- Switches operate at the data link layer (Layer 2) of the OSI model
- They create separate collision domains for each port
- Switches use MAC addresses to forward data only to the intended recipient

### Comparison to Hubs
- Switches are more intelligent than hubs
- They can learn which devices are connected to which ports
- Switches reduce network congestion by creating separate collision domains

### MAC Address Table
- Switches maintain a MAC address table (also called a forwarding table)
- The table maps MAC addresses to specific ports
- Switches learn MAC addresses by examining the source address of incoming frames

### How Switches Learn
1. When a frame arrives, the switch records the source MAC address and the port it came from
2. If the destination MAC is known, the frame is sent only to that port
3. If unknown, the frame is flooded to all ports except the one it came from
4. Over time, the switch builds a complete map of the network

### Benefits of Switches Over Hubs
- Improved performance: Reduced collisions and efficient use of bandwidth
- Enhanced security: Data is only sent to the intended recipient
- Scalability: Switches can handle larger networks more effectively

## Routers and Gateways

### Definition and Basic Function
- Routers operate at the network layer (Layer 3) of the OSI model
- They connect different networks and direct traffic between them
- Routers make decisions based on IP addresses

### Role in Connecting Different Networks
- Routers serve as the main gateway between networks
- They can connect networks with different protocols or architectures
- Routers determine the best path for data to travel across networks

### IP Addressing and Routing Tables
- Routers use IP addresses to make forwarding decisions
- They maintain routing tables containing:
  - Network destinations
  - Metrics (cost of reaching the destination)
  - Next hop (the next router in the path)
- Routing protocols (e.g., OSPF, BGP) help routers build and maintain these tables

### Difference Between Routers and Switches
- Switches operate within a single network, while routers connect multiple networks
- Switches use MAC addresses, routers use IP addresses
- Routers can perform Network Address Translation (NAT) and firewall functions

### Gateways
- A gateway is a node that serves as an entrance to another network
- It can be a router, but may also include additional functionality
- Gateways often perform protocol conversion between different network types

# Discussion Questions

1. How does the operation of a hub differ from that of a switch? What are the implications for network performance?

2. In what scenarios might a hub still be useful, despite its limitations compared to a switch?

3. Explain how a switch learns MAC addresses and builds its forwarding table. Why is this process important?

4. How does a router's function differ from that of a switch? In what situations would you need a router instead of just a switch?

5. Discuss the potential security implications of using hubs versus switches in a network.

6. How might the choice of network devices (hubs, switches, routers) impact the scalability of a network?

7. In the context of Timor-Leste's developing technological landscape, what challenges might be faced when implementing more advanced networking devices?

8. How do routers facilitate communication between different types of networks? Why is this important for internet connectivity?

9. Explain the concept of a collision domain. How do hubs and switches differ in their handling of collision domains?

10. What role do gateways play in network communication? How might they be used in connecting Timorese networks to the global internet?

# Writing Exercise Instructions

## Network Device Comparison Essay

Write a 500-word essay comparing and contrasting hubs, switches, and routers. Your essay should cover the following points:

1. The basic function of each device
2. The OSI layer at which each device operates
3. How each device handles data transmission
4. The advantages and disadvantages of each device
5. Typical use cases for each device in a network

Structure your essay with an introduction, body paragraphs for each device, a comparison section, and a conclusion. Use specific examples to illustrate your points.

# Assignment Details

## Research Project: Network Devices in Timorese Institutions

### Objective
Investigate the types of network devices used in various institutions across Timor-Leste and analyze their effectiveness in meeting the institution's networking needs.

### Requirements
1. Choose at least two different types of institutions (e.g., government office, school, hospital, business)
2. Research and identify the network devices used in each institution
3. Analyze the suitability of these devices for the institution's needs
4. Suggest potential improvements or upgrades, if applicable

### Deliverables
1. A 3-5 page report detailing your findings, including:
   - Introduction to the chosen institutions
   - Description of network devices used
   - Analysis of device suitability
   - Recommendations for improvements
2. A network diagram for each institution, showing the placement and connections of devices
3. A 5-minute presentation summarizing your findings and recommendations

### Evaluation Criteria
- Accuracy of technical information
- Depth of research and analysis
- Quality of recommendations
- Clarity of written report and diagrams
- Effectiveness of oral presentation

# Additional Materials

## Network Device Comparison Chart

| Feature | Hub | Switch | Router |
|---------|-----|--------|--------|
| OSI Layer | Physical (Layer 1) | Data Link (Layer 2) | Network (Layer 3) |
| Addressing | None | MAC Address | IP Address |
| Data Forwarding | Broadcasts to all ports | Sends to specific port | Routes between networks |
| Collision Domains | Single | Multiple | N/A |
| Broadcast Domains | Single | Single | Multiple |
| Typical Use | Very small networks | LAN segmentation | Connecting networks |
| Intelligence | Low | Medium | High |
| Cost | Low | Medium | High |

## Simple Network Diagrams

### Hub-based Network
```
   Device A
      |
      |
 [Hub]----Device B
      |
      |
   Device C
```

### Switch-based Network
```
   Device A
      |
      |
[Switch]----Device B
      |
      |
   Device C
```

### Router-connected Networks
```
Network A        Network B
   |                |
   |                |
[Router A]------[Router B]
   |                |
   |                |
Network C        Network D
```

## Glossary of Key Terms

- **Collision**: When two or more devices attempt to send data simultaneously on a shared network segment.
- **Broadcast Domain**: A logical division of a computer network, in which all nodes can reach each other by broadcast at the data link layer.
- **MAC Address**: A unique identifier assigned to network interfaces for communications at the data link layer.
- **IP Address**: A numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
- **NAT (Network Address Translation)**: A method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.
- **OSPF (Open Shortest Path First)**: A routing protocol for Internet Protocol networks.
- **BGP (Border Gateway Protocol)**: A standardized exterior gateway protocol designed to exchange routing and reachability information among autonomous systems on the Internet.