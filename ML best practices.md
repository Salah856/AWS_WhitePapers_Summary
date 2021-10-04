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

![image](https://user-images.githubusercontent.com/23625821/135813159-2c3dcf88-238f-4f04-b922-290217687b2b.png)






### Reference

<a href="https://d1.awsstatic.com/whitepapers/machine-learning-best-practices-for-public-sector-organizations.pdf?did=wp_card&trk=wp_card"> Original paper </a>




















