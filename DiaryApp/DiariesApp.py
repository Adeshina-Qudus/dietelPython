from DiaryApp.DiaryApp import Diary
from DiaryApp.Exception.InvalidUsername import InvalidUsername


class Diaries:

    def __init__(self):
        self.diaries = []
        self.diariesNumber = 0

    def addNew(self, username, password):
        self.diariesNumber += 1
        diary = Diary(username, password)
        self.diaries.append(diary)

    def numberOfDiaries(self):
        return self.diariesNumber

    def findByUsername(self, username):
        for diary in self.diaries:
            if diary.getUsername() == username:
                return diary
            else:
                raise InvalidUsername("username does not exist")
