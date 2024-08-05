FROM public.ecr.aws/lambda/python:3.9

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy function code and other files
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY dictionary.json ${LAMBDA_TASK_ROOT}
COPY phrases.json ${LAMBDA_TASK_ROOT}
COPY compound.json ${LAMBDA_TASK_ROOT}
COPY E2T.txt ${LAMBDA_TASK_ROOT}
COPY T2E.txt ${LAMBDA_TASK_ROOT}
COPY template.html ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "lambda_function.lambda_handler" ]