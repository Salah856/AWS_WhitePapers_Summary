
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

#### Model Building 
- Once the need for a machine learning system is found, data scientists will research and experiment to develop the best model, by trying different combinations of algorithms, and tuning their parameters and hyperparameters.

#### Model Evaluation
- As the data science process is very research-oriented, it is common that there will be multiple experiments running in parallel, and many of them will never make their way to production.
- Your CD4ML architecture will need to support tracking, visualizing, comparing results from different runs, as well as to support the graduation and promotion of models that prove to be useful.

#### Productionize the Model
- There will always be an implicit contract (API) between the model and how it is consumed.

#### Testing & Quality
- While you cannot write a deterministic test to assert the model score from a given training run, the CD4ML process can automate the collection of such metrics and track their trend over time.
- This allows you to introduce quality gates that fail when they cross a configurable threshold and to ensure that models don’t degrade against known performance baselines.

#### Deployment
- Once a good candidate model is found, it must be deployed to production.
-  There are different approaches to do that with minimal disruption: 
    1. You can have multiple models performing the same task for different partitions of the problem.
    2. You can have a shadow model deployed side by side with the current one to monitor its performance before promoting it.
    3. You can have competing models being actively used by different segments of the user base.
    4. Or you can have online learning models that are continuously improving with the arrival of new data.

- Elastic cloud infrastructure is a key enabler for implementing these different deployment scenarios while minimizing any potential downtime, allowing you to scale the infrastructure up and down on-demand, as they are rolled out.

