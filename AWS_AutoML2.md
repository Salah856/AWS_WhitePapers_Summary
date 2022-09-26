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

Other than initiating the full CI process, the source artefacts stage doesn't really do any particular tasks. In essence, this step acts as a repository for the source code or software components that make up the finished application. The pipeline begins when new software artefacts (such as new features) or updated software artefacts (such as bug patches) are added to this repository.

For instance, application developers contribute updates to the shared version control system (such as GitHub, Bitbucket, or AWS CodeCommit) when they modify the code, add new features, or correct application defects. These stored changes are called commits, with\seach commit having an associated description or message that describes why a particular\schange was done. To help other contributors understand what has been changed in the code and why, these commits summarise the history of all the modifications. A Pull Request can be opened by the developer after a commit has been made (PR).

### Construction of pipeline assets

The various software artefacts (and their dependencies) are produced or compiled in the next stage of the pipeline. These assets, or assets that are specific to the current release or, to put it another way, assets that are specific to the current execution of the pipeline, are essentially the end product of building the source code artefacts into an asset that is specific to the current release. For instance, the build step can be used to create a Docker container image or to convert C++ code into a release binary.

### Testing the pipeline assets

After the pipeline assets are constructed, the following stage of the pipeline involves testing them for functionality as well as integration into the larger design or application. At this level, developers use automated testing, testing scripts, or even a testing architecture (also known as a test environment or QA environment) to carry out system testing.
This step's main objective is to ensure that built assets will work properly after being put into production. Application developers can ensure that the overall integrity of the solution, in its entirety, is preserved once it is released into production by testing the complete system.

### Approving the release

The final step of the CI phase is to authorise the system or application for production once the integrity of the entire system or application has been tested. This step of the procedure can either include a human (or team) approving the test results, or it can be automated in cases when there are lots of code changes.


## Creating a CI/CD pipeline on AWS

AWS offers a comprehensive collection of developer tools to meet the varied needs for hosting code as well as creating and delivering pipeline assets. We will leverage three key services from the AWS developer toolchain to build a CI/CD pipeline on AWS. We will use two additional services from the AWS development package to make the construction and automation of the pipeline even easier.

The following are the three essential elements of a CI/CD pipeline:
  • An element for keeping track of the numerous pipeline artefacts.
  
  • A step in the construction of the various pipeline assets.
  
  • A pipeline execution automation component.

AWS offers specialised services to meet the necessary capabilities of each of these three key components, particularly the following:

• <a href="https://aws.amazon.com/codecommit/"> AWS CodeCommit </a>

• AWS CodeBuild

• AWS CodePipeline


- AWS CodeCommit is a cloud-based source code and version control service. In essence, it is the AWS-managed alternative to GitHub. CodeCommit used to store all the various pipeline and ML model artifacts.


