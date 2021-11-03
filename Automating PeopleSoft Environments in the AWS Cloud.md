

# Automating PeopleSoft environments in the AWS Cloud

- Numerous enterprises have successfully migrated their Oracle PeopleSoft (PeopleSoft) applications to the Amazon Web Services (AWS) Cloud. 

- The majority of these migrations have been lift-and-shift projects, which are projects in which a static architecture, similar to the enterprise’s previous on-premises-based deployment, is recreated in the AWS Cloud. 

- Such enterprises have effectively used the AWS infrastructure as a service (IaaS) offering to outsource their data centers to the AWS Cloud.


### Benefits of Automating PeopleSoft Environments in the AWS Cloud

- Automating PeopleSoft environments in the AWS Cloud has several very important benefits, including the following.

  - Flexibility 
  - Consistency
  - Change Control
  - Stability
  - Scalability
  - Security
  - Economics
 

### Automation Tools in Action

#### Docker

- This automation process relies heavily on the Docker2 open source tool. Docker allows components of the PeopleSoft applications to be containerized. 
- This means they are run in isolation from the host operating system and other containers that run on the host machine. 
- It also means that because the application is containerized, deployment and orchestration automation can be developed in a standard way. 

- The Automations leverage existing infrastructure automations from AWS and use Amazon ECS instead of building custom automations to provision and scale applications and environments.

- In some ways, Docker is similar to virtual machine software. Like virtual machine software, Docker automates the creation of a well-defined and consistently deployed workspace. 

- Unlike virtual machine software, Docker accomplishes this by sharing the host operating system kernel and using kernel functionality to create an isolated
workspace.

- Docker uses the kernel in the host machine to create an isolated workspace, known as a container, where an application and its dependencies can run consistently and reliably.

- The process to create a container begins with a Dockerfile, which is a script written in the Go programming language, composed of various commands and arguments listed successively, which perform actions on an existing, base Docker image to create a new, more specialized Docker image. 


### AWS CloudFormation

- AWS CloudFormation is an AWS service through which users can create a template that describes all the AWS infrastructure resources needed to create user-defined
services. 

- AWS CloudFormation takes care of provisioning and configuring all the specified infrastructure components and services. The AWS CloudFormation template describes exactly what resources are provisioned and their settings. 

- Templates are text files, so users can see the differences in template versions and track changes in their infrastructure solution



### Amazon ECS

- Amazon Elastic Container Service (Amazon ECS) is a scalable, container management solution that supports Docker containers. 

- Amazon ECS schedules, runs, and scales containerized applications on AWS. 

- Amazon ECS can launch and stop Docker-enabled applications, 
- query the complete state of such applications, and access many AWS features, such as IAM roles, security groups, load balancers, and AWS CloudFormation


### Amazon RDS

- Amazon RDS is a web service that simplifies the setup, operation, and scaling of a relational database in the AWS Cloud. 

- Amazon RDS provides cost-efficient, resizable capacity for an industry-standard relational database, and manages common database administration tasks




### Reference

<a href="https://d1.awsstatic.com/whitepapers/Automating-PeopleSoft-Environments-in-AWS-Cloud.pdf?did=wp_card&trk=wp_card"> Original paper </a>