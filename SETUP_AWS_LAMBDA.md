# AWS Lambda

Here are the steps to create the AWS Lambda that'll be used in the cloud provider to interact with the AWS Bedrock Agent.

The configurations were done using **AWS Management Console**.

## Lambda Setup

- Lambda > Create function
    - Fill the form
        - Choose the function name
        - Choose the Runtime: Python 3.13
    - Click on Create function

### File to upload the core code inside the Lambda function

- [lambda_core.py](aws_lambda/lambda_core.py)

### Provide AWS Bedrock Agent invocation grant

- Lambda > Choose your Lambda funtion name
    - Configuration tab
        - Resource-based policy statements
            - Click on Add permissions button
                - Choose AWS service
                - Service
                    - Choose Other
                - Statement ID
                    - Provide an unique ID
                - Principal
                    - bedrock.amazonaws.com
                - Source ARN
                    - Paste the AWS Bedrock Agent ARN you created in [README.md](README.md)
                - Action
                    - lambda:InvokeFuntion
                - Click on Save button
                