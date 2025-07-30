def load_payload(agent, business_number, customer_number, twilio_token, twilio_account):
    agent_payload = {
        "assistant": agent,
        "phoneNumber": {
            "twilioAccountSid": twilio_account,
            "twilioAuthToken": twilio_token,
            "twilioPhoneNumber": business_number,
            "smsEnabled": False
        },
        "customer": {
                "number": customer_number
        },
    }

    return agent_payload
