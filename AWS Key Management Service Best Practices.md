
# AWS Key Management Service Best Practices


AWS Key Management Service (AWS KMS) is a managed service that allows you to concentrate on the cryptographic needs of your applications while Amazon Web Services (AWS) manages availability, physical security, logical access control, and maintenance of the underlying infrastructure. 

Further, AWS KMS allows you to audit usage of your keys by providing logs of all API calls made on them to help you meet compliance and regulatory requirements.

Customers want to know how to effectively implement AWS KMS in their environment. 

This whitepaper discusses how to use AWS KMS for each capability described in the AWS Cloud Adoption Framework Security Perspective whitepaper, including the differences between the different types of customer master keys, using AWS KMS key policies to ensure least privilege, auditing the use of the keys, and listing some use cases that work to protect sensitive information within AWS.


### Identity and Access Management

The Identity and Access Management capability provides guidance on determining the controls for access management within AWS KMS to secure your infrastructure according to established best practices and internal policies.


#### AWS KMS and IAM Policies

You can use AWS Identity and Access Management (IAM) policies in combination with key policies to control access to your customer master keys (CMKs) in AWS KMS. 

This section discusses using IAM in the context of AWS KMS.  It doesn’t provide detailed information about the IAM service. 


Policies attached to IAM identities (that is, users, groups, and roles) are called identity-based policies (or IAM policies). 

Policies attached to resources outside of IAM are called resource-based policies. 

In AWS KMS, you must attach resource-based policies to your customer master keys (CMKs). 

These are called key policies. All KMS CMKs have a key policy, and you must use it to control access to a CMK. 

IAM policies by themselves are not sufficient to allow access to a CMK, although you can use them in combination with a CMK key policy. 

To do so, ensure that the CMK key policy includes the policy statement that enables IAM policies.


#### Key Policies

Key policies are the primary way to control access to CMKs in AWS KMS. Each CMK has a key policy attached to it that defines permissions on the use and management of the key. 

The default policy enables any principals you define, as well as enables the root user in the account to add IAM policies that reference the key. 

We recommend that you edit the default CMK policy to align with your organization’s best practices for least privilege. 

To access an encrypted resource, the principal needs to have permissions to use the resource, as well as to use the encryption key that protects the resource. 

If the principal does not have the necessary permissions for either of those actions, the request to use the encrypted resource will be denied.

#### Least Privilege / Separation of Duties







#### Reference 

<a href="https://docs.aws.amazon.com/whitepapers/latest/kms-best-practices/kms-best-practices.pdf#welcome"> Original paper </a> 

