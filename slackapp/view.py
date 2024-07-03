import os
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
import requests
import os
import requests
from django.http import HttpResponse
from django.conf import settings

def create_channel(request):


    # API endpoint for creating channels
    url = 'https://slack.com/api/conversations.create'

    # Channel name and other parameters
    channel_name = 'heloqqqqqqqqqqqq'
    is_private = False  # Set to True for private channels

    # Payload for the API request
    data = {
        # 'token': slack_token,
        'name': channel_name,
        'is_private': is_private
    }

    # Send the request
    response = requests.post(url, data=data)
    print(response)
    # Check if the request was successful
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
        response_data = response.json()

        if response_data['ok']:
            print(f"Channel '{channel_name}' created successfully.")
            return HttpResponse('channel create sucessfully')

        else:
            print(f"Failed to create channel: {response_data['error']}")
            return HttpResponse('channel create failed')

    else:
        print(f"Failed to create channel. Status code: {response.status_code}")
        return HttpResponse('Responce is not 200')




def login(request):
    print("9")
    print(settings.SLACK_REDIRECT_URI)
    print("11")

    client_id = settings.SLACK_CLIENT_ID
    redirect_uri = settings.SLACK_REDIRECT_URI
    
    return redirect(
f'https://slack.com/oauth/v2/authorize?client_id={client_id}&scope=channels:manage,chat:write,channels:read,incoming-webhook&redirect_uri={redirect_uri}'
    )


def oauth_callback(request):
    code = request.GET.get('code')
    client_id = settings.SLACK_CLIENT_ID
    client_secret = settings.SLACK_CLIENT_SECRET
    redirect_uri = settings.SLACK_REDIRECT_URI

    response = requests.post('https://slack.com/api/oauth.v2.access', data={
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri
    })

    response_data = response.json()
    access_token = response_data.get('access_token')

    if access_token:
        # Save the access token in the session
        request.session['access_token'] = access_token
        return HttpResponse('Authentication successful! You can now use the Slack API.')
    else:
        return HttpResponse('Authentication failed.')
