# CI/CD for ML

The scope of an ML practitioner's duties stops after they have created an ideal ML model, regardless of whether they used the CRISP-DM technique or an AutoML methodology. The ML practitioner simply hands the model off to the various teams in charge of managing and deploying the model in production after their role is finished.

When trying to automate the entire process, this handover causes a disconnect that makes things more difficult. More importantly, this separation frequently affects the overall delivery schedule and delays the project's effective conclusion.

Using a Continuous Integration and Continuous Delivery (CI/CD) approach, the main objective of this article is to illustrate one of the ways to close this apparent gap in model deployment and further automate the process. By demonstrating how an ML practitioner can better communicate with the application development and operations teams, I'll also introduce you to the idea of an agile, cross-functional team. By the end of the chapter, you will see how this methodology can consistently produce production-grade ML models and deploy them. We will concentrate on the following subjects in order to achieve this:
CI/CD methodology introduction; automating machine learning with CI/CD; building a CI/CD pipeline on AWS


## Introducing the CI/CD methodology

A highly well-liked mechanism for automating the creation and release of software into production is the CI/CD pattern. The basic idea behind this method is to deploy changes to production automatically and seamlessly after making incremental, dependable, and frequent modifications to the software code.
Although this discipline has been around for a while and is used by many DevOps engineers, MLOps, or Machine Learning Operations, is beginning to gain traction within the ML practitioner community. Before delving into how this methodology might be used for ML, let's become familiar with the individual parts of the procedure, beginning with CI.


![image](https://user-images.githubusercontent.com/23625821/192133212-55593a11-624e-4bfd-9853-9a38c0301e6e.png)


### Creating or updating source artifacts

