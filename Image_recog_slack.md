

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
- 


### References

<a href="https://docs.aws.amazon.com/whitepapers/latest/moderating-image-content-in-slack/moderating-image-content-in-slack.pdf#moderating-image-content-in-slack"> Original White Paper </a>
