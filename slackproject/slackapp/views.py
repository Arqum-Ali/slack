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
def create_channelffffffffffffffffffffffff(request):

    # Replace with your Slack API token


    # API endpoint for creating channels
    url = 'https://slack.com/api/conversations.create'

    # Channel name and other parameters
    channel_name = 'heloqqqqqqqqqqqq'
    is_private = False  # Set to True for private channels

    # Payload for the API request
    data = {
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






def list_channels(request):
    slack_token = 'hello'
    url = 'https://slack.com/api/conversations.list'
    headers = {
        'Authorization': f'Bearer {slack_token}'
    }
    params = {
        'limit': 1000  # You can adjust the limit based on your requirements
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()
        if response_data['ok']:
            channels = response_data['channels']
            channel_list = []
            for channel in channels:
                channel_info = {
                    'id': channel['id'],
                    'name': channel['name']
                }
                channel_list.append(channel_info)
                print(f"Channel Name: {channel['name']}, Channel ID: {channel['id']}")
            return HttpResponse(channel_list)
        else:
            print(f"Failed to fetch channels: {response_data['error']}")
            return HttpResponse(f"Failed to fetch channels: {response_data['error']}", status=400)
    else:
        print(f"Failed to fetch channels. Status code: {response.status_code}")
        return HttpResponse(f"Failed to fetch channels. Status code: {response.status_code}", status=400)



def add_channel_member(request):
    # Replace with your actual Slack OAuth token, channel ID, and user ID
    slack_token = 'hello'
    channel_id = 'C07BDPPD0EL'
    user_id = 'U079PJZABFH'

    url = 'https://slack.com/api/conversations.invite'
    headers = {
        'Authorization': f'Bearer {slack_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'channel': channel_id,
        'users': user_id
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        if response_data['ok']:
            print(f"Successfully added user {user_id} to channel {channel_id}.")
            return HttpResponse("member added sucessfully")
        else:
            print(f"Failed to add user: {response_data['error']}")
            return HttpResponse(f"Failed to add user: {response_data['error']}")

    else:
        print(f"Failed to add user. Status code: {response.status_code}")
        return HttpResponse(f"Failed to invite the member in a channels. Status code: {response.status_code}", status=400)








def remove_channel_member(request):
    
    # Replace with your actual Slack OAuth token, channel ID, and user ID
    slack_token = 'hello'
    channel_id = 'C07BDPPD0EL'
    user_id = 'U079PJZABFH'

    url = 'https://slack.com/api/conversations.kick'
    headers = {
        'Authorization': f'Bearer {slack_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'channel': channel_id,
        'user': user_id
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        if response_data['ok']:
            print(f"Successfully removed user {user_id} from channel {channel_id}.")
            return HttpResponse(f"Successfully removed user {user_id} from channel {channel_id}.", status=400)

        else:
            print(f"Failed to remove user: {response_data['error']}")
            return HttpResponse(f"Failed to remove user: {response_data['error']}", status=400)

    else:
        print(f"Failed to remove user. Status code: {response.status_code}")
        return HttpResponse(f"Failed to remove user Status code: {response.status_code}", status=400)








import requests

def get_channel_members(request):
        # Replace with your actual Slack OAuth token and channel ID
    slack_token = 'hello'
    channel_id = 'C07BDPPD0EL'


    members_url = f'https://slack.com/api/conversations.members?channel={channel_id}'
    headers = {
        'Authorization': f'Bearer {slack_token}'
    }

    response = requests.get(members_url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if response_data['ok']:
            member_ids = response_data['members']
            member_info_list = []

            for member_id in member_ids:
                user_info_url = f'https://slack.com/api/users.info?user={member_id}'
                user_response = requests.get(user_info_url, headers=headers)

                if user_response.status_code == 200:
                    user_data = user_response.json()
                    if user_data['ok']:
                        member_info = {
                            'id': member_id,
                            'name': user_data['user']['name']
                        }
                        member_info_list.append(member_info)
                    else:
                        print(f"Failed to fetch user info for {member_id}: {user_data['error']}")
                else:
                    print(f"Failed to fetch user info for {member_id}. Status code: {user_response.status_code}")

            for member in member_info_list:
                print(f"User ID: {member['id']}, User Name: {member['name']}")
            return HttpResponse(member_info_list)

        else:
            print(f"Failed to fetch members: {response_data['error']}")
            return HttpResponse(f"Failed to fetch members.Status code: {response.status_code}", status=400)
    else:
        print(f"Failed to fetch members.not the 200 code Status code: {response.status_code}")
        return HttpResponse(f"Failed to fetch members.Status code: {response.status_code}", status=400)



















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
