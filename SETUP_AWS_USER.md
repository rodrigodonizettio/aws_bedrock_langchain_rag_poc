# AWS IAM

Here are the steps to create the AWS IAM User that'll be used in the cloud provider.

The configurations were done using **AWS Management Console**.

## IAM User Setup

- IAM > Users > Create User
    - Choose User name
    - Create a Group
        - Choose Usergroup name
        - Choose the Policy 'AmazonBedrockFullAccess'
            - Click on Attach policies
        - Choose the Policy 'AmazonKendraFullAccess'
            - Click on Attach policies
        - Click on Create Usergroup
    - Select the Usergroup you've just created
    - Next > Create User

<br />

## Generate & Retrieve IAM User Credentials

- IAM > Users > Select the User you've just created
    - Select 'Security Credentials' tab
        - Click on Create Access Key
            - Other > Next > Create Access Key > Download .csv file (it'll contain the AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY. Keep it safe)
- (Recommended) Store the credentials in AWS Secrets Manager 

