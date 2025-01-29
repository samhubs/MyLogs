import utils
import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    for record in event['Records']:
        srcbucket = record['s3']['bucket']['name']
        srckey = record['s3']['object']['key']

        desbucket = "all-uploads-source"
        desfolder = "uploads-anil"
        deskey = desfolder + "/" + srckey
        print("Source Bucket: " + srcbucket)
        print("Source Key: " + srckey)
        print("Destination Bucket: " + desbucket)
        print("Destination Key: " + deskey)
        source = {
            'Bucket': srcbucket,
            'Key': srckey
        }
        dest = {
            'Bucket': desbucket,
            'Key': deskey
        }
        s3.meta.client.copy(source, desbucket, deskey)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
