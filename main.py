from channel_repository import ChannelRepository
from youtube_api_service import YoutubeAPIService


def main():
    youtube_api_service = YoutubeAPIService()
    channel_repository = ChannelRepository()

    keywords = ['tempest', 'youtube', 'estrela']
    max_results_per_keyword = 3

    youtube_channels_data = []

    for keyword in keywords:
        youtube_channels_data.extend(youtube_api_service.get_channels(keyword, max_results_per_keyword))

    for channel_data in youtube_channels_data:
        channel_repository.save_channel(channel_data)
        print(channel_data)


if __name__ == '__main__':
    main()

