import os, sys
from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template('chat.html')

# function to generate outbound call
@app.route('/generate_outbound_call', methods=['POST'])
def generate_call():
    try:
        from agents.brennan import agent_id
        from api.vapi import call_vapi
        call_vapi(agent_id)
        return jsonify({'success': True, 'message': 'Call initiated successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # run the app
    app.run()
