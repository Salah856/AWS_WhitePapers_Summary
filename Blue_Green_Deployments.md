
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





















#### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/blue-green-deployments.pdf#welcome"> Original paper </a>







