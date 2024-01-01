# Summary of Lambda Function Deployment Process

## Encountered Problems
1. **Module Import Error**: 
   - AWS Lambda was unable to import the `lambda_function` module. This was caused by incorrect handler configuration or improper file structure in the deployment package.

2. **Permission Error**:
   - Encountered a permission issue with `FetchJobsData.py`. This indicated that the AWS Lambda execution environment lacked the necessary permissions to execute or read the script.

3. **SSL/TLS Connection Error**:
   - The script failed to connect to the PostgreSQL database, requiring an SSL/TLS connection for security.

## Steps for Lambda Function Deployment

### A. Fixing Module Import and Permission Issues
1. **Handler Configuration**:
   - Ensure the handler in AWS Lambda matches the filename and function name, e.g., `FetchJobsData.lambda_handler`.

2. **File Permissions**:
   - Set appropriate permissions for the Python file (`FetchJobsData.py`) before zipping. Use `chmod 644` for read/write permissions or `chmod 755` for executable permissions.

### B. Installing psycopg2-binary with Amazon Linux Compatibility
1. **psycopg2-binary Installation**:
   - Download from [https://github.com/jkehler/awslambda-psycopg2/tree/master/with_ssl_support](https://github.com/jkehler/awslambda-psycopg2/tree/master/with_ssl_support)
   - Use psycopg2-3.8
   - Rename it to psycopg2
   - Make sure Lambda runtime is Python 3.8
   - move to the same directory as `FetchJobsData.py`
   - inside the directory, run `chmod 755 FetchJobsData.py` and `zip -r ../lambda_deployment.zip .`
   - upload the zip file as the Lambda function's deployment package