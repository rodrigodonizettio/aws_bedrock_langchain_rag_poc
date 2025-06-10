# aws_bedrock_langchain_rag_poc
AWS Bedrock knowledge based on Lee Assam's course Learning Amazon Bedrock.

Following the code inside **aws_bedrock** folder you'll be able to learn AI concepts until you reach the final file [**bedrock_rag_streamlit_chat_bot.py**](aws_bedrock/bedrock_rag_streamlit_chat_bot.py) where we build a Chat Bot application using:
- LangChain
    - LLM Embedding for VectorDB
    - LLM and Prompt for Chat interaction
    - Chain for Query LLM interaction
    - Chat Message Histories for Memory context
    
- PyPDF for PDF files management

- Facebook
    - FAISS (Facebook AI Similarity Search) for VectorDB clustering and similarity search tasks

- StreamLit for Chat Web App

![Final Chat Bot Project Result](aws_bedrock/bedrock_rag_streamlit_chat_bot.png)

<br />

LLMs explored in the codes:
- Amazon Titan Embed Text-v1
- Amazon Titan Text Express v1
- Meta Llama3 70b Instruct v1.0


The AWS Bedrock configurations for this course were done using **AWS Management Console**.
You can see below how to do that.

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


    

