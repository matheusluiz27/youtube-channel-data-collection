class Channel:
    def __init__(self, id, title, description, url, keyword, image_base64):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.keyword = keyword
        self.image_base64 = image_base64

    def __str__(self):
        return 'id: ' + self.id + '\ntitle: ' + self.title + '\ndescription: ' + self.description + '\nurl: ' + self.url + '\nkeyword: ' + self.keyword
