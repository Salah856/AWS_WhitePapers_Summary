# Amazon Aurora MySQL Database Administrator’s Handbook

- This paper outlines the best practices for managing database connections, setting server connection parameters, and configuring client programs, drivers, and connectors. 

- It’s a recommended read for Amazon Aurora MySQL Database Administrators (DBAs) and application developers.

## Introduction

- Amazon Aurora MySQL (Aurora MySQL) is a managed relational database engine, wire-compatible with MySQL 5.6 and 5.7. Most of the drivers, connectors, and tools that you currently use with MySQL can be used with Aurora MySQL with little or no change.

- Aurora MySQL database (DB) clusters provide advanced features such as:

    - One primary instance that supports read/write operations and up to 15 Aurora Replicas that support read-only operations. 
    
    - Each of the Replicas can be automatically promoted to the primary role if the current primary instance fails.

    - A cluster endpoint that automatically follows the primary instance in case of failover.
    
    - A reader endpoint that includes all Aurora Replicas and is automatically updated when Aurora Replicas are added or removed.
    
    - Ability to create custom DNS endpoints containing a user-configured group of database instances within a single cluster.
    
    - Internal server connection pooling and thread multiplexing for improved scalability. 


## DNS endpoints

- An Aurora DB cluster consists of one or more instances and a cluster volume that manages the data for those instances. 

- There are two types of instances:

  - Primary instance – Supports read and write statements. Currently, there can be one primary instance per DB cluster.

  - Aurora Replica – Supports read-only statements. 
    - A DB cluster can have up to 15 Aurora Replicas. 
    - The Aurora Replicas can be used for read scaling, and are automatically used as failover targets in case of a primary instance failure.


- Amazon Aurora supports the following types of Domain Name System (DNS) endpoints:
  
  - Cluster endpoint – Connects you to the primary instance and automatically follows the primary instance in case of failover, that is, when the current primary instance is demoted and one of the Aurora Replicas is promoted in its place.

  - Reader endpoint – Includes all Aurora Replicas in the DB cluster under a single DNS CNAME. You can use the reader endpoint to implement DNS round robin load balancing for read-only connections.

  - Instance endpoint – Each instance in the DB cluster has its own individual endpoint. You can use this endpoint to connect directly to a specific instance.

  - Custom endpoints – User-defined DNS endpoints containing a selected group of instances from a given cluster.


## Connection handling in Aurora MySQL and MySQL










### Reference 

<a href="https://d1.awsstatic.com/whitepapers/RDS/amazon-aurora-connection-management-handbook.pdf?did=wp_card&trk=wp_card"> Original paper </a>

