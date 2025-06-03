import boto3
import json
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

prompt_data = """
You're an English and French translator specialist.
Translate to French the following English text: 'Learning about Generative AI is fun and exciting using Amazon Bedrock'.
Don't provide explanations, just return the translated text.
"""

formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{prompt_data}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

native_request = {
    "prompt": formatted_prompt,
    "max_gen_len": 1000, # Maximum number of tokens to generate in the response
    "temperature": 0.2
}

request = json.dumps(native_request)

try:
    response = bedrock_client.invoke_model(
        modelId="meta.llama3-70b-instruct-v1:0",   
        body=request 
    )

    extracted_response = json.loads(response['body'].read().decode('utf-8'))['generation']
    print("Response from the model:", extracted_response)
except Exception as e:
    print(f"Error invoking model: {e}")
    print(traceback.format_exc())
    sys.exit(1)
