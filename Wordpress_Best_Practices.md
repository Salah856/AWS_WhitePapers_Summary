
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

Before migrating to a multi-server, scalable deployment (discussed later in this paper), there are a number of performance and cost efficiencies you can apply. 

These are good practices that you should follow anyway, even if you do move to a multi-server architecture.

The following sections introduce a number of options that can improve aspects of your WordPress website’s performance and scalability. 

Some can be applied to a single-server deployment, whereas others take advantage of the scalability of multiple servers. 

Many of those modifications require the use of one or more WordPress plugins. 

Although various options are available, W3 Total Cache is a popular choice that combines many of those modifications in a single plugin.








### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/best-practices-wordpress.pdf#welcome"> Original paper </a> 
