# Amazon Connect Data Lake Best Practices

- Customer service is a crucial element of brand reputation and business success. 
- Contact centers are vital to enabling a two-way agent-customer interaction and essential to delivering a superior customer service experience. Conversely, a poor experience can lead to customer churn. 
- Organizations invest in omnichannel contact centers for a competitive edge in enhancing customer experience.
- To get the most advanced analytics beneﬁts, organizations need a robust platform and cost-eﬀective solution to run a thriving contact center. 
- Amazon Web Services (AWS) provides customers with a comprehensive set of services and a scalable platform to ensure high availability, security, and resiliency of a data lake in the cloud.
- This whitepaper outlines the best practices for architecting a contact center data lake with Amazon Connect.

- The following ﬁgure shows the architecture of a traditional on-premises contact center.
![1](https://user-images.githubusercontent.com/23625821/127283202-dc879ae4-33b2-4bdb-97a6-6a3435f90c7d.png)

- The following ﬁgure shows a strategic approach to simplifying complex traditional contact center data spans across infrastructure, licensing, and maintenance environments into Amazon Connect.
![2](https://user-images.githubusercontent.com/23625821/127283239-4a78f25a-774a-4c98-8949-254a5e27a5af.png)

- A data lake is a centralized, curated, and secured repository that stores and governs all your structured and unstructured data in its native or transformed formats for analysis.
- AWS delivers the breadth and depth of services to build a secure, scalable, comprehensive, and cost-eﬀective data lake solution.
-  You can use the AWS services to ingest, store, ﬁnd, process, and analyze data from a wide variety of sources.

## Amazon Connect
- Amazon Connect is an easy-to-use and cost-eﬀective omnichannel cloud contact center.
- You can get started with a fully managed cloud-based and artiﬁcial intelligence (AI) enabled contact center within minutes.
- With the pay-as-you-go model, you pay only when the service is in use.
- There is no infrastructure to manage or upfront costs.

- Forrester Research Consulting conducted a Total Economic Impact (TEI) study on Amazon Connect and concluded a three-year ﬁnancial impact on how Amazon Connect helps customers with signiﬁcant cost savings, increased revenue, and improved agent productivity. Key ﬁndings include:
  
  - Reduction in cloud technology costs of $4.3 million
  - Subscription cost savings of 31%
  - Agent labor savings from reduced call volume of $4.6 million
  - Increased operating income by $2.6 million with enhanced customer experience
  - Return on investment (ROI) of 241%

- Using Amazon Connect’s extensive set of published APIs, you can programmatically integrate with other AWS services and third-party systems, including customer relationship management (CRM) solutions and anti-fraud solutions. 

- The following ﬁgure shows a high-level Amazon Connect contact center architecture.
![3](https://user-images.githubusercontent.com/23625821/127284304-c4ecad5a-83f0-47a3-8000-dd8fe37ec640.png)


-  Amazon Connect provides a uniﬁed and seamless customer experience across multiple channels.
-  Along with voice and webchat, Amazon Connect integrates with Amazon Pinpoint and Amazon Simple Email Service (Amazon SES) to expand the contact center’s capability on text messages and email delivery.
-  Amazon Connect integrates with Apple Business Chat for Apple device users.

## Data lake design principles 
- How do you collect, store, and analyze high-velocity data across various data types, including structured, unstructured, and semi-structured?
- How do you store and share petabytes of data on-demand globally and cost-eﬀectively?
- How do you scale IT resources to support a high number of concurrent queries against your data and scale down automatically for cost savings?
- How do your users view, search, and run queries on multiple data repositories today?
- How do you derive future insights using historical data patterns and past scenarios?

## Customer proﬁles
- Amazon Connect Customer Proﬁles enables agents to deliver eﬃcient and personalized customer service by importing customer information from various applications into a uniﬁed customer proﬁle.
- You can ingest customer data from homegrown or third-party applications such as Salesforce, ServiceNow, Zendesk, and Marketo into your Amazon Simple Storage Service (Amazon S3) data lake using pre-built connectors. 

## Contact trace record
- It captures transactional metrics such as hold time, wait time, and agent interaction time in JavaScript Object Notation (JSON) format.
- Amazon Connect aggregates CTR data to create metrics reporting. Data retention for CTR is 24 months upon contact initiation.
- You can stream CTRs to Amazon Kinesis for extended retention and advanced analysis.
- The CTR data model describes various event types available in CTRs.

## Contact ﬂow logs
- It captures real-time events and metrics about how your customers interact with contact ﬂows.
- AWS CloudWatch creates a log group for each AWS Connect instance when you enable contact ﬂow logging and include a set logging behavior block for contact ﬂows.
- Contact ﬂow logs contain the contact ﬂow ID, the customer’s contact ID, and the block’s actions.
- Using contact ﬂow logs, you can compare customer’s interactions with diﬀerent contact ﬂow versions or trace their interactions through each contact ﬂow. 
- Contact ﬂow logs help you debug and roll back contact ﬂows to previous versions should any issues arise.

## Contact Lens output ﬁles
- Using natural language processing (NLP) and speech-to-text analytics, Contact Lens for Amazon Connect provides insights to analyze customer sentiment, identify conversations trends for product feedback, and compliance audits for standard greetings and sign-oﬀs.
- With advanced conversational search, you can perform a fast full-text search for relevant calls by sentiment scores and non-talk time to identify common utterances that result in positive or negative customer sentiment. Contact Lens automatically redacts sensitive personally identiﬁable information (PII) for data privacy.
- Contact Lens stores metadata for call transcript, sentiment analysis, non-talk time, talk speed, interruptions, and categorization labels in Amazon S3. You can create custom visualization or machine learning (ML) models using data from Contact Lens and CTR stored in S3.

## Agent events streams
- It captures and store agent activity in S3 via Amazon Kinesis Data Streams. 
- You can create dashboards for near real-time agent reporting such as agent login, agent logout, agent connects with a contact and agent status change.
- You can integrate agent event streams into workforce management (WFM) solutions for agent staﬃng management or conﬁgure alerts on speciﬁc agent activity.

## Voice and chat recordings
- Amazon Connect records a conversation only when a customer connects to an agent. When the contact disconnects, the call recordings are available in your S3 bucket, or accessible in the customer's contact trace record (CTR).
- Amazon Connect redacts, encrypts, and stores voice and chat conversations between the agent and the contact in your S3 bucket for advanced analytics.

## Third-party integration
- When using AWS Partners or other third-party solutions with Amazon Connect, you can consolidate logs and external data sources in Amazon S3.

## Data lake lifecycle

Building a data lake typically involves ﬁve stages:
 - Setting up storage
 - Moving data
 - Preparing and cataloging data
 - Conﬁguring security policies
 - Making data available for consumption



### References

<a href="https://docs.aws.amazon.com/whitepapers/latest/amazon-connect-data-lake-best-practices/amazon-connect-data-lake-best-practices.pdf#amazon-connect-data-lake-best-practices"> Original White Paper </a>

