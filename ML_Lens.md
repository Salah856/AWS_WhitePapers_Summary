
# Machine Learning Lens - AWS Well-Architected Framework 

- This document describes the Machine Learning Lens for the AWS Well-Architected Framework. The document includes common machine learning (ML) scenarios and identifies key elements to ensure that your workloads are architected according to best practices.

- While designing ML workloads, you should use applicable best practices and questions from the AWS Well-Architected Framework whitepaper.

- The Machine Learning Lens is based on five pillars: operational excellence, security, reliability, performance efficiency, and cost optimization. AWS provides multiple core components for ML workloads that enable you to design robust architectures for your ML applications.

- There are two areas that you should evaluate when you build a machine learning workload:
 1. Machine Learning Stack 
 2. Phases of ML Workloads 

- When you build an ML-based workload in AWS, you can choose from different levels of abstraction to ML Services ML Frameworks and Infrastructure. 

-  The AI Services level provides fully managed services that enable you to quickly add ML capabilities

- The ML Frameworks and Infrastructure level is intended for expert machine learning practitioners.


- Building and operating a typical ML workload is an iterative process, and consists of multiple phases, like in the following figure.


![crisp-dm](https://user-images.githubusercontent.com/23625821/124374931-72457f00-dc9f-11eb-894d-fc75d3d8b5f8.png)

- In Business Goal Identification phase: 

1. You will want to validate that ML is the appropriate approach to deliver your business goal.
2. You will need training data to train and benchmark your ML model, but you also need data from the business to evaluate the value of an ML solution.

3. Understand business requirements
4. Determine a project’s ML feasibility and data requirements
5. Evaluate the cost of data acquisition, training, inference, and wrong predictions

- In ML Problem Framing Phase: 

1. You have to establish an observable and quantifiable performance metric for the project, such as accuracy. 
2. You need to formulate the ML question in terms of inputs, desired outputs, and the performance metric to be. 



