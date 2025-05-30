# aws_bedrock_langchain_rag_poc
AWS Bedrock knowledge based on Lee Assam's course Learning Amazon Bedrock.

Here you'll find interactions with the SDKs:
- boto3
- langchain

LLMs explored in the codes:
- Amazon Titan Text Express v1
- Meta Llama3 70b Instruct v1.0

The configurations were done using **AWS Management Console**.

<br />

## AWS Bedorck Setup

### Enabling LLM (Models)

- Bedrock > Model Access
    - Manage Model Access
    - Select all Models matching to the AWS Region you'll run the project
        - (Optional) For Anthropic Claude you'll need to submit a Use Case to use it. See more at [anthropic_claude](anthropic_claude/use_case_details.txt)
    - Click on Request Model Access
    - Follow the requests checking the value on 'Access Status' column

<br />

## Choosing the Foundation Model (LLM)

- Bedrock > Foundation Models > Model Catalog
    - Choose the Category (Vendor)
    - Choose the Model (LLM)
    - Choose the Inference (On demand/Provisioned)
    - Choose the Configurations (e.g. Temperature, Top P, Response Length, etc)

- See more at [Bedrock Supported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
<br />

## Trying the Foundation Model (LLM)

- Bedrock > Playground > Chat/Text / Image/Video playground


    

