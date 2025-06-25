import sys
import traceback
# <deprecated> from langchain.chains.retrieval_qa import RetrievalQA
from langchain.chains import RetrievalQA
# <deprecated> from langchain.llms.bedrock import Bedrock # https://pypi.org/project/langchain/ ; https://pypi.org/project/langchain-community/
from langchain_aws import BedrockLLM  # https://pypi.org/project/langchain-aws/ ;
# <deprecated> from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
from langchain_aws.retrievers.bedrock import AmazonKnowledgeBasesRetriever


AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
AWS_REGION=
AWS_CREDENTIALS_PROFILE_NAME=


def config_llm():
    inference_modifier = {
        "temperature": 0,  # Adjusted temperature for more focused responses (Range: 0.0 to 1.0, where 0.0 is more precise and conservative. 1.0 is more creative and random)
        "topP": 1,  # cumulative probability. (Range: 0.0 to 1.0, where 0.0 is more conservative in choosing the vocabulary words. 1.0 is more creative and random)
        "maxTokenCount": 1000  # Maximum number of tokens to generate in the response
    }
    
    model_id = "amazon.titan-text-express-v1"

    llm = BedrockLLM(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION,
        model_id=model_id,
        model_kwargs=inference_modifier
    )
    return llm


def config_kb_retriever():
    my_bedrock_kb_id = "myKBID" # AWS Bedrock > Builder Tools > Knowledge Bases > myKB > Knowledge Base ID

    kb_retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id=my_bedrock_kb_id, 
        region_name=AWS_REGION,
        credentials_profile_name=AWS_CREDENTIALS_PROFILE_NAME,  # Use valid credentials profile name from ~/.aws/credentials
        retrieval_config={
            "vectorSearchConfiguration": {
                "numberOfResults": 5
            }
        }
    )
    return kb_retriever


def create_qa_chain(llm, kb_retriever):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=kb_retriever,
        return_source_documents=True
    )
    return qa_chain


llm = config_llm()
kb_retriever = config_kb_retriever()
qa_chain = create_qa_chain(llm, kb_retriever)

while True:
    try:
        query = input("\nEnter your question about the KB (or type 'exit' to quit): \n")
        if query.lower()  == 'exit':
            sys.exit(0)
        else:
            response = qa_chain.invoke(query)
            print('Response is:', response['result'])
            source_docs = response['source_documents']
            print('\nSource documentation are:')
            for doc in source_docs:
                meta = doc.metadata.get('source_metadata')
                print(f"- {meta.get('x-amz-bedrock-kb-source-uri', 'No URI')} (Page Number: {meta.get('x-amz-bedrock-kb-document-page-number', 'No Page Number')})")      
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        sys.exit(1)
