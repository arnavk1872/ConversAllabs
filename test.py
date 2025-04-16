from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class AgentRequest(BaseModel):
    provider: str 
    name: str
    description: str
    voice_id: str
    instructions: str

def create_vapi_agent(data: AgentRequest):
    url = "https://api.vapi.ai/assistants"
    payload = {
        "name": data.name,
        "description": data.description,
        "voice_id": data.voice_id,
        "instructions": data.instructions
    }
    headers = {
        "Authorization": "Bearer YOUR_VAPI_API_KEY",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def create_retell_agent(data: AgentRequest):
    url = "https://api.retellai.com/agents"
    payload = {
        "name": data.name,
        "description": data.description,
        "voice": data.voice_id,
        "prompt": data.instructions
    }
    headers = {
        "Authorization": "Bearer YOUR_RETELL_API_KEY",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

@app.post("/create-agent")
def create_agent(agent: AgentRequest):
    if agent.provider.lower() == 'vapi':
        return create_vapi_agent(agent)
    elif agent.provider.lower() == 'retell':
        return create_retell_agent(agent)
    else:
        raise HTTPException(status_code=400, detail="Unsupported provider. Choose 'vapi' or 'retell'.")
