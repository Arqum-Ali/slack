import os
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    print("9")
    print(settings.SLACK_REDIRECT_URI)
    print("11")

    client_id = settings.SLACK_CLIENT_ID
    redirect_uri = settings.SLACK_REDIRECT_URI
    
    return redirect(
f'https://slack.com/oauth/v2/authorize?client_id={client_id}&scope=channels:manage,channels:read,channels:write,channels:history,channels:join,chat:write,incoming-webhook,users:read&redirect_uri={redirect_uri}'
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
