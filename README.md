# Oura Readout
Based on the Replexa, the Alexa Skills template from Replit. Built for the Replit Summer Hackathon 2021.

This uses the Oura Ring API to get the latest Sleep, Activity, and Readiness scores from Tim Lee's Oura Ring, and compares it to the previous 3 day average. This summary is then read out by Alexa.

Checkout what is read out by Alexa with this test request here: https://ourareadoutalexa.burneverything1.repl.co/ouratest

### For Your Use
If you'd like to use this for yourself, replace 'skill_id' in main.py with the Alexa Skill Id and the 'access_token' in oura.py with your Oura Ring PAT ('Personal Access Token').

### Alexa Commands
"oura ring"
"get my ring stats"