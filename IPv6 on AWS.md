

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

### IPv6 adoption strategies and mechanisms

Working with customers, AWS observed the following two main drivers for IPv6 adoption.

   - Network Address Translation is no longer sufficient to work around exhaustion and poses significant challenges with overlapping IP addresses.
   - There are numerous organizational or regulatory mandates to adopt IPv6. 
   

Following is a summary of IPv6 adoption drivers:

- Mandated IPv6 endpoints — Either mandated by a government policy or an industry regulator, and not necessarily tied to a particular use case.


- Interoperability with IPv6 networks — The last years have seen a growing population of IPv6-only clients, and as a result so have the number of organizations wanting to cater to this user base. With the number of mobile IPv6-only users, many companies find they can’t afford to lose that section of their potential user base.

- Public IPv4 exhaustion — As public IPv4 addresses become more scarce, allocating contiguous IP address ranges for public routing becomes more difficult and costly.

- Private IPv4 exhaustion — As private IPv4 (RFC1918) addresses become exhausted and too fragmented within organizations’ private networks, IPv6-only networks offer opportunities to address additional nodes.

IPv6 adoption strategy depends on the driving force behind it. You may have an immediate goal such as addressing private IPv4 exhaustion, or the ability to provide IPv6 service endpoints as per government mandate, with the long-term goal of fully converting to an IPv6 only network. 

Following are the four main driving forces, and the corresponding adoption strategy:

- Private IPv4 exhaustion — The goal is to provision new nodes and allocate routable IP addresses without IP overlap, and without the challenge of sourcing contiguous and usable IP addresses.

- Adoption strategy — Configure IPv6-only routing between dual stack network segments, to facilitate communication using the IPv6 stack. Provide IPv6 to IPv4 interoperability layer, such as dual-stack load balancers. 


- Public IPv4 exhaustion — The goal is to support IPv6 only nodes connecting to your public endpoints. As an example, you may have an API endpoint for data upload from IoT devices which are connected to an IPv6-only network. The IoT devices have IPv6 addresses, and the network does not provide interoperability layer to IPv4. Other devices may operate in IPv4 networks.

- Adoption strategy — Create dual-stack VPCs and subnets. Configure AWS services such as load balancers and edge service in dual-stack mode with corresponding DNS record on the AWS Cloud. Optionally, provide separate endpoints for IPv4 and IPv6 in dedicated IPv4-only or IPv6-only deployments.


### Interoperability

Although operating in dual-stack mode solves a lot of the problems with IPv4 and IPv6 interoperability, it creates management overhead. For example, security becomes harder because you have to manage two sets of security rules, one for each network stack. Routing and troubleshooting become harder, and you have to maintain additional records to existing DNS names.

You may be able to avoid making the entire network dual-stack by focusing on implementing dual-stack at your border via load balancers. Existing segments of your network can continue to operate as IPv4 in most cases, and new segments are built with IPv6. Focus on implementing and operating interoperability layer where AWS services such as dual-stack VPC and load balancers, to help you solve interoperability challenges.



### Planning IPv6 adoption in the AWS Cloud network

Elastic network interfaces in an IP network could operate in three different modes:

- IPv4-only mode — Your resources can communicate over IPv4, and if communicating to IPv6 nodes, require an interoperability layer.

- IPv6-only mode — Your resources can communicate over IPv6, and if communicating to IPv4 nodes, require an interoperability layer.

- Dual-stack mode — Your resources can communicate over both IPv4 and IPv6.

A separate interoperability layer is not required

#### IPv6 addressing plan on AWS

Coming up with an IPv6 addressing plan is one of the most important initial tasks for any organization proceeding with IPv6 adoption. For most organizations, IPv6 is deployed in parallel with IPv4 in existing IPv4 AWS and hybrid networks. 

IPv4 addressing plans tend to grow over time, and consequently may be highly fragmented, not contiguous, or not big enough. Simply duplicating the IPv4 addressing scheme in
some fashion in IPv6 might initially prove advantageous. 

However, any temporary advantage gained by such a shortcut will ultimately be surpassed by the ease and efficiency of operation and design offered by a proper IPv6 addressing plan that incorporates the key benefits of the larger allocations possible with IPv6. 


#### AWS-assigned IPv6 VPC CIDR

By default, Amazon provides one fixed size (/56) IPv6 CIDR block to a VPC. This range is assigned by the service, and consequently, you can’t assign contiguous IPv6 CIDR blocks to VPCs in the same Region or based on other custom-defined criteria.

For customers that have a large VPC footprint in AWS and prefer to use IP route summarization to simplify their overall environment, bring your own IPv6 (BYOIPv6) described, in the next section, may be the preferred solution.



#### BYOIPv6 VPC CIDR

Alternatively, if you own an IPv6 address space, you can import it into AWS using the Bring Your Own IPv6 service. The smallest IPv6 address range that you can bring is /48 for CIDRs that are publicly advertised by AWS, and /56 for CIDRs that are not publicly advertised by AWS. 


You can also choose to bring a /48 and mark it as non-advertisable, keeping control of IP advertisements on your on-premises setup. After importing it, you can assign /56 ranges from the space to individual VPCs in the same account.











### Reference

<a href="https://d1.awsstatic.com/whitepapers/IPv6-on-AWS.pdf"> Original paper </a> 
