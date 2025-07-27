def outbound_call(agent_payload, vapi_token):
    import requests
    import json
    import time

    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {vapi_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=agent_payload, headers=headers)
    response.raise_for_status()
    
    call_id = response.json().get('id')
    if call_id:
        poll_url = f"{url}/{call_id}"
        for _ in range(30):
            poll_resp = requests.get(poll_url, headers=headers)
            data = poll_resp.json()
            if data.get('endedAt'):
                structured_data = data.get('analysis', {}).get('structuredData', {})
                return {
                    "success": True,
                    "message": "Call successfully completed, continuing program.",
                    "follow_up": structured_data.get("follow_up", False),
                    "preferred_contact": structured_data.get("preferred_contact", "NA"),
                    "phone_contact": structured_data.get("phone_contact", "NA"),
                    "email_contact": structured_data.get("email_contact", "NA")
                }
            time.sleep(10)
        return {"success": False, "message": "Call did not finish in time.", "follow_up": False}
    else:
        time.sleep(60)
        return {"success": False, "message": "No call ID, fallback sleep used.", "follow_up": False}
