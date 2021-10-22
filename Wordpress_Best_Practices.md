
# Best Practices for WordPress on AWS

- This whitepaper provides system administrators with specific guidance on how to get started with WordPress on AWS and how to improve both the cost efficiency of the deployment as well as the end user experience. 

- It also outlines a reference architecture that addresses common scalability and high availability requirements.
- When the first version of WordPress was released in 2003, it was not built with modern elastic and scalable cloud-based infrastructures in mind. 

- Through the work of the WordPress community and the release of various WordPress modules, the capabilities of this CMS solution are constantly expanding.
- Today, it is possible to build a WordPress architecture that takes advantage of many of the benefits of the AWS Cloud.

## Simple deployment

- For low-traffic blogs or websites without strict high availability requirements, a simple deployment of a single server might be suitable. 
- This deployment isn’t the most resilient or scalable architecture, but it is the quickest and most economical way to get your website up and running.

### Considerations

- This discussion starts with a single web server deployment. 
- There may be occasions when you outgrow it, for example:

    - The virtual machine that your WordPress website is deployed on is a single point of failure. 
    - A problem with this instance causes a loss of service for your website.
    
    - Scaling resources to improve performance can only be achieved by “vertical scaling;” 
    - That is, by increasing the size of the virtual machine running your WordPress website.



### Available approaches

- AWS has a number of different options for provisioning virtual machines. 
- There are three main ways to host your own WordPress website on AWS:

- Amazon Lightsail
- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Marketplace


#### Amazon Lightsail

Lightsail is the easiest way to get started on AWS for developers, small businesses, students, and other users who need a simple VPS solution.

The service abstracts many of the more complex elements of infrastructure management away from the user. 

It is, therefore, an ideal starting point if you have less infrastructure experience, or when you need to focus on running your website and a simplified product is sufficient for your needs.

With Amazon Lightsail, you can choose Windows or Linux/Unix operating systems and popular web
applications, including WordPress, and deploy these with a single click from preconfigured templates.

As your needs grow, you have the ability to smoothly step outside of the initial boundaries and connect to additional AWS database, object storage, caching, and content distribution services.


##### Selecting an Amazon Lightsail pricing plan

A Lightsail plan defines the monthly cost of the Lightsail resources you use to host your WordPress website. 

There are a number of plans available to cover a variety of use cases, with varying levels of CPU resource, memory, solid-state drive (SSD) storage, and data transfer. 

If your website is complex, you may need a larger instance with more resources. 

You can achieve this by migrating your server to a larger plan using the web console or as described in the Amazon Lightsail CLI documentation.






### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/best-practices-wordpress.pdf#welcome"> Original paper </a> 
