# Infrastructure as code

- Infrastructure as Code has emerged as a best practice for automating the provisioning of infrastructure services. 
- This paper describes the benefits of Infrastructure as Code.
- And how to leverage the capabilities of AWS in this realm to support DevOps initiatives.


## Introduction to Infrastructure as Code

- Infrastructure management is a process associated with software engineering.
- Organizations have traditionally “racked and stacked” hardware, and then installed and configured operating systems and applications to support their technology needs. 
- Cloud computing takes advantage of virtualization to enable the on-demand provisioning of compute, network, and storage resources that constitute technology infrastructures.

- Infrastructure managers have often performed such provisioning manually. 
- The manual processes have certain disadvantages, including:
    
     - Higher cost because they require human capital that could otherwise go toward more important business needs.
     - Inconsistency due to human error, leading to deviations from configuration standards.
    
     - Lack of agility by limiting the speed at which your organization can release new versions of services in response to customer needs and market drivers.
     - Difficulty in attaining and maintaining compliance to corporate or industry standards due to the absence of repeatable processes.


## The Infrastructure Resource Lifecycle

![image](https://user-images.githubusercontent.com/23625821/133917214-9c20040a-f476-4857-8aa8-2ca9fec2e7f9.png)

1. Resource provisioning. Administrators provision the resources according to the specifications they want.
2. Configuration management. The resources become components of a configuration management system that supports activities such as tuning and patching.

3. Monitoring and performance. Monitoring and performance tools validate the operational status of the resources by examining items such as metrics, synthetic transactions, and log files.
4. Compliance and governance. Compliance and governance frameworks drive additional validation to ensure alignment with corporate and industry standards, as well as regulatory requirements.

5. Resource optimization. Administrators review performance data and identify changes needed to optimize the environment around criteria such as performance and cost management.

### AWS CloudFormation
AWS CloudFormation gives developers and systems administrators an easy way to create, manage, provision, and update a collection of related AWS resources in an orderly and predictable way. AWS CloudFormation uses templates written in JSON or YAML format to describe the collection of AWS resources (known as a stack), their associated dependencies, and any required runtime parameters. You can use a template repeatedly to create identical copies of the same stack consistently across AWS Regions.

#### Template anatomy

```yaml
---
AWSTemplateFormatVersion: "version date"
    Description:
        String
    Parameters:
        set of parameters
    Mappings:
        set of mappings
    Conditions:
        set of conditions
    Transform:
        set of transforms
    Resources:
        set of resources
    Outputs:
        set of outputs

```


![1](https://user-images.githubusercontent.com/23625821/134113464-e3422ed2-8465-4787-b857-c3459c37000f.png)
































### References:

<a href="https://d0.awsstatic.com/whitepapers/DevOps/infrastructure-as-code.pdf"> Original paper </a>


