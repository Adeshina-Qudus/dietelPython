from typing import List, Any

from DiaryApp.Entry import Entry
from DiaryApp.Exception.EmptyTitle import EmptyTitle
from DiaryApp.Exception.InvalidID import InvalidID
from DiaryApp.Exception.incorrect_password import IncorrectPasswordException


class Diary:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.number_of_entries = 0

    def is_Locked(self):
        return self.is_locked

    def un_LockDiary(self, param):
        self.validate_password(param)
        if self.password == param:
            self.is_locked = False

    def validate_password(self, password):
        if self.password != password:
            raise IncorrectPasswordException("Invalid Password")

    def lockDiary(self):
        self.is_locked = True

    def createEntry(self, title, body):
        self.validate_title(title)
        self.number_of_entries += 1
        id = self.generateID()
        entry = Entry(id, title, body)
        self.entries.append(entry)

    def validate_title(self, title):
        if len(title) == 0:
            raise EmptyTitle("Title cannot be empty")

    def generateID(self):
        return self.number_of_entries

    def numbers_of_Entry(self):
        return self.number_of_entries

    def findEntryByID(self, id):
        for entry in self.entries:
            if entry.getId() == id:
                return entry
        raise InvalidID("Id does not exist")

    def deleteEntry(self, id):
        myEntry: Entry = self.findEntryByID(id)
        self.entries.remove(myEntry)
        self.number_of_entries -= 1

    def updateEntry(self, id, title, body):
        entry: Entry = self.findEntryByID(id)
        self.validate_title(title)
        entry.setTitle(title)
        concat = entry.getBody() + " " + body
        entry.setBody(concat)

    def getUsername(self):
        return self.username

