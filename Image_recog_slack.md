

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
   
   6. In Step 2 (Conﬁgure ﬂow), choose the Source name dropdown list and choose Slack from the list of options:

  ![3](https://user-images.githubusercontent.com/23625821/126064279-d5b32388-de1a-4216-b1c2-27d485cfaf3f.png) 
   7. A Choose Slack connection dropdown list appears. From this list, choose Create new connection:
   ![4](https://user-images.githubusercontent.com/23625821/126064307-fdc5e466-2301-4358-89c1-9a69d651ec10.png)
   
   8.  Enter your Slack workspace address (for example, testingslackdevgroup.slack.com), and Client ID and Client Secret generated when created the Slack App.
   9.  Give your connection a name on the Connect to Slack popup window.
   10. Choose Continue.
   
   ![5](https://user-images.githubusercontent.com/23625821/126064352-d3841ee3-5111-485a-bf60-40e9a4785111.png)
   
   11. A window pops up with a conﬁrmation prompt to allow permissions. Choose Allow.
   12. Your new connection is conﬁgured & displayed in the Choose Slack connection dropdown list, and a new Choose Slack object dropdown list appears directly below it. Choose Conversations.
   13. A new dropdown appears directly below Choose Slack channel. From this list, choose the Slack channel that you would like to perform content moderation on.
   
   ![6](https://user-images.githubusercontent.com/23625821/126064515-dfbdbdcf-4ae2-4925-93ad-f48d08e7bb4d.png)
   
   14. With the Slack workspace connected, and the channel for moderation selected, you can move on to conﬁguring the Destination details. First, choose Amazon S3 from the Destination name dropdown list. Select S3. 
    
  ![7](https://user-images.githubusercontent.com/23625821/126064535-32d96be2-af4f-46b7-85f4-79dd2e178748.png)
  15. A new section titled Flow trigger appears with two options: Run on demand or Run ﬂow on schedule. Choose the second option, and conﬁgure the schedule to run every one (1) minute.
  16. When you choose this option, the Incremental Transfer option is auto-selected. Enter a value for Starting at and Start date.
  17. In Step 3 (Map data ﬁelds), you have the option to perform transformations on the data ﬁelds. Choose Manually map ﬁelds.
  18. From the Source ﬁeld name dropdown, select Map all ﬁelds directly. This creates a mapping of all the ﬁelds without any transformations.
  19. Choose Next.
  20. In Step 4 (Add ﬁlters), you have the option to perform ﬁltering on the data. Do not add any ﬁlters here, simply choose Next to continue.
  21. On the Review and Create screen, a summary of all your selections from previous steps is shown. Review these for accuracy, then scroll to the bottom of page and choose Create ﬂow.
  22.After the ﬂow has been created, on the following screen, choose the Activate ﬂow button.
 

### Create a Lambda function to process ﬁles in the S3 bucket that contain new Slack messages
- Because the Lambda function needs to store the image URLs it ﬁnds into a new SQS queue, ﬁrst create that queue by following the steps outlined in <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html"> Getting started with Amazon SQS </a> . Name this queue new-image-findings.
- 


   




### References

<a href="https://docs.aws.amazon.com/whitepapers/latest/moderating-image-content-in-slack/moderating-image-content-in-slack.pdf#moderating-image-content-in-slack"> Original White Paper </a>
