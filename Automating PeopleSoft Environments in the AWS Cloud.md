

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



## Environment Architecture

The application architecture of a PeopleSoft environment in the AWS Cloud was designed to be scalable for production environments and flexible for smaller workloads of non-production environments. 

Using AWS CloudFormation and Amazon ECS ensures that each environment is deployed and configured in a consistent manner.

The AWS CloudFormation templates create the VPC, load balancers, Amazon EC2 servers, Amazon ECS clusters, and Amazon RDS instances, that form the environments. 

The Amazon VPC restricts access to the environments to only customer-approved users.


Automation scripts and AWS CloudFormation are used to generate two types of deployments: one for the production environment and one for the non-production environments. 

The automation scripts for both the production and non-production environments use all of the same components, however, they are composed and behave differently


### Amazon ECS Service Design

Amazon ECS orchestrates Docker containers and creates tasks, or groups of container services, that are essential elements of the environments. 

Amazon ECS also monitors the health of these tasks and launches new tasks if an issue with an existing task is detected. 

The Docker images in Amazon ECR and managed by Amazon ECS contain the instructions necessary to build out the web, application, and batch containers. 

For example, the Amazon ECS task definition might combine a web and app container into a single task which can be monitored and managed by Amazon ECS.


### Scalable Production Deployment

Production environment deployments are built to allow the online transaction processing application, process scheduler, and integration brokers to be decoupled into separate Amazon ECS services. 

This allows each component to be scaled independently. The following are some examples of methods you can use to scale your production environments up or down to meet your business needs.

In off-peak hours, a production environment can be scaled down to a minimal footprint. 

This allows the application to continue to be available, but takes advantage of cost savings by only running a minimal set of resources.






### Reference

<a href="https://d1.awsstatic.com/whitepapers/Automating-PeopleSoft-Environments-in-AWS-Cloud.pdf?did=wp_card&trk=wp_card"> Original paper </a>
