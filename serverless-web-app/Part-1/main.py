import json
import boto3
import uuid
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Fetch the region from environment variable or use a default
region = os.environ.get('Region', 'us-east-1')

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name=region)

# Specify the table
table = dynamodb.Table('ProductPurchases')

def lambda_handler(event, context):
    logger.info('Received event: %s', json.dumps(event, indent=2))

    for record in event['Records']:
        body = record['body']
        logger.info('Record body: %s', body)
        
        # Parse the body as JSON
        body = json.loads(body)
        
        try:
            # Extract fields
            ProductId = body.get('ProductId')
            ProductName = body.get('ProductName')
            Category = body.get('Category')
            PricePerUnit = body.get('PricePerUnit')
            CustomerId = body.get('CustomerId')
            CustomerName = body.get('CustomerName')
            TimeOfPurchase = body.get('TimeOfPurchase')

            # Check for missing fields
            if not all([ProductId, ProductName, Category, PricePerUnit, CustomerId, CustomerName, TimeOfPurchase]):
                logger.warning('Missing one or more fields in the message.')
                continue

            # Generate a unique key for the entire product purchase entry
            ProductPurchaseKey = str(uuid.uuid4())

            # Insert a single item with all attributes
            table.put_item(Item={
                'ProductPurchaseKey': ProductPurchaseKey,
                'ProductId': ProductId,
                'ProductName': ProductName,
                'Category': Category,
                'PricePerUnit': PricePerUnit,
                'CustomerId': CustomerId,
                'CustomerName': CustomerName,
                'TimeOfPurchase': TimeOfPurchase
            })

            logger.info('Item successfully inserted into DynamoDB.')

        except Exception as e:
            logger.error('Error occurred: %s', str(e), exc_info=True)

    return {}
