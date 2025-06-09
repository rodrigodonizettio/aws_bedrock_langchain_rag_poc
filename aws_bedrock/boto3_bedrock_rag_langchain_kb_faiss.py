import boto3
import json
import sys
import traceback
# <deprecated> from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_aws import BedrockEmbeddings
from langchain_aws import BedrockLLM
from langchain.prompts.prompt import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader # https://pypi.org/project/pypdf/
from langchain_community.vectorstores import FAISS # https://pypi.org/project/faiss-cpu/
from langchain.chains import LLMChain


AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
AWS_REGION=


global vector_store_faiss


def config_llm():
    try:
        inference_modifier = {
            "temperature": 0.1,  # Adjusted temperature for more focused responses (Range: 0.0 to 1.0, where 0.0 is more precise and conservative. 1.0 is more creative and random)
            "top_p": 1,  # cumulative probability. (Range: 0.0 to 1.0, where 0.0 is more conservative in choosing the vocabulary words. 1.0 is more creative and random)
            "max_gen_len": 1000  # Maximum number of tokens to generate in the response
        }

        model_id = "meta.llama3-70b-instruct-v1:0"

        llm = BedrockLLM(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token=AWS_SESSION_TOKEN,
            region_name=AWS_REGION,
            model_id=model_id,
            model_kwargs=inference_modifier
        )
        return llm
    except Exception as e:
        print(f"Error creating BedrockLLM: {e}")
        traceback.print_exc()
        sys.exit(1)


def config_vector_db(filename):
    try:
        embedding_model_id = 'amazon.titan-embed-text-v1'

        bedrock_embeddings = BedrockEmbeddings(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token=AWS_SESSION_TOKEN,
            region_name=AWS_REGION,
            model_id=embedding_model_id
        )

        loader = PyPDFLoader(filename)

        pages = loader.load_and_split()

        vector_store_faiss = FAISS.from_documents( 
            pages,
            bedrock_embeddings
        )
        return vector_store_faiss # in-memory VectorDB
    except Exception as e:
        print(f"Error configuring vector database: {e}")
        traceback.print_exc()
        sys.exit(1)


def vector_search(query):
    try:
        k = 3  # Number of similar chunks/documents to retrieve based on top scores
        documents = vector_store_faiss.similarity_search_with_score(query, k=k)
        info = ''
        for doc, score in documents:
            info += f"Document: {doc.page_content}\nScore: {score}\n\n"
        return info
    except Exception as e:
        print(f"Error performing vector search: {e}")
        traceback.print_exc()
        sys.exit(1)


llm = config_llm()

vector_store_faiss = config_vector_db('social-media-training.pdf')

prompt_data = """
Human: 
    You are a conversational assistant designed to help answer questions from an employee. 
    You should reply to the human's question using the information provided below. Include all relevant information but keep your answers short. Only answer the question. Do not say things like "according to the training or handbook or according to the information provided...".
    
    <Information>
    {info}
    </Information>
    

    {input}

Assistant:
"""

prompt_template = PromptTemplate(
    input_variables=["info", "input"],
    template=prompt_data
)

question_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="answer"
)

while True:
    try:
        question = input("\nEnter your question about the Social Media Training Manual (or type 'exit' to quit): \n")
        if question.lower() == 'exit':
            sys.exit(0)
        else:
            info = vector_search(question)
            output = question_chain.invoke({
                "info": info,
                "input": question
            })
            print(f"\nAnswer: {output['answer']}\n")
    except Exception as e:
        print(f"Error in main loop: {e}")
        traceback.print_exc()
        sys.exit(1)
