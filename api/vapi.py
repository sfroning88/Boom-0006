def outbound_call(agent_payload, token):
    import requests

    # Set the API endpoint
    url = "https://api.vapi.ai/call"

    # Set the headers with the Bearer token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Make the POST request to initiate the call
    response = requests.post(url, json=agent_payload, headers=headers)
    print(f"\nResponse: \n{response.call.json()}\n")

    # Return the extracted variables
    return {
        'success': True,
        'follow_up': response.call.analysis.structuredData.get('follow_up', 'False'),
        'preferred_contact': response.call.analysis.structuredData.get('preferred_contact', 'NA'),
        'phone_contact': response.call.analysis.structuredData.get('phone_contact', 'NA'),
        'email_contact': response.call.analysis.structuredData.get('email_contact', 'NA')
    }
