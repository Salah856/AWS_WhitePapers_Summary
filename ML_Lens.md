
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


- Build Intelligent Applications using AWS AI Services

1. When developers use these services, they don’t have to manage the data preparation, data analysis, etc. 
2. Amazon Comprehend is a natural language processing (NLP) service that uses ML to help you uncover and parts of speech, and because the service understands how positive or negative the text is. 
3. Amazon Lex is a service for building conversational interfaces into any application using voice and text. 

4. Amazon Polly is a text-to-speech service that uses advanced deep learning technologies to synthesize speech that sounds like a human. 
5. Amazon Rekognition makes it easy to add image and video analysis to your applications. 
6. Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for you to add speech-to-text capability to your applications files stored in Amazon S3 and have the service return a text file of the transcribed speech. 

7. Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable translations. 
8. AWS Acceptable Use Policy (AUP) prohibits customers from using any AWS service, including Amazon Rekognition, to violate the law, and customers who violate our AUP will not be able to use our services.


- Reference Architecure

![1](https://user-images.githubusercontent.com/23625821/124392779-b06e8d00-dcf7-11eb-94bd-2c0c6aa0e213.png)

1. Create an Amazon S3 bucket to temporarily store images and enable encryption on the bucket. 
2. Customer images captured in the retail store are uploaded to the Amazon S3 bucket.
3. Each image uploaded to Amazon S3 triggers an AWS Lambda function, and you can use facial analysis. 

4. The demographic data is stored in .csv format in a second Amazon S3 bucket.
5. Amazon Athena reads and loads the demographic data from the .csv files for queries.
6. To make sure that confidence levels are used appropriately, use Views in Amazon In this example, the object of interest is an image and Amazon Rekognition is used to analyze the image.


- Use Managed ML Services to Build Custom ML Models

![1](https://user-images.githubusercontent.com/23625821/124393253-e14fc180-dcf9-11eb-9ec6-f5809a4673bb.png)

1. Amazon S3 is used as a data lake that holds the raw, modeled, enhanced, and transformed data.
2. Data transformation code is hosted on AWS Lambda to prepare the raw data for consumption. 
3. Data transformation code is hosted on AWS Lambda.


- Machine Learning on Edge and on Multiple Platforms

![2](https://user-images.githubusercontent.com/23625821/124393374-836fa980-dcfa-11eb-8ce1-3f162c7d015e.png)

1. Performing inference locally on connected devices running AWS IoT Greengrass reduces latency and cost.
2. Instead of sending all device data to the cloud to perform ML inference and make a prediction, you can run inference directly on the device. 
3. Data gathered from the inference running on AWS IoT Greengrass can be sent back to Amazon Sagemaker. 


- Reference Architecture 

1. a Bird Species Identification on the Edge use case is shown. 

![1](https://user-images.githubusercontent.com/23625821/124393593-71dad180-dcfb-11eb-89fa-2b96e9a420ae.png)


2. In this architecture, an object detection model is trained on Amazon SageMaker and deployed to an edge device.
3. The edge device used for this use case is AWS DeepLens, which is a deep-learning-enabled video camera.


- Gather, understand, and prepare the bird image dataset
- Train the object detection model using the Amazon SageMaker built-in algorithm
- Host the model using an Amazon SageMaker endpoint

- Deploy the model to the edge on AWS DeepLens:
  a. Convert the model artifacts before you deploy to AWS DeepLens
  b. Optimize the model from your AWS Lambda function on AWS DeepLens

- Perform model inference and bird species identification on AWS DeepLens
- If you want to deploy an ML model to a platform other than the specific platform that you trained it for, you must first optimize the model using Sagemaker Neo. 

