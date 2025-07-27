def load_payload(agent_id, business_number, customer_number):
    agent_prompt = [{
        "role": "system", 
        "content": '''
        You will be given the transcript of the call and the system prompt of the AI Assistant. 
        JSON Schema: \{schema\}, extract the following using only JSON format:
        1) follow_up : either True or False for if the client would like to be sent a link for a meeting
        2) preferred_contact : if applicable, either "phone" or "email"; "NA" if not found
        3) phone_contact : if applicable, the full phone number; "NA" if not found
        4) email_contact : if applicable, the full email address; "NA" if not found
        '''
    }, 
    { 
      "role": "user", 
      "content": '''
      Here is the transcript: \{transcript\}. 
      Here is the ended reason of the call: \{endedReason\}
      '''
    }]
    
    agent_payload = {
        "assistantId": agent_id,
            "phoneNumberId": business_number,
            "customer": {
                "number": customer_number,
            },
        "assistantOverrides": {
            "maxDurationSeconds": 300,
            "analysisPlan": {
                "structuredDataPlan": {
                    "enabled": True,
                    "messages": agent_prompt,
                    "timeoutSeconds": 20
                }
            }
        }
    }

    return agent_payload
