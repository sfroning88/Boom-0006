def outbound_call(agent_payload, token):
    import requests
    import json

    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    print(f"DEBUG Payload (dict): {agent_payload}")
    print(f"DEBUG Payload (json): {json.dumps(agent_payload)}")
    print(f"DEBUG Headers: {headers}")

    try:
        response = requests.post(url, json=agent_payload, headers=headers)
        print(f"DEBUG Response Status: {response.status_code}")
        print(f"DEBUG Response Text: {response.text}")
        response.raise_for_status()
    except Exception as e:
        print(f"DEBUG Exception: {e}")
        raise

    structured_data = response.json().get('analysis', {}).get('structuredData', {})
    print(f"\nStructured Data: \n{structured_data}\n")
    
    return {
        "success": True,
        "follow_up": structured_data.get("follow_up", 'False'),
        "preferred_contact": structured_data.get("preferred_contact", "NA"),
        "phone_contact": structured_data.get("phone_contact", "NA"),
        "email_contact": structured_data.get("email_contact", "NA")
    }
