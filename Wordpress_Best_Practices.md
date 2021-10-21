
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





### Reference

<a href="https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/best-practices-wordpress.pdf#welcome"> Original paper </a> 
