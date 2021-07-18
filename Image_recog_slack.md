

# #AWS_WhitePaper_Summary

- This document shows you how to use Amazon Rekognition and Amazon AppFlow to build a fully serverless content moderation pipeline for messages posted in a Slack channel. 

- The content moderation strategy identiﬁes images that violate sample chosen guidelines:
  - Images that contain themes of tobacco or alcohol.
  - Images that contain the following disallowed words:
     - medical
     - private

- Amazon Rekognition content moderation is a deep learning-based service that can detect inappropriate, or oﬀensive images & videos, making it easier to ﬁnd and remove such content at scale.
- It provides a detailed taxonomy of moderation categories. 
-  Such as Explicit Nudity, Suggestive, Violence, and Visually Disturbing.
-  You can now detect six new categories: Drugs, Tobacco, Alcohol, Gambling, Rude Gestures, and Hate Symbols.

- Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between Software-as-a-Service (SaaS) applications like Salesforce, Marketo, Slack, and ServiceNow, and AWS services like S3, Redshift, in just a few clicks.
-  This solution leverages Amazon AppFlow to capture the content posted in Slack channels for analysis using Amazon Rekognition.
- It's supposed that reader of this document has an account/workspace on AWS and Slack, also S3 bucket accessibility.
- Also, client credetials for this services will be used.  
- This solution doesn't require any prior machine learning (ML) expertise, or development of your own custom ML models.

## Architecture overview
- This solution uses serverless technologies and managed services to be scalable and cost-eﬀective.
-  By using an event-driven architecture that incorporates AWS Lambda and SQS, you can decouple image detection and image processing without provisioning or managing any servers.

![1](https://user-images.githubusercontent.com/23625821/126063940-44fdd366-c750-4643-9dd7-ccf5bfd0ca69.png)

### Create Amazon AppFlow Integration with your Slack workspace
- First you have to create a Slack app, <a href="https://api.slack.com/authentication/basics"> for more details </a> . 
- Now follow these steps to conﬁgure the Amazon AppFlow integration: 
   1. Navigate to the Amazon AppFlow console and choose Create ﬂow.
   2. In Step 1 of the creation process, enter a Flow name, and optionally, a description. 
   3. For the purposes of this demo, leave the Data  encryption setting as it is.
   4. Optionally, enter any tags you’d like for the ﬂow.
   5. Choose Next.

![2](https://user-images.githubusercontent.com/23625821/126064238-b2f9535e-6989-4941-b5e0-f2dfbe7d13eb.png)





### References

<a href="https://docs.aws.amazon.com/whitepapers/latest/moderating-image-content-in-slack/moderating-image-content-in-slack.pdf#moderating-image-content-in-slack"> Original White Paper </a>
