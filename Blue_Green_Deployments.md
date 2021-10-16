
# Blue/Green Deployments on AWS

- The blue/green deployment technique enables you to release applications by shifting traffic between two identical environments that are running different versions of the application. 
- Blue/green deployments can mitigate common risks associated with deploying software, such as downtime and rollback capability. 
- This whitepaper provides an overview of the blue/green deployment methodology and describes techniques customers can implement using Amazon Web Services (AWS) services and tools. 
- It also addresses considerations around the data tier, which is an important component of most applications.


## Blue/Green Deployment Methodology

- Blue/green deployments provide releases with near zero-downtime and rollback capabilities. 
- The fundamental idea behind blue/green deployment is to shift traffic between two identical environments that are running different versions of your application. 

- The blue environment represents the current application version serving production traffic. 
- In parallel, the green environment is staged running a different version of your application. 
- After the green environment is ready and tested, production traffic is redirected from blue to green. 
- If any problems are identified, you can roll back by reverting traffic back to the blue environment.



## Benefits of Blue/Green

- After you deploy the green environment, you have the opportunity to validate it. 
- You might do that with test traffic before sending production traffic to the green environment, or by using a very small fraction of production traffic, to better reflect real user traffic. 
- This is called canary analysis or canary testing. 
- If you discover the green environment is not operating as expected, there is no impact on the blue environment. 
- You can route traffic back to it, minimizing impaired operation or downtime and limiting the blast radius of impact.

- This ability to simply roll traffic back to the operational environment is a key benefit of blue/green deployments. 
- You can roll back to the blue environment at any time during the deployment process. 
- Impaired operation or downtime is minimized because impact is limited to the window of time between green environment issue detection and shift of traffic back to the blue environment. 

- Additionally, impact is limited to the portion of traffic going to the green environment, not all traffic. 
- If the blast radius of deployment errors is reduced, so is the overall deployment risk. 
- Blue/green deployments also work well with continuous integration and continuous deployment (CI/CD) workflows, in many cases limiting their complexity. 
- Your deployment automation has to consider fewer dependencies on an existing environment, state, or configuration as your new green environment gets launched onto an entirely new set of resources.



## Define the Environment Boundary

- When planning for blue/green deployments, you have to think about your environment boundary, where have things changed and what needs to be deployed to make those changes live. 
- The scope of your environment is influenced by a number of factors: 

Application architecture: Dependencies, loosely/tightly coupled

Organization: Speed and number of iterations

Risk and complexity: Blast radius and impact of failed deployment

People: Expertise of teams

Process: Testing/QA, rollback capability

Cost: Operating budgets, additional resources


For example, organizations operating applications that are based on the microservices architecture pattern could have smaller environment boundaries because of the loose coupling and well-defined interfaces between the individual services. 

Organizations running legacy, monolithic apps can still leverage blue/green deployments, but the environment scope can be wider and the testing more extensive. 

Regardless of the environment boundary, you should make use of automation wherever you can to streamline the process, reduce human error, and control your costs.

## Services for blue/green deployments

- Amazon Route 53
- Elastic Load Balancing
- Auto Scaling
- AWS Elastic Beanstalk
- AWS OpsWorks
- AWS Cloudformation
- Amazon CloudWatch
- AWS CodeDeploy


There are three ways traffic can be shifted during a deployment on Amazon Elastic Container Services (Amazon ECS).

1. Canary – Traffic is shifted in two increments.
2. Linear – Traffic is shifted in equal increments.
3. All-at-once – All traffic is shifted to the updated tasks.


### AWS Lambda Hooks

With AWS Lambda hooks, CodeDeploy can call the Lambda function during the various lifecycle events including deployment of ECS, Lambda function deployment, and EC2/On-premise deployment. The hooks are helpful in creating a deployment workflow for your apps.


## Implementation Techniques

- The following techniques are examples of how you can implement blue/green on AWS. 
- While AWS highlights specific services in each technique, you may have other services or tools to implement the same pattern. 
- Choose the appropriate technique based on the existing architecture, the nature of the application, and the goals for software deployment in your organization. - Experiment as much as possible to gain experience for your environment and to understand how the different deployment risk factors affect your specific workload.


### Update DNS Routing with Amazon Route 53

- DNS routing through record updates is a common approach to blue/green deployments. 
- DNS is used as a mechanism for switching traffic from the blue environment to the green and vice versa when rollback is necessary. 
- This approach works with a wide variety of environment configurations, as long as you can express the endpoint into the environment as a DNS name or IP address.

- Within AWS, this technique applies to environments that are:

    - Single instances, with a public or Elastic IP address
    - Groups of instances behind an Elastic Load Balancing load balancer, or third-party load balancer
    - Instances in an Auto Scaling group with an Elastic Load Balancing load balancer as the front end
    
    - Services running on an Amazon Elastic Container Service (Amazon ECS) cluster fronted by an Elastic Load Balancing load balancer
    - Elastic Beanstalk environment web tiers
    - Other configurations that expose an IP or DNS endpoint


You can shift traffic all at once or you can do a weighted distribution. For weighted distribution with Amazon Route 53, you can define a percentage of traffic to go to the green environment and gradually update the weights until the green environment carries the full production traffic. 

This provides the ability to perform canary analysis where a small percentage of production traffic is introduced to a new environment. You can test the new code and monitor for errors, limiting the blast radius if any issues are encountered. It also allows the green environment to scale out to support the full production load if you’re using Elastic Load Balancing(ELB), for example. ELB automatically scales its request-handling capacity to meet the inbound application traffic; the process of scaling isn’t instant, so we recommend that you test, observe, and understand your traffic patterns. Load balancers can also be pre-warmed (configured for optimum capacity) through a support request.



### Swap the Auto Scaling Group Behind the Elastic Load Balancer










#### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/blue-green-deployments.pdf#welcome"> Original paper </a>







