# AWS S3

Here are the steps to create the AWS S3 Bucket that'll be used in the cloud provider to store the data content for AWS Bedrock Knowledge Base (KB).

The configurations were done using **AWS Management Console**.

## S3 Bucket Setup

- S3 > Create Bucket
    - Fill the form
        - Choose the AWS Region
        - Choose Bucket name
    - Click on Create Bucket

### File to upload inside the S3 Bucket to use as a KB content

- [Employee-Handbook.pdf](aws_bedrock/Employee-Handbook.pdf)

### File to upload inside the S3 Bucket to use as OpenAPI documentation with the Lambda Function

- [pto_api.yml](aws_lambda/pto_api.yml)