import os, sys
from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

# set up Vapi secret key
token = os.environ.get('VAPI_API_KEY')

@app.route('/')
def home():
    return render_template('chat.html')

# function to generate outbound call
@app.route('/generate_outbound_call', methods=['POST'])
def generate_call():
    try:
        ############################################################ 
        from agents.brennan import agent

        # Hardcoded transient phone number
        business_number = "d4437aa7-12b0-49ce-b612-6165578a35e1"
        # free vapi random number: +1 (206) 231 6331

        # Hardcoded customer phone number
        customer_number = "+17737240301"

        # Hardcoded Calendly booking link
        booking_link = "https://calendly.com/seanf-boom/new-meeting"   
        ############################################################ 

        from api.payload import load_payload
        from api.vapi import outbound_call
        response = outbound_call(load_payload(agent, business_number, customer_number), token)
        print(f"\nResponse: \n{response}\n")
        
        # Check if follow_up is True and send message if needed
        if response.get('follow_up') == 'True':
            # TODO: Implement send_message function
            # send_message(
            #     preferred_method=response.get('preferred_method'),
            #     phone_contact=response.get('phone_contact'),
            #     email_contact=response.get('email_contact')
            # )
            return jsonify({'success': True, 'message': 'Call initiated successfully. Follow-up message will be sent.'}), 200
        else:
            return jsonify({'success': True, 'message': 'Call initiated successfully. No follow-up needed.'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # run the app
    app.run()
