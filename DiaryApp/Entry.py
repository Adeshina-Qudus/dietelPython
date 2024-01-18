class Entry:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body

    def getId(self):
        return self.id

    def setTitle(self, title):
        self.title = title

    def getBody(self):
        return self.body

    def setBody(self, concat):
        self.body = concat
