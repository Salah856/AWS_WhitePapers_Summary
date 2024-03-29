# Automating Machine Learning Model Development Using SageMaker Autopilot

AWS provides a variety of methods for automating the creation of ML models. I'll describe one such approach in this article: SageMaker Autopilot. A framework called Autopilot runs the essential phases of a typical ML workflow automatically. This basically automates the end-to-end ML process by allowing both inexperienced and seasoned ML practitioners to assign the manual chores of data discovery, algorithm selection, model training, and model optimization to a dedicated AWS service.

This post will introduce you to some of the AWS features that concentrate on machine learning (ML) solutions and ML automation.

The following topics will be covered: 
  • Introduction to the AWS AI and ML landscape.
  
  • Overview of SageMaker Autopilot.
   
  • Using SageMaker Autopilot to overcome automation problems.
  
  • Using the SageMaker SDK to automate the ML experiment.


## Introducing the AWS AI and ML landscape

AWS offers a wide range of machine learning (ML) and artificial intelligence (AI) capabilities to its clients. AWS has collected and arranged these capabilities into what is often known as the AI/ML Stack in order to further aid its clients in understanding them. The main objective of the AI/ML stack is to offer the tools that a developer or an expert in machine learning could need, depending on their level of experience. In essence, it equips all developers, whether they are regarded as novices or experts, with AI and ML skills. 

![image](https://user-images.githubusercontent.com/23625821/191805882-11ffbc89-818c-403e-b67a-8bf82a88c5d4.png)


![image](https://user-images.githubusercontent.com/23625821/191806161-3355ff90-f041-4b60-b1c6-072532d7589e.png)

## Overview of SageMaker Autopilot

The AWS service that offers AutoML capability to its users is called SageMaker Autopilot. The following SageMaker modules are pieced together by Autopilot into an automated framework to address the various AutoML requirements:

• SageMaker Processing: Using a streamlined and controlled experience, processing jobs handle the labor-intensive tasks and scalability requirements of organising, validating, and feature engineering the data.

• SageMaker Built-in Algorithms: SageMaker offers a number of pre-built algorithms that are suited to a variety of use case types, making it easier for ML practitioners to get started with model-building activities.

• SageMaker Training: Training jobs handle the labor-intensive scaling and provisioning operations related to setting up the necessary compute resources to train the model.

• Automatic Model Tuning: By enabling the ML practitioner to run numerous training jobs concurrently, each with a subset of the necessary parameters, model tuning or hyperparameter tuning scales the model tuning task. As a result, there is no longer a need to adjust, assess, and retrain the model in a sequential manner. In order to choose future hyperparameters that will better optimise the model, SageMaker model tuning by default creates a probabilistic model of the performance of previously used hyperparameters using Bayesian Search (although Random Search can also be used).

• SageMaker Managed Deployment: After an optimal model has been trained, SageMaker Hosting can be used to deploy a single model or a collection of models as a fully functional API for use by production applications in an elastic and scalable way.


These tools are connected by Autopilot to form an automated workflow. The raw data is the only component that the ML practitioner is required to provide. By just providing the data, Autopilot enables even a beginner in machine learning to automatically develop a model that is suitable for production.


## Overcoming automation challenges with SageMaker Autopilot

• The difficulties associated with creating the optimal ML model, such as gathering and comprehending the data before creating the model that is most appropriate for the use case.
• The difficulties brought on by the ML process itself, which is difficult, laborious, iterative, and continual.


For experimenting Sagemaker Autopilot, you can refer to this <a href="https://aws.amazon.com/getting-started/hands-on/create-machine-learning-model-automatically-sagemaker-autopilot/#"> tutorial </a>

## SageMaker SDK Using for automating the ML experiment

The SageMaker SDK is essentially a higher-level SDK with an emphasis on ML exploration that utilises the base boto3 SDK. For instance, a machine learning practitioner would need to execute three different boto3 calls to deploy a model as a SageMaker hosted endpoint:
1. The machine learning practitioner must use the SageMaker training job's output artefact to instantiate a trained model. This is done by using the boto3.client("sagemaker") low-level SageMaker client's create model() method.
2. After that, the ML expert must construct a SageMaker hosted endpoint configuration that details the endpoint's extra configuration options as well as the underlying computer resources. The SageMaker client's create endpoint config() method is used for this.
3. The trained model is deployed with the endpoint settings using the create endpoint() method.


As an alternative, the ML practitioner might achieve the same result by executing the deploy() method on a model that has already been trained using the SageMaker SDK. The underlying model, endpoint setup, and endpoint deployment are all created by the SageMaker SDK.
The SageMaker SDK greatly simplifies ML experimentation for the more seasoned ML practitioner. You will begin getting acquainted with the SageMaker SDK in the following part by working through an example to codify the AutoML experiment.

You can refere this <a href="https://sagemaker-examples.readthedocs.io/en/latest/autopilot/index.html"> link </a> to implement your models using Sagemaker Autopilot and codify your Autopilot experiments. 




