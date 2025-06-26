import sys
import traceback
# <deprecated> from langchain.chains.conversational_retrieval import ConversationalRetrievalChain
from langchain.chains import ConversationalRetrievalChain
# <deprecated> from langchain.llms.bedrock import Bedrock # https://pypi.org/project/langchain/ ; https://pypi.org/project/langchain-community/
from langchain_aws import BedrockLLM  # https://pypi.org/project/langchain-aws/ ;
# <deprecated> from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
from langchain_aws.retrievers.bedrock import AmazonKnowledgeBasesRetriever
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT


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
    
    model_id = "amazon.titan-text-express-v1"  # Titan Text Express

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
    kb_retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id="myKBID", # AWS Bedrock > Builder Tools > Knowledge Bases > myKB > Knowledge Base ID
        region_name=AWS_REGION,
        credentials_profile_name=AWS_CREDENTIALS_PROFILE_NAME,  # Use valid credentials profile name from ~/.aws/credentials
        retrieval_config={
            "vectorSearchConfiguration": {
                "numberOfResults": 5
            }
        }
    )
    return kb_retriever


def config_prompt_template():
    my_prompt_template = '''
        You are a conversational assistant. Answer the question based on the knowledge base provided context.
        
        Context: {context}

        {chat_history}
        
        Question: {question}
    '''

    prompt_template = PromptTemplate(
        template=my_prompt_template,
        input_variables=['context', 'chat_history', 'question']
    )
    return prompt_template


def create_qa_chain(llm, kb_retriever, prompt_template):
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        output_key='answer',
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=kb_retriever,
        return_source_documents=True,
        combine_docs_chain_kwargs={
            'prompt': prompt_template
        },
        memory=memory,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT
    )
    return qa_chain


llm = config_llm()
kb_retriever = config_kb_retriever()
prompt_template = config_prompt_template()
qa_chain_with_history = create_qa_chain(llm, kb_retriever, prompt_template)

while True:
    try:
        query = input("\nEnter your question about the KB (or type 'exit' to quit): \n")
        if query.lower()  == 'exit':
            sys.exit(0)
        else:
            response = qa_chain_with_history.invoke({
                'question': query,
                'chat_history': qa_chain_with_history.memory.load_memory_variables({})
            })
            print('Response is:', response['answer'])
            source_docs = response['source_documents']
            print('\nSource documentation are:')
            for doc in source_docs:
                meta = doc.metadata.get('source_metadata')
                print(f"- {meta.get('x-amz-bedrock-kb-source-uri', 'No URI')} (Page Number: {meta.get('x-amz-bedrock-kb-document-page-number', 'No Page Number')})")      
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        sys.exit(1)
