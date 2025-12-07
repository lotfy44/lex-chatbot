# lex-chatbot
# Serverless Chatbot using Lex V2, Lambda, and DynamoDB

This project implements a fully serverless chatbot architecture using:
- **Amazon Lex V2** — Intent detection and NLP  
- **AWS Lambda** — Processing messages  
- **Amazon DynamoDB** — Storing user interactions  

### Features
- Handles Lex intents via Lambda  
- Stores every user message with timestamp and session ID  
- Dynamically responds to user sessions  
- Fully serverless and scalable  
- AWS CLI deployment  

---

## Architecture

1. **User → Lex V2 Bot**  
2. **Lex invokes Lambda**  
3. **Lambda writes to DynamoDB**  
4. **Lambda returns response to Lex**

---

## Project Structure

Lex-chatbot/
│
├── lambda/
│ └── app.py
│
├── infrastructure/
│ ├── create-table.json
│ └── commands.txt
│
└── README.md
