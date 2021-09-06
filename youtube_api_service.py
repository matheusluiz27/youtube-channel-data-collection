import requests

from channel import Channel


def convert_response_json_item_to_channel(response_item, keyword):
    snippet = response_item['snippet']
    title = snippet['title']
    description = snippet['description']
    channel_id = snippet['channelId']
    channel_url = 'youtube.com/channel/' + channel_id
    thumbnail_url = snippet['thumbnails']['default']['url']
    image_base64 = requests.get(thumbnail_url).content

    return Channel(channel_id, title, description, channel_url, keyword, image_base64)


class YoutubeAPIService:
    def __init__(self):
        self.kei_api = 'AIzaSyAExwTx36ca32Z4m-PhDlw0ahlQ4GYWDQ4'

    def get_channels(self, keyword, max_results):
        channels = []

        payload = {'key': self.kei_api, 'part': 'snippet', 'q': keyword, 'type': 'channel', 'maxResults': max_results}
        response = requests.get('https://youtube.googleapis.com/youtube/v3/search', params=payload)

        items = response.json()['items']
        for item in items:
            channels.append(convert_response_json_item_to_channel(item, keyword))

        return channels
