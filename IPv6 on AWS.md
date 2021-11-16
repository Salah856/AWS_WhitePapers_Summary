
# IPv6 on AWS

## Best practices for adopting and designing IPv6-based networks on AWS

- Every node connected to an Internet Protocol (IP) network must have an IP address for communication purposes. 

- As the internet continues to grow, so does the need for IP addresses. 

- IPv6 is a version of the Internet Protocol that uses a larger address space than its predecessor, IPv4. 

- This whitepaper focuses on best practices for adopting and designing IPv6-based networks on AWS Cloud. 

- It covers IPv6 dual-stack networks for both internet-facing and private IPv6 networks use cases.


## Intro

- An increasing number of organizations operate dual-stack IPv4/IPv6 networks. 
- Carrier networks and ISPs were the first groups to start deploying IPv6 on their networks, with mobile networks leading the charge. 
- Adoption of IPv6 has been delayed, partly due to NAT with IPv4, which takes private IP addresses and turns them into public IP addresses.

- An increasing number of organizations are adopting IPv6 in their environments, driven by the public IPv4 space exhaustion, private IPv4 scarcity, especially within large-scale networks, and the need to provide connectivity to IPv6-only clients. 
- There is no onesize-fits-all approach with IPv6; however, there are best practices AWS customers can follow to plan and implement IPv6 into their existing cloud networks. 

- This whitepaper explains key drivers for adoption and highlights best practices to guide you while leaving enough space for you to decide, based on your specific use case and implementation, how to approach IPv6 in your network.


### Tenets for IPv6 adoption

- Adhering to the following tenets for IPv6 adoption can help make the process and decision more manageable: 
   - Re-evaluate network controls — IPv6 offers opportunities to rethink your approach to perimeter security and make design decisions that further improve your security posture.
   - Design for scale — More usable IPv6 addresses doesn’t mean you can shortcut IP allocation and planning.
   - Phase your IPv6 adoption — Focus on your business needs to implement IPv6 where needed, and remember that IPv4 and IPv6 can be made to coexist as long as needed.
   

### Internet Protocol version 6

- IPv6 is the next generation IP address standard intended to supplement and eventually replace IPv4, the original and ubiquitous IP address scheme. 

- Every computer, mobile phone, home automation component, IoT sensor, and any other device connected to an IP-based network needs a numerical IP address to communicate with other devices.

- Public reachable IPv4 addresses are in short supply due to their widespread usage and constantly increasing demand stemming from the proliferation of connected devices globally. 

- The last available block of new IP version 4 (IPv4) addresses was allocated back in 2011, and from that time on, everyone has been reusing a finite set of available addresses. 

- IP version 6 (IPv6) is the replacement for IPv4, and it is designed to address the depletion of IP addresses, and change the way traffic is managed.


### IPv6 addressing

The IPv6 address space is organized by using format prefixes, that logically divide it in the form of a tree so that a route from one network to another can easily be found.


The main categories of IPv6 addresses are:
      - Aggregatable global unicast addresses (GUA) — 2000::/3
      - Unique-local unicast addresses (ULA) — FC00::/7
      - Link-local unicast addresses — FE80::/10
      - Multicast addresses — FF00::/8










### Reference

<a href="https://d1.awsstatic.com/whitepapers/IPv6-on-AWS.pdf"> Original paper </a> 
