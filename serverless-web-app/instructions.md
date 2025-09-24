# Exercise 4
## Task 1
1. Download the zip file
```wget <s3-url-for-zip-file>```
2. Unzip the contents
```unzip <zip-file-name>```
3. Send message comand
```aws sqs send-message --https://sqs.us-east-1.amazonaws.com/761151261492/ProductPurchasesDataQueue --message-body file://message-body-2.json```

# Exercise 5
## Task 2
1. Change to backend folder
```cd ~/build-a-serverless-app/Part-2/DCTProductPurchaseForm/backend/```
2. Edit the main.py and modify the queue URL
```sudo nano main.py```
3. Take this file and copy and paste the contents of the modified 'main.py' and paste it into the created Lambda function code window.

# Exercise 6
## Task 1
### Step 8
1. Open the index.html file from the 'DCTProductPurchaseForm/frontend' folder using CloudShell.
2. Copy the API endpoint from the API gateway console and paste it in the placeholder API endpoint on line 125 of the 'index.html'.

# Exercise 7
## Task 1
8. Copy all files from the frontend directory to the S3 bucket (change the bucket name):
```aws s3 sync ./ s3://product-purchases-webform-2e312sd13```

# Optional Extension

## Create a method of processing multiple order entries submitted in json files to an S3 bucket

1. Create an S3 bucket named 'bucket-for-adding-order-files-24d3dq'
2. Create a Lambda function using Python 3.12 named 'load-data-from-s3'
3. Add the code from the 'event-notification-add-to-queue.py' file in the 'optional-extension' folder to the lambda function
4. Edit the queue URL in the code.
5. Edit the execution role and add S3 ready-only permissions and the 'productPurchasesSendMessage' policy
6. Create an event notification for S3 object creation events with the Lambda function as the target
7. Upload the 'items-for-ddb.json' file to the S3 bucket.
8. Check the table to see if the items were added - 10 new records should now appear.