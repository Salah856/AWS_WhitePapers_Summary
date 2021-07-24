
# Getting started with Julia on AWS SageMaker

#aws_whitepaper_summary 

In this article we will explore how to get started combining these powerful tools and start an exciting journey using Julia as an alternative for data science and machine learning.

- This guide will walk you through the following steps:
  - Creating an Amazon SageMaker notebook instance
  - Creating a Julia environment
  - Installing IJulia and running a Julia notebook
  - Testing the Julia notebook

- This guide assumes that you have the following:
  - An AWS account with the capability to create new instances in the Amazon SageMaker console.
  - A basic understanding of machine learning or data processing.


## Setting Up Your Environment

### Creating an Amazon SageMaker Notebook Instance
1. Sign in to Amazon SageMaker console, and open the Amazon SageMaker Dashboard.
2. Select Notebook instances. Alternatively, on the left menu panel, select Notebook instances in the Notebook section.
3. Select Create notebook instance.
4. For Notebook instance name enter the name, and for the Notebook instance type select the instance type for your workload and budget.

![in](https://user-images.githubusercontent.com/23625821/126863890-5b7ff0af-0ed6-43dd-9c5d-3f36d7b91d6e.png)

5. Select Open JupyterLab, to launch a console of your notebook instance

![in](https://user-images.githubusercontent.com/23625821/126863913-57c5d043-b79b-4b58-af91-717a04d7d845.png)

### Creating a Julia Environment

