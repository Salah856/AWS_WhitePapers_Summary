# Serverless Architecture for Product Defect Detection Using Computer Vision

## Detect product defects, get real-time notifications, and visualize insights using AWS AI/ML, and serverless services


Architecture for camera-based in-line or end-of-line quality inspection. Supports automated or one-time anomaly detection using image classification in the cloud; real-time monitoring and notifications; and analytics and insights from the classification results.


- Upload training data to Amazon Lookout For Vision or import training data from Amazon Simple Storage Service (Amazon S3) and train a model.

- Admin users signup and login to a management front end website.

- Start or stop the model or do one-time defect detection by uploading an image.

- Camera or a client application invokes an Amazon API Gateway endpoint to get a signed URL from Amazon S3. The request is authorized by an AWS Lambda function and a signed URL is returned.

- Using the signed URL, an image, along with its associated metadata, is uploaded to Amazon S3.

- Image upload to the S3 bucket triggers an event notification to initiate an AWS Step Functions workflow.

- Fetch image from the S3 bucket and present to Amazon Lookout For Vision for anomaly detection using DetectAnomalies API.

- Store inference result and image metadata in Amazon DynamoDB.

- Publish a notification to an Amazon Simple Notification Service (Amazon SNS) topic to send an email alert to subscribed operators and plant managers in case a defect or a low-confidence result is detected.

- Inference results are fetched from DynamoDB Streams, transformed and enriched, sent to Amazon Kinesis Data Firehose for batching, and saved in another S3 bucket.

- Inference results datasets are imported into Amazon Quicksight.

- Create dashboards and analyses for business users, and gain insights from the inference results.

- Amazon CloudWatch provides a single pane of glass to operators and plant managers for workload and defect detection monitoring using logs, alarms, and dashboards.

- Alarm notifications from Amazon CloudWatch are sent to operators and plant managers by Amazon SNS whenever defects exceed a pre-defined threshold


















<a href="https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/serverless-architecture-for-product-defect-detection-using-computer-vision-ra.pdf?did=wp_card&trk=wp_card"> Ref </a>
