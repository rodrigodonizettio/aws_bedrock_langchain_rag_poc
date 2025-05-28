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

model_id = "amazon.titan-text-express-v1"
accept_type = "application/json"
content_type = "application/json"

prompt_data = """
You're a Lord of the Rings expert.
Provide the list of top#20 main characters in the Lord of the Rings' movies universe.
"""

body_data = json.dumps({
    "inputText": prompt_data,
    "textGenerationConfig": {
        "maxTokenCount": 1000,
        "temperature": 0.2, # Adjusted temperature for more focused responses (Range: 0.0 to 1.0, where 0.0 is more precise and conservative. 1.0 is more creative and random)
        "topP": 0.2 # cumulative probability. (Range: 0.0 to 1.0, where 0.0 is more conservative in choosing the vocabulary words. 1.0 is more creative and random)
    }
})

try:
    response = bedrock_client.invoke_model(
        modelId=model_id,
        accept=accept_type,
        contentType=content_type,
        body=body_data
    )

    response_body = json.loads(response['body'].read().decode('utf-8'))
    print('response_body:', response_body)
    if response_body['results'][0]['outputText']:
        extracted_response = response_body['results'][0]['outputText']
    else:
        extracted_response = "No output text found in the response."
    print("Response from the model:", extracted_response)

except Exception as e:
    print(f"Error invoking model: {e}")
    print(traceback.format_exc())
    sys.exit(1)
