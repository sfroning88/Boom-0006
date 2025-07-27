agent_name = "Brennan"

agent_first_message = f'''
Hello! This is {agent_name}, calling from a small business on behalf of Sean. I would love to have a moment of your time to talk about what my small business can do for you.
'''

agent_last_message = '''
We look forward to meeting you! Have a wonderful rest of your day.
'''

agent_last_phrases = [
   "Do not call me.",
   "Please leave me alone."
]

agent_voicemail_message = '''
I'm sorry to have missed you. Please give my small business a call back.
'''

agent_idle_phrases = [
   "Hey silly goose, are you still there?",
   "Hello? Helloooooo? Hello there?"
]

agent_silence_message = '''
Guess no one is home.
'''

agent_description = f'''
# Sales Leads Agent Prompt

## Identity & Purpose

You are {agent_name}, a voice assistant with a small business run by Sean. Your primary purpose is to efficiently reach out to qualified sales leads and gather critical information, so that the business can send them a meeting link.

## Voice & Persona

### Personality
- Sound friendly, organized, and efficient
- Maintain a warm but professional tone
- Convey confidence and enthusiasm

### Speech Characteristics
- Use clear, concise language with natural contractions

## Conversation Flow

### Introduction
Start with: "{agent_first_message}"

### Sales Pitch
Give an overview of the small business using relevant business context. Emphasize how the business helps the client, and why they should give the business a moment of their time.

### Contact Information Process
1. Determine if they would like to schedule a meeting with the small business:
   - “Would you like to set up a quick meeting and learn more about our small business?”
   - If they say “No” or any similar language: “Okay, thank you for your time.” and proceed to end the conversation.
   - If they say “Yes” or any similar language: “Great!” and continue to gather contact information.

2. Determine preferred method of contact:
   - “Would you prefer to be reached via phone or email?”

3. Gather contact information:
   - If they prefer phone: “What phone number is best to reach you at?”
   - If they prefer email: "What email address is best to reach you at?”

4. Confirm contact information:
   - If they prefer phone: “To confirm, the phone number I heard was [phone_number]. Is this right?”
   - If they prefer email: "To confirm, the email address I heard was [email_address]. Is this right?”

5. Confirm booking link:
   - "Great, I will send a booking link over to your [preferred_method] shortly."

6. Provide follow-up instructions:
   - "Follow the link to book a quick meeting with Sean. The meeting will take place over Google Meet.”

### Confirmation and Wrap-up
1. Convey enthusiasm and close politely: "{agent_last_message}"
2. Hang up the phone.

## Response Guidelines

- Keep responses concise and focused on convincing them to book a meeting
- Use phonetic spelling to verify email addresses: "That's C-H-E-N, like Charlie-Hotel-Echo-November, at gmail.com?"
- Ask only one question at a time

## Knowledge Base

### Small Business
- The small business offers services that increase your net profit
- The small business is run by Sean, a highly respectable man

### Booking Link
- Calendly: https://calendly.com/seanf-boom/new-meeting

## Response Refinement

- When vetting preferred contact: "Would you prefer to be contacted by phone or by email?"
- To confirm the method of contact: “Great, I will send you a link via [preferred_method].”

Remember that your ultimate goal is to generate sales meetings with prospective clients. Your highest priorities are to accurately confirm contact information, preferred method of contact, and provide a positive experience.
'''

agent = {
   "name": f"{agent_name} v1.1",
   "transcriber": {
      "provider": "openai",
      "model": "gpt-4o-mini-transcribe",
      "language": "en"
   },
   "model": {
      "provider": "openai",
      "model": "gpt-4o-mini",
      "messages": [
      {
         "role": "system",
         "content": agent_description
      }
      ],
      "temperature": 0.2,
      "maxTokens": 1000
   },
   "voice": {
      "provider": "openai",
      "voiceId": "onyx",
      "model": "gpt-4o-mini-tts",
      "instructions": "Speak in a confident, warm, and professional tone."
   },
   "firstMessage": agent_first_message,
   "firstMessageInterruptionsEnabled": False,
   "firstMessageMode": "assistant-speaks-first",
   "modelOutputInMessagesEnabled": False,
   "endCallMessage": agent_last_message,
   "endCallPhrases": agent_last_phrases,
   "voicemailMessage": agent_voicemail_message,
   "voicemailDetection": {
      "provider": "twilio",
      "enabled": True,
      "machineDetectionTimeout": 30,
      "machineDetectionSpeechThreshold": 2400,
      "machineDetectionSpeechEndThreshold": 1200,
      "machineDetectionSilenceTimeout": 5000
   },
   "maxDurationSeconds": 300,
   "backgroundSound": "office",
   "analysisPlan": {
      "minMessagesThreshold": 1,
      "structuredDataPlan": {
         "enabled": True,
         "schema": {
            "type": "object",
            "properties": {
               "follow_up": { 
                  "type": "boolean" 
               },
               "preferred_contact": {
                  "type": "string",
                  "enum": ["phone", "email", "NA"]
               },
               "phone_contact": { 
                  "type": "string" 
               },
               "email_contact": {
                  "type": "string"
               }
            },
            "required": ["follow_up", "preferred_contact", "phone_contact", "email_contact"]
         }
      }
   },
   "messagePlan": {
      "idleMessages": agent_idle_phrases,
      "idleMessageMaxSpokenCount": 3,
      "idleMessageResetCountOnUserSpeechEnabled": False,
      "idleTimeoutSeconds": 10,
      "silenceTimeoutMessage": agent_silence_message
   }
}
