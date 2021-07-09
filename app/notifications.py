import json
import os
import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'ZTP Server'
}
data = {}

def viaSlack(msg):
    slack_token = 'mySlacToken'
    url = 'https://hooks.slack.com/services/' + slack_token
    data['text'] = msg
    requests.post(url, headers=headers, data=json.dumps(data))

def viaTeams(msg):
    # You must create the connectorcard object with the Microsoft Webhook URL
    myTeamsMessage = connectorcard("teamsWebHookUrl")
    # Add text to the message.
    myTeamsMessage.text(msg)
    # send the message.
    myTeamsMessage.send()
