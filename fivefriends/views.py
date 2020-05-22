from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        template = "fivefriends/home.html"
        request_url = 'https://api.vk.com/method/{}'

        # try:
        vk_user = request.user.social_auth.get(provider ='vk-oauth2')
        access_token = vk_user.extra_data['access_token']

        friends_request = requests.get(
            request_url.format('friends.get'),
            params={
                'order': 'hints',
                'count': 5,
                'fields': 'items',
                'v': 5.52,
                'access_token': access_token
            }
        )
        friends_response = friends_request.json()
        items = friends_response['response']['items']
        friends_data = []
        for i in items:
            friends_data.append('{} {}'.format(i['first_name'], i['last_name']))
        return render(request, template, context={'friends': friends_data})
        # except:
            # return redirect('login/')
