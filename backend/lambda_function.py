import json
import boto3
import random
import string
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['URL_TABLE'])

def lambda_handler(event, context):
    # Get the long URL from the request body
    body = json.loads(event['body'])
    long_url = body['longUrl']
    
    # Generate a short key
    short_key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Store the mapping in DynamoDB
    table.put_item(
        Item={
            'short_key': short_key,
            'long_url': long_url
        }
    )

    # Return the shortened URL
    shortened_url = f"https://{os.environ['shortmyurl.in']}/{short_key}"

    return {
        'statusCode': 200,
        'body': json.dumps({
            'shortenedUrl': shortened_url
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
