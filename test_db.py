import unittest

from main import search_player_name
# These tests don't work, I think because of the input required...
# But at least I tried!!!

class SearchTests(unittest.TestCase):

    def test_search_by_player_name_if_correct_name_is_given(self):
        self.assertEqual(search_player_name()("MMitchell"), "MMitchell")

    def test_search_by_player_name_if_incorrect_name_is_given(self):
        self.assertEqual(search_player_name()("asdf"), "Sorry no player by that name was found.")

