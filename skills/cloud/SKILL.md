---
name: cloud-platform-aws
description: AWS cloud platform fundamentals including EC2, S3, RDS, Lambda, and cloud architecture best practices.
---

# Cloud Platform Fundamentals (AWS)

## EC2 Setup

### Launch and Configure Instance

```bash
# Using AWS CLI
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.small \
  --key-name my-key-pair \
  --security-groups web-server-sg

# SSH into instance
ssh -i my-key-pair.pem ec2-user@<instance-ip>

# Update and install software
sudo yum update -y
sudo yum install -y nodejs npm
```

## S3 for Storage

### Upload and Retrieve Objects

```python
import boto3

s3_client = boto3.client('s3')

# Upload file
s3_client.upload_file(
    'local_file.txt',
    'my-bucket',
    'path/to/object.txt'
)

# Download file
s3_client.download_file(
    'my-bucket',
    'path/to/object.txt',
    'downloaded_file.txt'
)

# List objects
response = s3_client.list_objects_v2(Bucket='my-bucket')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Set public access
s3_client.put_object_acl(
    Bucket='my-bucket',
    Key='path/to/object.txt',
    ACL='public-read'
)
```

## RDS Database

### Create and Connect

```bash
# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.small \
  --engine postgres \
  --master-username admin \
  --master-user-password password123 \
  --allocated-storage 20

# Connect using psql
psql -h mydb.xxxxxx.us-east-1.rds.amazonaws.com \
     -U admin \
     -d mydb
```

## Lambda Function

### Serverless Function

```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    try:
        # Parse request
        user_id = event['pathParameters']['userId']

        # Query database
        response = table.get_item(Key={'id': user_id})
        user = response.get('Item')

        if not user:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps(user)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

## DynamoDB

### Table Operations

```python
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# Create item
table.put_item(Item={
    'id': '123',
    'name': 'John Doe',
    'email': 'john@example.com',
    'created_at': '2025-11-18'
})

# Read item
response = table.get_item(Key={'id': '123'})
print(response['Item'])

# Update item
table.update_item(
    Key={'id': '123'},
    UpdateExpression='SET #name = :val',
    ExpressionAttributeNames={'#name': 'name'},
    ExpressionAttributeValues={':val': 'Jane Doe'}
)

# Query items
response = table.query(
    KeyConditionExpression='id = :id',
    ExpressionAttributeValues={':id': '123'}
)
```

## IAM Policies

### Policy Example

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/Users"
    }
  ]
}
```

## VPC and Networking

### VPC Configuration

```
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24)
│   ├── Route Table → Internet Gateway
│   └── NAT Gateway
├── Private Subnet (10.0.2.0/24)
│   ├── Route Table → NAT Gateway
│   └── RDS Database
└── Security Groups
    ├── Web SG (allows 80, 443, 22)
    └── DB SG (allows 5432 from Web SG)
```

## Key Concepts

1. **Compute Services**
2. **Storage Solutions**
3. **Database Options**
4. **Networking & VPC**
5. **Security & IAM**
6. **Monitoring & Logging**
7. **Cost Optimization**