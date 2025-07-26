def call_vapi(agent_id):
  import requests
    import os

    # Set your Vapi API token (should be set as an environment variable for security)
    token = os.environ.get('VAPI_API_KEY')

    # Hardcoded phone number for MVP
    phone_number = "+17737240301"

    # Hardcoded Calendly booking link
    booking_link = "https://calendly.com/seanf-boom/new-meeting"

    # Prepare the payload for the outbound call
    payload = {
        "assistantId": agent_id,  # Use the assistantId, not the full URL
        "customer": {
            "number": phone_number
        },
        # Optionally, you could pass context or variables here
        "assistantOverrides": {
            "templateVariables": {
                "booking_link": booking_link
            }
        }
    }

    # Set the API endpoint
    url = "https://api.vapi.ai/call"

    # Set the headers with the Bearer token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Make the POST request to initiate the call
    response = requests.post(url, json=payload, headers=headers)

    # Raise an error if the call failed
    response.raise_for_status()

    # Return the response JSON
    return response.json()
