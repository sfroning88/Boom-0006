def send_text(booking_link, twilio_token, twilio_account, sender, receiver):
    from twilio.rest import Client

    agent_message = f'''
    Hello! Thank you for taking the time earlier to speak about what my small business can do for you.
    Go ahead and book a 15 minute meeting with Sean using this link: 
    {booking_link}

    Best,
    Small Business
    '''

    try: 
        # Create Twilio client
        client = Client(twilio_account, twilio_token)

        # Send SMS using client
        message = client.messages.create(
        body=agent_message,
        from_=sender,
        to=receiver
        )
        return True

    except Exception as e:
        print(e)
        return False

def send_email(booking_link, sendgrid_token, sender, receiver):
    import ssl, certifi
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    agent_message = f'''
    Hello! Thank you for taking the time earlier to speak about what my small business can do for you.
    Go ahead and book a 15 minute meeting with Sean using this link: 
    {booking_link}

    Best,
    Small Business
    '''

    try:
        message = Mail(
        from_email=str(sender),
        to_emails=str(receiver),
        subject="Follow Up Booking Link",
        html_content=f"<strong>{agent_message}</strong>"
        )

        # Create SSL context with proper certificate verification
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        sg = SendGridAPIClient(sendgrid_token)

        # Send email using Client
        response = sg.send(message)
        return True
        
    except Exception as e:
        print(e)
        return False
