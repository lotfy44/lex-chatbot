# Serverless Chatbot using Lex V2, Lambda, and DynamoDB

This project implements a fully serverless chatbot architecture using:
- **Amazon Lex V2** — Intent detection  
- **AWS Lambda** — Processing & logic  
- **DynamoDB** — Storing user interactions  

---

## 🚀 Features

- Handles Lex intents using Lambda (DialogCodeHook)
- Stores every user message in DynamoDB
- Serverless, scalable, and cost-efficient
- Deployed fully with AWS CLI

---

## 📁 Project Structure

```
lex-chatbot/
│
├── lambda/
│ └── app.py # Lambda function
│
├── infrastructure/
│ ├── create-table.json # DynamoDB table definition
│ └── commands.txt # AWS CLI deployment script
│
├── .gitignore
└── README.md
```

---

## 🏗️ Deployment (AWS CLI)

### 1️⃣ Create DynamoDB table

```bash
aws dynamodb create-table --cli-input-json file://infrastructure/create-table.json
2️⃣ Create IAM role for Lambda

Attach:

AWSLambdaBasicExecutionRole

DynamoDBFullAccess

3️⃣ Create Lambda function
aws lambda create-function \
  --function-name LexProcessor \
  --runtime python3.10 \
  --role <ROLE_ARN> \
  --handler app.lambda_handler \
  --zip-file fileb://lex_lambda.zip

4️⃣ Allow Lex to call Lambda
aws lambda add-permission \
  --function-name LexProcessor \
  --statement-id lex-invoke-2 \
  --action lambda:InvokeFunction \
  --principal lexv2.amazonaws.com

5️⃣ Connect Lambda inside Lex V2 console

Open Bot → Locale → Intent

Enable Lambda initialization and validation

Select LexProcessor

Build locale

🧪 Testing

Use Lex test window:

Hello


Should return:

Thanks, I recorded your message: 'Hello'


Check DynamoDB:

aws dynamodb scan --table-name ChatbotInteractions

📌 Future Improvements

Multi-intent routing

Slot value validation

Conversation memory

Personalized responses
