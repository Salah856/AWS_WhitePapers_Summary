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

- The twelve factors are a set of best practices for building modern applications that are optimized for cloud computing. The twelve factors cover four key areas: deployment, scale, portability, and architecture:

 1. Codebase - One codebase tracked in revision control, many deploys
 2. Dependencies - Explicitly declare and isolate dependencies
 3. Conﬁg - Store conﬁgurations in the environment
 4. Backing services - Treat backing services as attached resources
 5. Build, release, run - Strictly separate build and run stages
 6. Processes - Execute the app as one or more stateless processes
 7. Port binding - Export services via port binding
 8. Concurrency - Scale out via the process model
 9. Disposability - Maximize robustness with fast startup and graceful shutdown
 10. Dev/prod parity - Keep development, staging, and production as similar as possible
 11. Logs - Treat logs as event streams
 12. Admin processes - Run admin/management tasks as one-oﬀ processes


## Componentization Via Services

- In a microservices architecture, software is composed of small independent services that communicate over well-deﬁned APIs.
- An analogy can be drawn to the Walkman portable audio cassette players that were popular in the 1980s: batteries bring power, audio tapes are the medium, headphones deliver output, while the main tape player takes input through key presses. Using them together plays music.
- Similarly, microservices need to be decoupled, and each should focus on one functionality. Additionally, a microservices architecture allows for replacement or upgrade. 

- Using the Walkman analogy, if the headphones are worn out, you can replace them without replacing the tape player. 
- Through modularization, microservices oﬀer developers the freedom to design each feature as a black box. That is, microservices hide the details of their complexity from other components. 
- Any communication between services happens by using well-deﬁned APIs to prevent implicit and hidden dependencies.
- Container images allow for modularity in services. 
- They are constructed by building functionality onto a base image. 
- Developers, operations teams, and IT leaders should agree on base images that have the security and tooling proﬁle that they want. These images can then be shared throughout the organization as the initial building block. 
- Replacing or upgrading these base images is as simple as updating the FROM ﬁeld in a Dockerﬁle and rebuilding, usually through a Continuous Integration/Continuous Delivery (CI/CD) pipeline.

- Here are the key factors from the twelve-factor app pattern methodology that play a role in componentization:
  - Dependencies (explicitly declare and isolate dependencies) – Dependencies are self-contained within the container and not shared with other services.
  - Disposability (maximize robustness with fast startup and graceful shutdown) – Disposability is leveraged and satisﬁed by containers that are easily pulled from a repository and discarded when they stop running.
  - Concurrency (scale out via the process model) – Concurrency consists of tasks or pods (made of containers working together) that can be auto scaled in a memory- and CPU-eﬃcient manner.


## Organized Around Business Capabilities
- Before microservices, system architecture would be organized around technological capabilities such as user interface, database, and server-side logic. 
- In a microservices-based approach, as a best practice, each development team owns the lifecycle of its service all the way to the customer. 
- For example, a recommendations team might own development, deployment, production support, and collection of customer feedback.
- Organizations which design systems ... are constrained to produce designs which are copies of the communication structures of these organizations. "Conway's Law"
- When architecture and capabilities are organized around atomic business functions, dependencies between components are loosely coupled. As long as there is a communication contract between services and teams, each team can run at its own speed. 
- With this approach, the stack can be polyglot, meaning that developers are free to use the programming languages that are optimal for their component.
- For example, the user interface can be written in JavaScript or HTML5, the backend in Java, and data processing can be done in Python.

- The following are key factors from the twelve-factor app pattern methodology that play a role in organizing around capabilities:
   - Codebase (one codebase tracked in revision control, many deploys) –Each microservice owns its own codebase in a separate repository and throughout the lifecycle of the code change.
   - Build, release, run (strictly separate build and run stages) – Each microservice has its own deployment pipeline and deployment frequency. This allows the development teams to run microservices at varying speeds so they can be responsive to customer needs.
   - Processes (execute the app as one or more stateless processes) – Each microservice does one thing and does that one thing really well. The microservice is designed to solve the problem at hand in the best possible manner.
   - Admin processes (run admin/management tasks as one-oﬀ processes) – Each microservice has its own administrative or management tasks so that it functions as designed. 

- To achieve a microservices architecture that is organized around business capabilities, use popular microservices design patterns. 
- A design pattern is a general, reusable solution to a commonly occurring problem within a giving context.

- Popular miscroservice design patterns include:
   - Aggregator Pattern – A basic service which invokes other services to gather the required information or achieve the required functionality. This is beneﬁcial when you need an output by combining data from multiple microservices.
   - API Gateway Design Pattern – API Gateway also acts as the entry point for all the microservices and creates ﬁne-grained APIs for diﬀerent types of clients. It can fan out the same request to multiple microservices and similarly aggregate the results from multiple microservices.
   - Chained or Chain of Responsibility Pattern – Chained or Chain of Responsibility Design Patterns produces a single output which is a combination of multiple chained outputs. object.
   - Asynchronous Messaging Design Pattern – In this type of microservices design pattern, all the services can communicate with each other, but they do not have to communicate with each other sequentially and they usually communicate asynchronously.


