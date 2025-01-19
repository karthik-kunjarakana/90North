import json
import base64
import boto3
import uuid

def lambda_handler(event, context):
    file_content = event.get('file_content')
    file_name = event.get('file_name', f"document_{uuid.uuid4()}.pdf")
    bucket_name = 'samplebucketassignment'
    
    if file_content:
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'
        )
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully!',
                'file_name': file_name
            })
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'No file content provided.'
            })
        }
