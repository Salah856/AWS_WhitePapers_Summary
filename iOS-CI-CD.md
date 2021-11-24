

# iOS CI/CD Build and Test Pipeline

Automate building and testing of iOS apps using AWS CodePipeline, Amazon EC2 Mac instance, and AWS Device Farm. 


- A developer initiates a build or test activity in AWS CodePipeline by pushing a code change to AWS CodeCommit.

- AWS CodePipeline detects the change in AWS CodeCommit and invokes AWS Step Functions to start the build process.

- An AWS Lambda function loads required build scripts from an Amazon S3 bucket and triggers an AWS Systems Manager Run command.

- 









<a href="https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/ios-cicd-build-test-pipeline-ra.pdf?did=wp_card&trk=wp_card"> Diagram </a> 






