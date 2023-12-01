from unittest import TestCase
from DiaryApp.DiaryApp import Diary
from DiaryApp.Entry import Entry
from DiaryApp.Exception.InvalidID import InvalidID
from DiaryApp.Exception.incorrect_password import IncorrectPasswordException


class TestDiary(TestCase):
    def test_diary_is_locked(self):
        my_diary = Diary("jumoke", "pin")
        self.assertTrue(my_diary.is_Locked())

    def test_diary_is_locked_andUnlockDiary_withCorrectPassword(self):
        my_diary = Diary("jumoke", "pin")
        self.assertTrue(my_diary.is_Locked())
        my_diary.un_LockDiary("pin")
        self.assertFalse(my_diary.is_Locked())

    def test_diaryIsLocked_andUnlockDiary_withIncorrectPassword(self):
        my_diary = Diary("jumoke", "pin")
        self.assertTrue(my_diary.is_Locked())
        with self.assertRaises(IncorrectPasswordException):
            my_diary.un_LockDiary("wrong pin")

    def test_diaryIsUnLocked_withCorrectPassword_andLockDiary(self):
        my_diary = Diary("jumoke", "pin")
        self.assertTrue(my_diary.is_Locked())
        my_diary.un_LockDiary("pin")
        my_diary.lockDiary()
        self.assertTrue(my_diary.is_Locked())

    def test_createDiaryEntry(self):
        my_diary = Diary("jumoke", "pin")
        self.assertTrue(my_diary.is_Locked())
        my_diary.un_LockDiary("pin")
        my_diary.createEntry("my love life ", "ohhh it's crazy")
        self.assertEqual(1, my_diary.numbers_of_Entry())

    def test_findDiaryEntryById(self):
        my_diary = Diary("jumoke", "pin")
        my_diary.createEntry("my love life", "heart broken")
        my_diary.createEntry("my love life part 2", "heart broken again")
        entry: Entry = my_diary.findEntryByID(1)
        entry2: Entry = my_diary.findEntryByID(2)
        self.assertEqual(1, entry.getId())
        self.assertEqual(2, entry2.getId())

    def test_findEntryWithWrongID(self):
        my_diary = Diary("jumoke", "pin")
        my_diary.createEntry("my love life", "heart broken")
        my_diary.createEntry("my love life part 2", "heart broken again")
        with self.assertRaises(InvalidID):
            my_diary.findEntryByID(4)

