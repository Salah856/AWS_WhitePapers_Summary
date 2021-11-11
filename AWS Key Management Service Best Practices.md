
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

Key policies specify a resource, action, effect, principal, and conditions to grant access to CMKs. 

Key policies allow you to push more granular permissions to CMKs to enforce least privilege. 

For example, an application might make a KMS API call to encrypt data but there is no use case for that same application to decrypt data. 

In that use case, a key policy could grant access to the kms:Encrypt action but not kms:Decrypt and reduce the possibility for exposure. 

Additionally, AWS allows you to separate the usage permissions from administration permissions associated with the key. 

This means that an individual may have the ability to manipulate the key policy, but might not have the necessary permissions to use the key for cryptographic functions.

### Cross Account Sharing of Keys

Delegation of permissions to a CMK within AWS KMS can occur when you include the root principal of a trusted account within the CMK key policy. 

The trusted account then has the ability to further delegate these permissions to IAM users and roles within their own account using IAM policies. 

While this approach may simplify the management of the key policy, it also relies on the trusted accounts to ensure that the delegated permissions are managed. 

The other approach would be to explicitly manage permissions to all authorized users using only the KMS key policy, which could make the key policy complex and less manageable. 

Regardless of the approach you take, the specific trust should be broken out on a per key basis to ensure that you adhere to the least privilege model.



### CMK Grants

Key policy changes follow the same permissions model used for policy editing elsewhere in AWS. 

That is, users either have permission to change the key policy or they do not. 

Users with the PutKeyPolicy permission for a CMK can completely replace the key policy for a CMK with a different key policy of their choice. 

You can use key policies to allow other principals to access a CMK, but key policies work best for relatively static assignments of permissions. 

To enable more granular permissions management, you can use grants. 

Grants are useful when you want to define scoped-down, temporary permissions to use your CMK on your behalf in the absence of a direct API call from you.

### Encryption Context

In addition to limiting permission to the AWS KMS APIs, AWS KMS also gives you the ability to add an additional layer of authentication for your KMS API calls utilizing encryption context. 

The encryption context is a key-value pair of additional data that you want associated with AWS KMS-protected information. 

This is then incorporated into the additional authenticated data (AAD) of the authenticated encryption in AWS KMS-encrypted ciphertexts. 

If you submit the encryption context value in the encryption operation, you are required to pass it in the corresponding decryption operation. 

You can use the encryption context inside your policies to enforce tighter controls for your encrypted resources.

Because the encryption context is logged in CloudTrail, you can get more insight into the usage of your keys from an audit perspective. 

Be aware that the encryption context is not encrypted and will be visible within CloudTrail logs. 

The encryption context should not be considered sensitive information and should not require secrecy.





#### Reference 

<a href="https://docs.aws.amazon.com/whitepapers/latest/kms-best-practices/kms-best-practices.pdf#welcome"> Original paper </a> 





