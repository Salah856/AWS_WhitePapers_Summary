# Security Overview of AWS Lambda

 #AWS_WhitePaper_Summary 

- The managed runtime environment model further reduces the attack surface while making cloud security simpler. 
- This whitepaper presents the underpinnings of that model, along with best practices, to developers, security analysts, security and compliance teams, and other stakeholders.

## The Shared Responsibility Model
- Security and Compliance is a shared responsibility between AWS and the customer. 
- This shared responsibility model can help relieve your operational burden, as AWS operates, manages, and controls the components from the host operating system and virtualization layer, down to the physical security of the facilities in which the service operates.

![1](https://user-images.githubusercontent.com/23625821/127966363-024e9080-3a6c-4d36-ae80-4652256a5999.png)

## Lambda Functions and Layers
- With Lambda, you can run code virtually with zero administration of the underlying infrastructure.
- You are responsible only for the code that you provide Lambda, and the conﬁguration of how Lambda runs that code on your behalf.
- Today, Lambda supports two types of code resources: Functions and Layers.
- Layers can be used to share common code or data across diﬀerent functions or AWS accounts. 
- You can also control the entire lifecycle of your functions and layers through Lambda's control plane APIs. 
- For example, you can choose to delete your function by calling DeleteFunction, or revoke permissions from another account by calling RemovePermission.

