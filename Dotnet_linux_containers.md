# Modernize .NET Applications with Linux Containers

- Since the introduction of .NET Framework in 2002, more than six million developers have adopted the .NET programming ecosystem to build their applications.  
- In its initial form, .NET was built to run exclusively on the Windows operating system. 

- This resulted in large portfolios of applications running on .NET and Windows, particularly in the enterprise.
- Many organizations simultaneously want to move their VM-based deployments to containers, to predictably deploy their applications across environments, maximize the efficiency of their resource consumption, and introduce DevOps practices to automate their development lifecycle.

- Gartner predicts that by 2022, more than 75% of global organizations will be running containerized applications in production, up from less than 30% in 2020. 
- An IDC survey found that 45% of respondents’ application portfolio is running in containers today, and that is expected to increase to 60% in three years

- This paper walks through this use case of modernizing a .NET Framework application running on Windows VMs to .NET 5, and Linux containers running on Amazon Elastic Container Service (Amazon ECS) and AWS Fargate.
- This guide uses AWS Fargate for ECS to deploy containerized .NET Framework applications on AWS.


## Choosing container orchestration

- When choosing your container orchestration option, you should start with the question, “How much of the container infrastructure do I want to manage?” The following options are available to you:

- Self-Managed Containers on Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon Elastic Container Service 
- Amazon Elastic Kubernetes Service 
- AWS Fargate

## Cost considerations

### Cloud Computing 
- Cloud computing helps businesses reduce costs and complexity, adjust capacity on-demand, accelerate time-to-market, increase opportunities for innovation, and enhance security.
- Weighing the financial considerations of operating an on-premises data center versus using cloud infrastructure is not as simple as comparing hardware, storage, and compute costs.

### AWS pricing model
- AWS offers a simple, consistent, pay-as-you-go pricing model, so you are charged only for the resources you consume.
- 
