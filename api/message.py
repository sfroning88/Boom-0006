def send_text(booking_link, twilio_token, twilio_account, business_number, customer_number):
    from twilio.rest import Client

    agent_message = f'''
    Hello! Thank you for taking the time earlier to speak about what my small business can do for you.
    Go ahead and book a 15 minute meeting with Sean using this link: 
    {booking_link}

    Best,
    Small Business
    '''

    # Create Twilio client
    client = Client(twilio_account, twilio_token)

    # Send SMS using client
    message = client.messages.create(
        body=agent_message,
        from_=business_number,
        to=customer_number
    )
    
    return True

def send_email(response):
    pass
