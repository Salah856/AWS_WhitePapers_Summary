
# MLOps: Operationalizing ML on AWS 

- In modern software development, continuous delivery (CD) principles have significantly improved the throughput of delivering software to production in a safe, continuous, and reliable way and helped to avoid big, disruptive, and error prone deployments. 

- Creating a process to operationalize ML systems enables organizations to leverage the new and endless opportunities of machine learning to optimize processes and products. 
- Using ML models in software development makes it difficult to achieve versioning, quality control, reliability, reproducibility, explainability, and audibility in that process.
- This happens because there are a higher number of: 
   1. changing artifacts to be managed. 
   2. In addition to the software code, such as the datasets, the machine learning models, and the parameters and hyperparameters used by such models.
   3. And the size and portability of such artifacts can be orders of magnitude higher than the software code.
  
- There are also organizational challenges.
   1. Different teams might own different parts of the process and have their own ways of working.
   2. Data engineers might be building pipelines to make data accessible, while data scientists can be researching and exploring better models.
   3. Machine learning engineers or developers then have to worry about how to integrate that model and release it to production.
   4. When these groups work in separate siloes, there is a high risk of creating friction in the process and delivering suboptimal results.


## Continuous Delivery for Machine Learning (CD4ML) 
- CD4ML is a software engineering approach in which a cross-functional team produces machine learning applications based on code, data, and models in small and safe increments that can be reproduced and reliably released at any time, in short adaptation cycles. 
- it requires a feedback loop: The real- world data is continuously changing and the models in productions are continuously monitored, leading to adaptations and improvements by re-training of the models and the re-iteration of the whole process. 

### CD4ML Process Steps

![1](https://user-images.githubusercontent.com/23625821/125156449-bb954300-e165-11eb-947c-e9bce2502e84.png)


