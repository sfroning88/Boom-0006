def load_payload(agent, business_number, customer_number):
    agent_payload = {
        "assistant": agent,
        "phoneNumberId": business_number,
        "customer": {
                "number": customer_number,
        },
    }

    return agent_payload
