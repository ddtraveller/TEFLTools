import json
import random
import string
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)

s3 = boto3.client('s3')
BUCKET_NAME = 'tl-web'
EXAMS_PREFIX = 'exams/'

def generate_passcode():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Load HTML template
with open('template.html', 'r') as file:
    HTML_TEMPLATE = file.read()

@app.route('/exams', methods=['GET'])
@app.route('/exams/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/exams/api/publish-exam', methods=['POST'])
def publish_exam():
    data = request.json
    exam_id = data.get('examId')
    exam = data.get('exam')
    
    if not exam_id or not exam:
        return jsonify({'error': 'Missing examId or exam data'}), 400
    
    passcode = generate_passcode()
    
    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=f"{EXAMS_PREFIX}{exam_id}.json",
            Body=json.dumps({'exam': exam, 'passcode': passcode}),
            ContentType='application/json'
        )
        return jsonify({'success': True, 'passcode': passcode})
    except Exception as e:
        print(f"Error publishing exam: {str(e)}")
        return jsonify({'error': 'Failed to publish exam'}), 500

@app.route('/exams/api/get-exam', methods=['GET'])
def get_exam():
    exam_id = request.args.get('id')
    
    if not exam_id:
        return jsonify({'error': 'Missing exam id'}), 400
    
    try:
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=f"{EXAMS_PREFIX}{exam_id}.json"
        )
        exam_data = json.loads(response['Body'].read().decode('utf-8'))
        return jsonify(exam_data)  # Return the entire exam_data object
    except s3.exceptions.NoSuchKey:
        return jsonify({'error': 'Exam not found'}), 404
    except Exception as e:
        print(f"Error retrieving exam: {str(e)}")
        return jsonify({'error': 'Failed to retrieve exam'}), 500

@app.route('/exams/api/list-exams', methods=['GET'])
def list_exams():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=EXAMS_PREFIX)
        exam_ids = [obj['Key'].split('/')[-1].replace('.json', '') for obj in response.get('Contents', [])]
        return jsonify(exam_ids)
    except Exception as e:
        print(f"Error listing exams: {str(e)}")
        return jsonify({'error': 'Failed to list exams'}), 500

@app.route('/exams/api/delete-exam', methods=['POST'])
def delete_exam():
    data = request.json
    exam_id = data.get('examId')
    passcode = data.get('passcode')
    
    if not exam_id or not passcode:
        return jsonify({'error': 'Missing examId or passcode'}), 400
    
    try:
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=f"{EXAMS_PREFIX}{exam_id}.json"
        )
        exam_data = json.loads(response['Body'].read().decode('utf-8'))
        
        if exam_data['passcode'] != passcode:
            return jsonify({'error': 'Invalid passcode'}), 403
        
        s3.delete_object(
            Bucket=BUCKET_NAME,
            Key=f"{EXAMS_PREFIX}{exam_id}.json"
        )
        return jsonify({'success': True})
    except s3.exceptions.NoSuchKey:
        return jsonify({'error': 'Exam not found'}), 404
    except Exception as e:
        print(f"Error deleting exam: {str(e)}")
        return jsonify({'error': 'Failed to delete exam'}), 500

@app.route('/exams/take-exam', methods=['GET'])
def take_exam():
    with open('take_exam.html', 'r') as file:
        return file.read()
        
@app.route('/exams/api/submit-exam', methods=['POST'])
def submit_exam():
    data = request.json
    exam_id = data.get('examId')
    submitted_answers = data.get('answers')
    
    if not exam_id or not submitted_answers:
        return jsonify({'error': 'Missing examId or answers'}), 400
    
    try:
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=f"{EXAMS_PREFIX}{exam_id}.json"
        )
        exam_data = json.loads(response['Body'].read().decode('utf-8'))
        exam_questions = exam_data['exam']
        
        if len(submitted_answers) != len(exam_questions):
            return jsonify({'error': 'Number of answers does not match number of questions'}), 400
        
        score = sum(1 for q, a in zip(exam_questions, submitted_answers) if q['correctAnswer'] == a)
        total = len(exam_questions)
        
        return jsonify({'score': score, 'total': total})
    except s3.exceptions.NoSuchKey:
        return jsonify({'error': 'Exam not found'}), 404
    except Exception as e:
        print(f"Error grading exam: {str(e)}")
        return jsonify({'error': 'Failed to grade exam'}), 500
        
def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    # Extract relevant information from the event
    http_method = event['requestContext']['http']['method']
    path = event['rawPath']
    headers = event['headers']
    query_string = event.get('rawQueryString', '')
    body = event.get('body', '')

    # Create a Flask request context
    with app.test_request_context(
        path=path,
        method=http_method,
        headers=headers,
        query_string=query_string,
        data=body
    ):
        try:
            # Dispatch the request to Flask
            response = app.full_dispatch_request()
            
            # Prepare the response for API Gateway
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
        except Exception as e:
            print(f"Error processing request: {str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

# Add this at the end of your file
app.config['FLASK_DEBUG'] = False

if __name__ == '__main__':
    app.run(debug=True)