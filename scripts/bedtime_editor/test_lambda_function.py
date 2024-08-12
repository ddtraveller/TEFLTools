import unittest
from unittest.mock import patch, MagicMock
import json
import hashlib

# Import the Lambda function code (assuming it's in a file named lambda_function.py)
import lambda_function

class TestLambdaFunction(unittest.TestCase):
    
    # Add a test password for use in our tests
    TEST_PASSWORD = 'test_password_123'

    @patch('lambda_function.s3')
    @patch.object(lambda_function, 'ALLOWED_PASSWORDS', [TEST_PASSWORD])
    def test_update_story_success(self, mock_s3):
        # Mock the S3 put_object method
        mock_s3.put_object.return_value = None

        # Prepare test data
        test_key = 'bedtime_test.html'
        test_content = '<html><body>Test content</body></html>'
        test_password = self.TEST_PASSWORD

        event = {
            'body': json.dumps({
                'action': 'update',
                'key': test_key,
                'content': test_content,
                'password': test_password
            })
        }

        # Call the lambda_handler
        response = lambda_function.lambda_handler(event, None)

        # Assert the response
        self.assertEqual(response['statusCode'], 200)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Story updated successfully')
        
        # Verify MD5 hash
        expected_md5 = hashlib.md5(test_content.encode()).hexdigest()
        self.assertEqual(response_body['md5'], expected_md5)

        # Verify S3 put_object was called with correct arguments
        mock_s3.put_object.assert_called_once_with(
            Bucket='tl-web',
            Key='stories/' + test_key,
            Body=test_content,
            ContentType='text/html'
        )

    @patch.object(lambda_function, 'ALLOWED_PASSWORDS', [TEST_PASSWORD])
    def test_update_story_invalid_password(self):
        event = {
            'body': json.dumps({
                'action': 'update',
                'key': 'bedtime_test.html',
                'content': 'Test content',
                'password': 'invalid_password'
            })
        }

        response = lambda_function.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 403)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Invalid password')

    @patch.object(lambda_function, 'ALLOWED_PASSWORDS', [TEST_PASSWORD])
    def test_update_story_invalid_filename(self):
        event = {
            'body': json.dumps({
                'action': 'update',
                'key': 'invalid_filename.txt',
                'content': 'Test content',
                'password': self.TEST_PASSWORD
            })
        }

        response = lambda_function.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 400)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Invalid file name. Only bedtime stories with .html extension are allowed.')

    def test_invalid_action(self):
        event = {
            'body': json.dumps({
                'action': 'invalid_action'
            })
        }

        response = lambda_function.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 400)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Invalid action')

    def test_missing_parameters(self):
        event = {
            'body': json.dumps({
                'action': 'update',
                'key': 'bedtime_test.html',
                # Missing 'content' and 'password'
            })
        }

        response = lambda_function.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 400)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Missing key, content, or password')

    @patch('lambda_function.s3')
    @patch.object(lambda_function, 'ALLOWED_PASSWORDS', [TEST_PASSWORD])
    def test_s3_error(self, mock_s3):
        # Mock S3 to raise an exception
        mock_s3.put_object.side_effect = Exception("S3 error")

        event = {
            'body': json.dumps({
                'action': 'update',
                'key': 'bedtime_test.html',
                'content': 'Test content',
                'password': self.TEST_PASSWORD
            })
        }

        response = lambda_function.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 500)
        response_body = json.loads(response['body'])
        self.assertTrue(response_body['message'].startswith('Error updating S3:'))

if __name__ == '__main__':
    unittest.main()