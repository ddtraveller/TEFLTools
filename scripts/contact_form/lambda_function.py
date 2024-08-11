import json
import boto3

def lambda_handler(event, context):
    # Parse the incoming JSON data
    body = json.loads(event['body'])
    
    # Extract form data
    name = body['name']
    email = body['email']
    message = body['message']
    
    # Compose the message to be sent to SNS
    sns_message = f"New contact form submission:\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    
    # Create an SNS client
    sns = boto3.client('sns')
    
    try:
        # Publish the message to the SNS topic
        response = sns.publish(
            TopicArn='arn:aws:sns:us-west-2:874956223356:my_email',
            Message=sns_message,
            Subject='New Contact Form Submission'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent successfully!')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending message.')
        }