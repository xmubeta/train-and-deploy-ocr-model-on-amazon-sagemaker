import requests
import json

#on sagemaker
import boto3
from botocore.config import Config
from sagemaker.session import Session


config = Config(
    read_timeout=120,
    retries={
        'max_attempts': 0
    }
)
def infer(bucket, input_image):
    from boto3.session import Session
    import json

    
    image_uri = input_image
    test_data = {
        'bucket' : bucket,
        'image_uri' : image_uri,
        'content_type': "application/json",
    }
    payload = json.dumps(test_data)
    print(payload)

    sagemaker_runtime_client = boto3.client('sagemaker-runtime', config=config)
    session = Session(sagemaker_runtime_client)

#     runtime = session.client("runtime.sagemaker",config=config)
    response = sagemaker_runtime_client.invoke_endpoint(
        EndpointName='paddlev7',
        ContentType="application/json",
        Body=payload)

    result = json.loads(response["Body"].read())
    print (result)

infer('bucket-name','tmp/20241102.jpg')
