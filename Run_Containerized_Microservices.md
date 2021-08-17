# Running Containerized Microservices on AWS

- This whitepaper is intended for architects and developers who want to run containerized applications at scale in production on Amazon Web Services (AWS). 
- This document provides guidance for application lifecycle management, security, and architectural software design patterns for container-based applications on AWS.

- It also discusses architectural best practices for adoption of containers on AWS, and how traditional software design patterns evolve in the context of containers. 

- It leverages Martin Fowler’s principles of microservices and map them to the twelve-factor app pattern and real-life considerations. 
- After reading this paper, you will have a starting point for building microservices using best practices and software design patterns.
- Microservices are an architectural and organizational approach to software development in which software is composed of small, independent services that communicate to each other.
- There are diﬀerent ways microservices can communicate, but the two commonly used protocols are HTTP request/response over well-deﬁned APIs, and lightweight asynchronous messaging.
- Microservices architectures make applications easier to scale and faster to develop.
- This enables innovation and accelerates time-to-market for new features. Containers also provide isolation and packaging for software, and help you achieve more deployment velocity and resource density.

- As proposed by Martin Fowler, the characteristics of a microservices architecture include the following:
  - Componentization via services
  - Organized around business capabilities
  - Products not projects
  - Smart endpoints and dumb pipes
  - Decentralized governance
  - Decentralized data management
  - Infrastructure automation
  - Design for failure
  - Evolutionary design

