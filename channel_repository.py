import sqlite3

from channel import Channel


class ChannelRepository:
    def __init__(self):
        self.database = sqlite3.connect('youtube_channel_data.bd')
        self.cursor = self.database.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS channel (title TEXT, description TEXT, id TEXT, url TEXT, imageBase64 TEXT, keyword TEXT)")

    def save_channel(self, channel: Channel):
        self.cursor.execute("INSERT INTO channel (title, description, id, url, imageBase64, keyword) "
                            "VALUES (?, ?, ?, ?, ?, ?)", (channel.title, channel.description, channel.id, channel.url, channel.image_base64, channel.keyword))

        self.database.commit()
