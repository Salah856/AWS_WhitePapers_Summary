
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

#### nstalling WordPress

Lightsail provides templates for commonly used applications such as WordPress. 

This template is a great starting point for running your own WordPress website as it comes pre-installed with most of the software you need. 

You can install additional software or customize the software configuration by using the in-browser terminal or your own SSH client, or via the WordPress administration web interface.

Amazon Lightsail has a partnership with GoDaddy Pro Sites product to help WordPress customers easily manage their instances for free. 

Lightsail WordPress virtual servers are preconfigured and optimized for fast performance and security, making it easy to get your WordPress site up and running in no time.

Customers running multiple WordPress instances find it challenging and time-consuming to update, maintain and manage all of their sites. 

With this integration, you can easily manage your multiple WordPress instances in minutes with only a few clicks. 

For more information about managing WordPress on Lightsail, refer to Getting started using WordPress from your Amazon Lightsail instance. 

Once you are finished customizing your WordPress website, we recommend taking a snapshot of your instance. 

A snapshot is a way to create a backup image of your Lightsail instance. 

It is a copy of the system disk and also stores the original machine configuration (that is, memory, CPU, disk size, and data transfer rate). 

Snapshots can be used to revert to a known good configuration after a bad deployment or upgrade. 

This snapshot allows you to recover your server if needed, but also to launch new instances with the same customizations.


### Recovering from failure

A single web server is a single point of failure, so you must ensure that your website data is backed up.

The snapshot mechanism described earlier can also be used for this purpose. 

To recover from failure, you can restore a new instance from your most recent snapshot. 

To reduce the amount of data that could be lost during a restore, your snapshots must be as recent as possible.

To minimize the potential for data loss, ensure that snapshots are being taken on a regular basis. 

You can schedule automatic snapshots of your Lightsail Linux/Unix instances. 

For steps, refer to Enabling or disabling automatic snapshots for instances or disks in Amazon Lightsail.

AWS recommends that you use a static IP: a fixed, public IP address that is dedicated to your Lightsail account. 

If you need to replace your instance with another one, you can reassign the static IP to the new instance. 

In this way, you don’t have to reconfigure any external systems (such as DNS records) to point to a new IP address every time you want to replace your instance.


### Improving performance and cost efficiency

You may eventually outgrow your single-server deployment. 

In this case, you may need to consider options for improving your website’s performance. 

Before migrating to a multi-server, scalable deployment , there are a number of performance and cost efficiencies you can apply. 

These are good practices that you should follow anyway, even if you do move to a multi-server architecture.

The following sections introduce a number of options that can improve aspects of your WordPress website’s performance and scalability. 

Some can be applied to a single-server deployment, whereas others take advantage of the scalability of multiple servers. 

Many of those modifications require the use of one or more WordPress plugins. 

Although various options are available, W3 Total Cache is a popular choice that combines many of those modifications in a single plugin.


#### Accelerating content delivery

- Any WordPress website needs to deliver a mix of static and dynamic content. Static content includes images, JavaScript files, or style sheets. Dynamic content includes anything generated on the server side using the WordPress PHP code, for example, elements of your site that are generated from the database or personalized to each viewer.

An important aspect of the end-user experience is the network latency involved when delivering the previous content to users around the world. Accelerating the delivery of the previous content improves the end-user experience, especially users geographically spread across the globe. This can be achieved with a Content Delivery Network (CDN) such as Amazon CloudFront.

Amazon CloudFront is a web service that provides an easy and cost-effective way to distribute content with low latency and high data transfer speeds through multiple edge locations across the globe. Viewer requests are automatically routed to a suitable CloudFront edge location to lower the latency. 

If the content can be cached (for a few seconds, minutes, or even days) and is already stored in a particular edge location, CloudFront delivers it immediately. If the content should not be cached, has expired, or isn’t currently in that edge location, CloudFront retrieves content from one or more sources of truth, referred to as the origin(s) (in this case, the Lightsail instance) in the CloudFront configuration. 

This retrieval takes place over optimized network connections, which work to speed up the delivery of content on your website. Apart from improving the end-user experience, the model discussed also reduces the load on your origin servers and has the potential to create significant cost savings.

#### Static content offload

This includes CSS, JavaScript, and image files – either those that are part of your WordPress themes or those media files uploaded by the content administrators. 

All these files can be stored in Amazon Simple Storage Service (Amazon S3) using a plugin such as W3 Total Cache and served to users in a scalable and highly available manner. 

Amazon S3 offers a highly scalable, reliable, and low-latency data storage infrastructure at low cost, which is accessible via REST APIs. 

Amazon S3 redundantly stores your objects, not only on multiple devices, but also across multiple facilities in an AWS Region, thus providing exceptionally high levels of durability.

This has the positive side effect of offloading this workload from your Lightsail instance and letting it focus on dynamic content generation. 

This reduces the load on the server and is an important step towards creating a stateless architecture (a prerequisite before implementing automatic scaling).

You can subsequently configure Amazon S3 as an origin for CloudFront to improve delivery of those
static assets to users around the world. 

Although WordPress isn’t integrated with Amazon S3 and CloudFront out-of-the-box, a variety of plugins add support for these services (for example, W3 Total Cache)


#### Dynamic content

Dynamic content includes the output of server-side WordPress PHP scripts. Dynamic content can also be served via CloudFront by configuring the WordPress website as an origin. 

Since dynamic content includes personalized content, you need to configure CloudFront to forward certain HTTP cookies and HTTP headers as part of a request to your custom origin server.

CloudFront uses the forwarded cookie values as part of the key that identifies a unique object in its cache. 

To ensure that you maximize the caching efficiency, you should configure CloudFront to only forward those HTTP cookies and HTTP headers that really vary the content (not cookies that are only used on the client side or by third-party applications, for example, for web analytics).


![2](https://user-images.githubusercontent.com/23625821/138556834-6619ab4a-6b64-4907-a3b6-c0aca8f27eca.png)



### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/best-practices-wordpress.pdf#welcome"> Original paper </a> 
