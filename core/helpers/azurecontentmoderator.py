import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from feed.settings.base import AZURE_CONTENT_MODERATOR_KEY


'''
Takes a post body, and returns a JSON representation processed by Azure Content Moderator
'''
def content_moderator_json(text):
    if AZURE_CONTENT_MODERATOR_KEY is None:
        raise EnvironmentError("Azure Key Not Found")

    headers = {
        # Request headers
        'Content-Type': 'text/plain',
        'Ocp-Apim-Subscription-Key': AZURE_CONTENT_MODERATOR_KEY,
    }

    params = urllib.parse.urlencode({
        'autocorrect': 'False',   # No autocorrection
        'PII': 'True',            # Detect personal information
        # 'listId': '{string}',   # Not using custom term lists
        'classify': 'True',       # Enable Text Classification
        # 'language': '{string}', # Defaults to English
    })

    try:
        conn = http.client.HTTPSConnection('australiaeast.api.cognitive.microsoft.com')
        conn.request("POST", "/contentmoderator/moderate/v1.0/ProcessText/Screen?%s" % params, text, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data

    except Exception as e:
        raise e


def content_moderator(text):
    response = content_moderator_json(text)
    json_response = json.loads(response)
    print(json_response)
    print(json_response['Classification'])