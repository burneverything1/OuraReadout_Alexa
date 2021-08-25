import requests
import currentday

payload={'access_token': 'VXF4W6JLKPQUKTYKEYW3JFCL4UKKGHQN'}

def get_sleep_score():
  response = requests.get('https://api.ouraring.com/v1/sleep', params=payload).json()
  sleepscore = response['sleep'][0]['score']
  print()
  return sleepscore

def 