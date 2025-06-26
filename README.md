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

- LangChain
    - LLM Embedding for VectorDB
    - LLM and Prompt for Chat interaction
    - Chain for Query LLM interaction
    - Chat Message History for Memory context

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
    - Step#1: Provide Knowledge Base details
        - Choose the Knowledge Base Name
        - IAM permissions
            - Create and use a new service role
            - Choose the Service Role Name
        - Choose data source
            - Amazon S3
        - Click on Next button
    - Step#2: Configure data source
        - Data source name
            - Choose the Data Source Knowledge Base Name
        - S3 source
            - Paste the S3 URI where you stored your content data
        - Chunking strategy
            - Choose Semantic chunking
        - Max buffer size for comparing sentence groups
            - 0 (default)
        - Max token size for a chunk
            - 300 (default)
        - Breakpoint threshold for sentence group similarity
            - 95 (default)
        - Click on Next button
    - Step#3: Configure data storage and processing
        - Embeddings model
            - Titan Text Embedding V2
        - Vector store
            - Vector store creation method
                - Quick create a new vector store
            - Vector store type
                - Amazon OpenSearch Serverless
    - Step#4: Review and Create
        - Click on Create knowledge base button
    - Step#5: Sync the Data Source
        - Wait until the Data source is created
        - Check the Knowledge Base in Bedrock > Builder tools > Knowledge Bases
        - Click on Sync button 


