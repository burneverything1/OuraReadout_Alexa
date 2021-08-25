from flask import Flask
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter
import intents
import requests


# Register the intents with the SkillBuilder. Intents are defined in intents.py.
# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers in intents.py. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()
sb.add_request_handler(intents.LaunchRequestHandler())
sb.add_request_handler(intents.HelpIntentHandler())
sb.add_request_handler(intents.CancelOrStopIntentHandler())
sb.add_request_handler(intents.HelloWorldIntentHandler())
sb.add_request_handler(intents.SessionEndedRequestHandler())
sb.add_request_handler(intents.GetOuraStats())
sb.add_request_handler(intents.IntentReflectorHandler()) # Register this intent last!

app = Flask(__name__)
skill_id = 'amzn1.ask.skill.21168df6-6607-4181-a8cb-9c202e36a40e'
Oura_PAT = 'VXF4W6JLKPQUKTYKEYW3JFCL4UKKGHQN'

skill_adapter = SkillAdapter(
  skill=sb.create(), 
  skill_id=skill_id, app=app
  )

@app.route("/", methods=["GET", "POST"])
def invoke_skill():
    return skill_adapter.dispatch_request()

@app.route("/ouratest", methods=["GET"])
def test_oura():
  payload={'access_token': 'VXF4W6JLKPQUKTYKEYW3JFCL4UKKGHQN'}
  response = requests.get('https://api.ouraring.com/v1/sleep', params=payload)
  app.logger.info(response.content)
  app.logger.info(response.url)
  print(response.content)
  print(response.url)
  return "ouratest"

app.run('0.0.0.0', port=443)