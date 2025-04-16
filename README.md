# STEPS TO RUN THE CODE

(1) Change directory to the project repo and add the mentioned dependencies
    pip install fastapi uvicorn requests
    
(2) Run uvicorn test:app --reload to start the server

(3) Visit Swagger's URL on the running server which is http://127.0.0.1:8000/docs

(4) Add Real API keys for RETELL AND VAPI. I have used dummy variables in the added code.

(5) Use the below JSON to verify, you can just changes vapi to provider and vice versa to change the API being called.

{
  "provider": "vapi",
  "name": "Test Agent",
  "description": "Agent to test vapi",
  "voice_id": "en_us_001",
  "instructions": "Help the user with their queries."
}

