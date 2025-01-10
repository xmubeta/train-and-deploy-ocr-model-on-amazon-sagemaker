# Build Docker
```
sh build_and_push.sh <image-name>      # <image-name> will also be ECR respository name, default is paddle
```

# Create Sagemaker endpoint
```
python create_endpoint.py  -e <aws-account-id>.dkr.ecr.cn-north-1.amazonaws.com.cn/<image-name>:latest -en <endpoint-name>
```

# Test predict
Put a picture on S3, then modify test_predict.py at line 42 with S3 bucket name and file path.

```
infer('bucket-name','tmp/20241102.jpg')
```
Then run:
```
python test_predict.py
```