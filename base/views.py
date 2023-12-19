import requests as req
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.core.exceptions import ObjectDoesNotExist
from .models import DiscordServer
from .constants import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET, API_ENDPOINT


def get_code(request):
    data = {key: val[0] for key, val in {**request.GET}.items()}
    return data


def get_Token(request):
    server_info = get_code(request)
    data = {
        'grant_type': 'authorization_code',
        'code': server_info['code'],
        'redirect_uri': REDIRECT_URI,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    res = req.post('%s/oauth2/token' % API_ENDPOINT,
                   data=data, headers=headers,
                   auth=(CLIENT_ID, CLIENT_SECRET))
    try:
        res.raise_for_status()
        try:
            token_info = res.json()
        except ValueError as v:
            raise Exception(v)
        try:
            server, created = DiscordServer.objects.get_or_create(server_id=server_info['guild_id'])

            server.server_id = server_info['guild_id']
            server.auth_code = server_info['code']
            server.auth_token = token_info['access_token']
            server.save()

        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("Discord Server Does not Exist")

        # return JSONResponse({'token':server_info['token']})
        return HttpResponse('Get the token')

    except req.exceptions.HTTPError as err:
        return HttpResponse(err)


# @require_GET
# def sendToken(request):
#     bot = DiscordServer.objects.all()
#     print(bot)
#     return JsonResponse({'token':bot[0].auth_token})
    