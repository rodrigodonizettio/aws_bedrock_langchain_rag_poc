# aws_bedrock_langchain_rag_poc
AWS Bedrock knowledge based on Lee Assam's courses:
- Learning Amazon Bedrock
- Building Applications using Amazon Bedrock

At the file [**bedrock_rag_streamlit_chat_bot.py**](aws_bedrock/bedrock_rag_streamlit_chat_bot.py) we build a Chat Bot application where we apply the Retrieval-Augmented Generation (RAG) concept:

![Final Chat Bot Project Result](aws_bedrock/bedrock_rag_streamlit_chat_bot.png)

Following the code inside **aws_bedrock** folder you'll be able to learn AI concepts using the tools:
- Bedrock
    - Foundation Models (LLMs)
    - Knowledge Base (KB)
    - Agent
        - Prompt Instructions
        - KB Instructions
        - Action Group Instructions (OpenAPI Schema)

- LangChain
    - LLM Embedding for VectorDB
    - LLM and Prompt for Chat interaction
    - Chain for Query LLM interaction
    - Chat Message History for Memory context

- AWS Kendra (VectorDB/Vector Store)

- Facebook FAISS (Facebook AI Similarity Search) for VectorDB clustering and similarity search tasks

- AWS IAM

- AWS S3

- PyPDF for PDF files management

- StreamLit for Chat Web App

<br />

LLMs explored in the codes:
- Amazon Titan Embed Text-v1
- Amazon Titan Text Express v1
- Meta Llama3 70b Instruct v1.0

<br />

## Projects Dependencies

Some Python modules must be installed for proper code working: ```pip install -r aws_bedrock/requirements.txt```

<br />

## AWS Bedrock Setup

The AWS Bedrock configurations for this course were done using **AWS Management Console**.
You can see below how to do that.

Here are the steps to enable the AWS Bedrock Foundation Models (LLMs) that'll be used in the cloud provider.
For this you're going to need an IAM User.
To check how the AWS IAM User was created see the [SETUP_AWS_USER.md](SETUP_AWS_USER.md) file.

### Enabling LLM (Models)

- Bedrock > Model Access
    - Manage Model Access
    - Select all Models matching to the AWS Region you'll run the project
        - (Optional) For Anthropic Claude you'll need to submit a Use Case to use it. See more at [anthropic_claude](anthropic_claude/use_case_details.txt)
    - Click on Request Model Access
    - Follow the requests checking the value on 'Access Status' column

<br />

### Choosing the Foundation Model (LLM)

- Bedrock > Foundation Models > Model Catalog
    - Choose the Category (Vendor)
    - Choose the Model (LLM)
    - Choose the Inference (On demand/Provisioned)
    - Choose the Configurations (e.g. Temperature, Top P, Response Length, etc)

- See more at [Bedrock Supported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)

<br />

### Trying the Foundation Model (LLM)

- Bedrock > Playground > Chat/Text / Image/Video playground

<br />

### Knowledge Base (KB)

Here are the steps to create the AWS Bedrock Knowledge Base (KB) that'll be used in the cloud provider to integrate with the S3 Bucket that stores our content data.
To check how the AWS S3 Bucket was created see the [SETUP_AWS_S3_BUCKET.md](SETUP_AWS_S3_BUCKET.md) file.

The configurations were done using **AWS Management Console**.

- Bedrock > Builder tools > Knowledge Bases
    - Create > Knowledge Base with vector store
    - Provide Knowledge Base details
        - Choose the Knowledge Base Name
        - IAM permissions
            - Create and use a new service role
            - Choose the Service Role Name
        - Choose data source
            - Amazon S3
        - Click on Next button
    - Configure data source
        - Data source name
            - Choose the Data Source Knowledge Base Name
        - S3 source
            - Paste the S3 URI where you stored your content data
        - Chunking strategy
            - Choose Semantic chunking
        - Click on Next button
    - Configure data storage and processing
        - Embeddings model
            - Titan Text Embedding V2
        - Vector store
            - Vector store creation method
                - Quick create a new vector store
            - Vector store type
                - Amazon OpenSearch Serverless
        - Click on Next button
    - Review and Create
        - Click on Create knowledge base button
    - Sync the Data Source
        - Wait until the Data source is created
        - Check the Knowledge Base in Bedrock > Builder tools > Knowledge Bases
        - Click on Sync button 

<br />

### Agent

Here are the steps to create the AWS Bedrock Agent that'll be used in the cloud provider to integrate with the Lambda that interacts with our PTO (Paid Time Off) API.
To check how the AWS Lambda was created see the [SETUP_AWS_LAMBDA.md](SETUP_AWS_LAMBDA.md) file.

The configurations were done using **AWS Management Console**.

- Bedrock > Builder tools > Agents > Create agent
    - Choose a name
    - Click on Create button
    - Click on your Agent name link
    - Click on Edit in Agent Builder
        - Agent resource role
            - Click on create and use a new service role
        - Select model
            - Click on Select model button and choose the desired LLM
        - Instructions for the Agent
            - Fill with the content inside [agent_instructions.txt](aws_bedrock/agent_instructions.txt)
        - Addtitional settings
            - User input
                - Enabled
        - Click on Save and exit button to create the IAM Role

    - Click on your Agent name link
    - Click on Edit in Agent Builder
        - Action groups
            - Click on Add button
            - Choose the Action group name
            - Action group type
                - Choose Define with API Schemas
            - Action group invocation
                - Choose Select an existing Lambda function
                - Select Lambda function
                    - Choose the Lambda name you created during the [SETUP_AWS_LAMBDA.md](SETUP_AWS_LAMBDA.md)
            - Action group schema
                - S3 Url
                    - Click on Browse S3 and choose the [pto_api.yml](aws_lambda/pto_api.yml) file you created during the [SETUP_AWS_S3_BUCKET.md](SETUP_AWS_S3_BUCKET.md)
            - Click on Create button
        - Knowledge Bases
            - Click on Add button
            - Select the KB you created in the [Knowledge Base (KB)](#knowledge-base-(kb)) section of this file
            - Knowledge Base instructions for Agent
            - Fill with the content inside [agent_kb_instructions.txt](aws_bedrock/agent_kb_instructions.txt)
            - Click on Add button
        - Click on Save and exit button to update the Agent configurations
    
    - In Test panel
        - Click on Prepare button
    - Click on Create Alias button
        - Choose "v1" as Alias name
        - Click on Create alias button
    - Then copy the Agent ARN and give it permission to invoke the AWS Lambda function (see more in [SETUP_AWS_LAMBDA.md](SETUP_AWS_LAMBDA.md))
