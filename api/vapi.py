def outbound_call(agent_id):
  import requests
    import os

    # Set your Vapi API token (should be set as an environment variable for security)
    token = os.environ.get('VAPI_API_KEY')

    # Hardcoded customer phone number
    customer_number = "+17737240301"

    # Hardcoded transient phone number
    business_number = "d4437aa7-12b0-49ce-b612-6165578a35e1"
    # free vapi random number: +1 (206) 231 6331

    # Hardcoded Calendly booking link
    booking_link = "https://calendly.com/seanf-boom/new-meeting"

    # Prepare the payload for the outbound call
    payload = {
        "assistantId": agent_id,
        "phoneNumberId": business_number,
        "customer": {
            "number": customer_number,
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
