

# ML Best Practices for Public Sector Organizations

- This whitepaper outlines some of the challenges for public sector agencies in adoption and implementation of ML. 
- And provides best practices to address thesechallenges. 
- The target audience for this whitepaper includes executive leaders and agency IT Directors.

## Challenges for public sector

- Data Ingestion and Preparation.
- Model Training and Tuning. 
- ML Operations (MLOps). 
- Governance. 

- Security & Compliance.
- Cost Optimization.
- Bias and Explainability.


## Best Practices

### Data Ingestion and Preparation
- The AWS Cloud enables public sector customers to overcome the challenge of connecting to and extracting data from both streaming and batch data, as described in the following:

  - For streaming data, Amazon Kinesis and AWS Managed Streaming for Apache Kafka (Amazon MSK) enable collection, processing, and analysis of data in real time. 
  - Amazon Kinesis provides a suite of capabilities to collect, process, and analyze real-time, streaming data. 
  - Amazon Kinesis Data Streams (KDS) is a service that enables ingestion of streaming data. 
  - Producers of data push data directly into a stream, which consists of a group of stored data units called records. 
  - The stored data is available for further processing or storage as part of the data pipeline. 
  
  - Ingestion of streaming videos can be done using Amazon Kinesis Video Streams.
  - There are a number of mechanisms available for data ingestion in batch format. 
  - With AWS Database Migration Services (AWS DMS), you can replicate and ingest existing databases while the source databases remain fully operational. 
  - The service supports multiple database sources and targets, including writing data directly to Amazon S3.

### Data Preparation
- Once the data is extracted, it needs to be transformed and loaded into a data store for feeding into an ML model. 
- It needs to be cataloged and organized so that it is available for consumption, and needs to enable data lineage for compliance with federal government guidelines. 
- AWS Cloud provides three services that provide these mechanisms.
   - AWS GLUE
   - Amazon Sagemaker data wrangler
   - Amazon EMR
   

### Model Training and Tuning
- It involves the selection of a ML model that is appropriate for the use case, followed by training and tuning of the ML model.
- One of the major challenges facing the public sector is the ability for team members to apply a consistent pattern or framework for working with multitudes of options that exist in this space.
- The AWS Cloud enables public sector customers to overcome challenges in model selection, training, and tuning as described in the following.

- You can use AWS Sagemaker built-in algorithms or your own script (script mode). 

![image](https://user-images.githubusercontent.com/23625821/135825866-e1b9c2a0-5852-47a7-ac9f-85f2f7e79077.png)


![image](https://user-images.githubusercontent.com/23625821/135813159-2c3dcf88-238f-4f04-b922-290217687b2b.png)

- Or you can use your own container (BYOC). 

![image](https://user-images.githubusercontent.com/23625821/135813365-1886b6cf-c529-41e8-a43e-976fdf2883f7.png)



### MLOps
- MLOps is the discipline of integrating ML workloads into release management, Continuous Integration / Continuous Delivery (CI/CD), and operations.
- One of the major hurdles facing government organizations is the ability to create a repeatable process for deployment that is consistent with their organizational best practices. 
- Using ML models in software development makes it difficult to achieve versioning, quality control, reliability, reproducibility, explainability, and audibility in that process.
- AWS Cloud provides a number of different options that solve these challenges, either by building an MLOps pipeline from scratch or by using managed services.
- You can use Amazon Sagemaker pipelines. 


### AWS CodePipeline and AWS Lambda
- For AWS programmers, teams that are already working with CodePipeline for deployment of other workloads, an option exists to utilize the same workflows for ML.

![image](https://user-images.githubusercontent.com/23625821/135985926-5dfdbfae-17b5-4d9d-bcc6-5f70a8cffe8f.png)


### AWS StepFunctions Data Science Software Development Kit (SDK)

- It is an open-source Python library that allows data scientists to create workflows that process and publish ML models using SageMaker and Step Functions. 
- This can be used by teams that are already comfortable using Python and AWS Step Functions.
- The SDK provides the ability to copy workflows, experiment with new options, and then put the refined workflow in production. 

- The SDK can also be used to create and visualize end-to-end data science workflows that perform tasks such as data pre-processing on AWS Glue and model training, hyperparameter tuning, and endpoint creation on Amazon SageMaker.
- Workflows can be reused in production by exporting AWS CloudFormation (infrastructure as code) templates.

### AWS MLOps Framework

![image](https://user-images.githubusercontent.com/23625821/135986339-23ac5cf0-a735-4dfa-846a-aa82aafd0c2d.png)

The solution provides a ready-made template to upload trained models (also referred to as a bring your own model), configure the orchestration of the pipeline, and monitor the pipeline's operations.























### Reference

<a href="https://d1.awsstatic.com/whitepapers/machine-learning-best-practices-for-public-sector-organizations.pdf?did=wp_card&trk=wp_card"> Original paper </a>




















