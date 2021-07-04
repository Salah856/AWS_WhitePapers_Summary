
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

- Data Preparation phase: 

1. AWS provides several services that you can use to annotate your data, extract, transfer, and load (ETL) and prepare your data, choose an algorithm, train it, tune and optimize it for deployment, and make ETL jobs on a fully managed, scale-out Apache Spark environment to load your data to its destination. 

2. Amazon SageMaker Inference Pipeline deploys pipelines so that you can pass raw input data and through the data preparation steps. 

- Data Visualization phase: 

1. AWS provides several services that you can use to visualize and analyze data at scale. 
2. Amazon Athena is a fully managed interactive query service that you can use to query data in Amazon. 
3. Amazon Kinesis Data Analytics provides real-time analytic capabilities by analyzing streaming data. 


- Feature Engineering phase: 

1. Feature engineering is a process to select and transform variables when creating a predictive model. 
2. Feature extraction is the process of creating new features from existing features. 

3. You can run feature extraction and transformation jobs using ETL services, such as AWS Glue or Amazon. 
4. You need to remove redundant and irrelevant features (to reduce the noise in the data and reduce correlations). 


- Model Training phase: 

1. Amazon SageMaker provides several popular built-in algorithms that can be trained data. 
2. After you select the algorithm, you can start training on Amazon SageMaker with an API call.
3. Amazon SageMaker also enables automatic model tuning through hyperparameter tuning jobs.

4. Amazon SageMaker Debugger provides visibility into the ML training process by monitoring, recording. 
5. Amazon SageMaker Autopilot simplifies the ML training process by handling the data preprocessing. 
6. Closely monitor your training metrics, because model performance may degrade over time. 

- Model and Business Evaluation phase: 

1. After the model has been trained, evaluate it to determine its performance and accuracy against the business expectations for the project.
2.  Plan and execute Production Deployment (Model Deployment and Model Inference). 

3.  After a model is trained, tuned, and tested, you can deploy the model into production, and make inferences (predictions) against the model. 
4. Amazon SageMaker Neo enables ML models to be trained once and then run anywhere in the cloud and compiled model. 




- General Design Principles 
 
1. Decouple model training and evaluation from model hosting. 
2. Select resources that best align with specific phases in the data science lifecycle by separating model training, model evaluation, and model hosting resources.

3. Detect data drift over time, continuously measure the accuracy of inference after the model is in
4. Automate training and evaluation pipeline


