import boto3
# <deprecated> from langchain.llms.bedrock import Bedrock # https://pypi.org/project/langchain/ ; https://pypi.org/project/langchain-community/
from langchain_aws import BedrockLLM  # https://pypi.org/project/langchain-aws/ ;
import sys
import traceback


AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
AWS_REGION=


try:
    bedrock_client = boto3.client(
        'bedrock-runtime',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION
    )
except Exception as e:
    print(f"Error creating Bedrock client: {e}")
    sys.exit(1)

inference_modifier = {
    "temperature": 0.2,  # Adjusted temperature for more focused responses (Range: 0.0 to 1.0, where 0.0 is more precise and conservative. 1.0 is more creative and random)
    "topP": 0.2,  # cumulative probability. (Range: 0.0 to 1.0, where 0.0 is more conservative in choosing the vocabulary words. 1.0 is more creative and random)
    "maxTokenCount": 1000  # Maximum number of tokens to generate in the response
}

try:
    llm = BedrockLLM(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION,
        model_id="amazon.titan-text-express-v1",
        model_kwargs=inference_modifier
    )
except Exception as e:
    print(f"Error initializing BedrockLLM: {e}")
    sys.exit(1)

'''
<deprecated>
llm = Bedrock(
    model_id="amazon.titan-text-express-v1",
    client=bedrock_client,
    model_kwargs=inference_modifier
)
'''

prompt_data = """
You're a Lord of the Rings expert.
Provide the list of top#20 main characters in the Lord of the Rings' movies universe.
"""

try:
    response = llm.invoke(prompt_data)
    print("Response from the model:", response)
except Exception as e:
    print(f"Error invoking model: {e}")
    print(traceback.format_exc())
    sys.exit(1)
