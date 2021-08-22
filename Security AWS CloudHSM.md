# Security of AWS CloudHSM Backups

- AWS CloudHSM clusters provide high availability and redundancy by distributing cryptographic operations across all hardware security modules (HSMs) in the cluster.
- Backup and restore is the mechanism by which a new HSM in a cluster is synchronized.
- This whitepaper provides details on thecryptographic mechanisms supporting backup and restore functionality, and the security mechanisms protecting the Amazon Web Services (AWS)-managed backups.
- It also provides in-depth information on how backups are protected in all three phases of the CloudHSM backup lifecycle process: Creation, Archive, and Restore.
- For the purposes of this whitepaper, it is assumed that you have a basic understanding of AWS CloudHSM and cluster architecture.
- AWS offers two options for securing cryptographic keys in the AWS Cloud: AWS Key Management Service (AWS KMS) and AWS CloudHSM.
- AWS KMS is a managed service that uses hardware security modules (HSMs) to protect the security of your encryption keys. 
- AWS CloudHSM delivers fully managed HSMs in the AWS Cloud, which allows you to add secure, validated key storage and high-performance crypto acceleration to your AWS applications.
- CloudHSM offers you the option of single-tenant access and control over your HSMs.
- CloudHSM is based on Federal Information Processing Standards (FIPS) 140-2 Level 3 validated hardware.
- CloudHSM delivers fully managed HSMs in the AWS Cloud. CloudHSM delivers all the benefits of traditional HSMs including secure generation, storage, and management of cryptographic keys used for data encryption that are controlled and accessible only by you.
- HSM capacity can be scaled quickly by adding and removing HSMs from your cluster on demand. 
- The backup and restore functionality of CloudHSM is what enables scalability, reliability, and high availability in CloudHSM. A key aspect of the backup and restore feature is a secure backup protocol that CloudHSM uses to back up your cluster. 
- This paper takes an in-depth look at the security mechanisms in place around this feature.


