from unittest import TestCase
from DiaryApp.DiariesApp import Diaries
from DiaryApp.DiaryApp import Diary


class TestDiaries(TestCase):
    def test_newDiaryAdded(self):
        diaries = Diaries()
        diaries.addNew("qudus","1234")
        self.assertEqual(1,diaries.numberOfDiaries())

    def test_findByUserName(self):
        diaries = Diaries()
        diaries.addNew("qudus", "1234")
        diary : Diary = diaries.findByUsername("qudus")
        self.assertEqual("qudus",diary.getUsername())

    def test_findByWrongUsername(self):
        diaries = Diaries()
        diaries.addNew("qudus", "1234")
        diary: Diary = diaries.findByUsername("aishat")
        with self.assertRaises(InvalidUsername):
            diary.getUsername()
