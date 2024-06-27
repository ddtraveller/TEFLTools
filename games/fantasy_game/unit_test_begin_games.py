import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the Python path so we can import begin_game and Navigation
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import begin_game
import Navigation

class TestBeginGame(unittest.TestCase):

    def test_function_existence(self):
        """Test that all expected functions exist in the begin_game module."""
        expected_functions = [
            'get_location_description',
            'select_initial_encounter',
            'weighted_choice',
            'get_llm_response',
            'get_llm_decision',
            'encounter',
            'load_character',
            'main'
        ]

        for func_name in expected_functions:
            self.assertTrue(hasattr(begin_game, func_name), f"Function '{func_name}' not found in begin_game module")

    @patch('begin_game.open', new_callable=unittest.mock.mock_open, read_data='Location,Description\nTest Location,A test description')
    def test_get_location_description(self, mock_file):
        """Test that get_location_description function exists and returns a string."""
        description = begin_game.get_location_description("Test Location")
        self.assertEqual(description, "A test description")

    @patch('json.load')
    @patch('begin_game.open', new_callable=unittest.mock.mock_open)
    def test_select_initial_encounter(self, mock_file, mock_json_load):
        """Test that select_initial_encounter function exists and returns a tuple."""
        mock_json_load.return_value = [{"name": "Test Monster", "level": 1, "locations": ["Test Location"], "armor_class": 10}]
        monster, location = begin_game.select_initial_encounter()
        self.assertIsInstance(monster, dict)
        self.assertIsInstance(location, str)

    def test_weighted_choice(self):
        """Test that weighted_choice function exists and returns a value."""
        weights = {'A': 0.5, 'B': 0.3, 'C': 0.2}
        choice = begin_game.weighted_choice(weights)
        self.assertIn(choice, weights.keys())

    @patch('begin_game.client.messages.create')
    def test_get_llm_response(self, mock_create):
        """Test that get_llm_response function exists and returns a string."""
        mock_create.return_value.content = [MagicMock(text="Test response")]
        response = begin_game.get_llm_response([{"role": "user", "content": "Test"}])
        self.assertEqual(response, "Test response")

    @patch('begin_game.get_llm_response')
    def test_get_llm_decision(self, mock_llm_response):
        """Test that get_llm_decision function exists and returns a string."""
        mock_llm_response.return_value = "Decision: Combat\nExplanation: Test\nNext Action: Test"
        character_data = {"name": "Test Character", "level": 1, "class": "Warrior"}
        monster_data = {"name": "Test Monster"}
        conversation_history = ["Player: Hello", "Monster: Greetings", "Player: Die!"]
        decision = begin_game.get_llm_decision(character_data, monster_data, conversation_history)
        self.assertIn("Decision: Combat", decision)

        # Test with empty conversation history
        decision = begin_game.get_llm_decision(character_data, monster_data, [])
        self.assertIn("Decision: Combat", decision)

    @patch('begin_game.combat')
    @patch('begin_game.get_llm_response')
    @patch('begin_game.get_llm_decision')
    def test_encounter(self, mock_llm_decision, mock_llm_response, mock_combat):
        """Test that encounter function exists and handles different scenarios."""
        mock_llm_response.return_value = "Monster response"
        mock_llm_decision.return_value = "Decision: Combat\nExplanation: Test\nNext Action: Test"
        mock_combat.return_value = True

        character_data = {
            "name": "Test Character",
            "level": 1,
            "class": "Warrior"
        }
        monster_data = {
            "name": "Test Monster",
            "long_description": "A test monster",
            "dialogue": ["Friendly"]
        }

        with patch('builtins.input', side_effect=['1', 'Hello', '3']):
            result = begin_game.encounter(character_data, monster_data, "Test Location", "test.csv", 50)
            self.assertTrue(result)

    @patch('os.listdir')
    @patch('json.load')
    @patch('begin_game.open', new_callable=unittest.mock.mock_open)
    def test_load_character(self, mock_file, mock_json_load, mock_listdir):
        """Test that load_character function exists and returns a dict or None."""
        mock_listdir.return_value = ['test_character.json']
        mock_json_load.return_value = {"name": "Test Character"}
        character = begin_game.load_character("Test")
        self.assertEqual(character, {"name": "Test Character"})

        mock_listdir.return_value = []
        character = begin_game.load_character("Nonexistent")
        self.assertIsNone(character)

class TestNavigation(unittest.TestCase):

    def test_function_existence(self):
        """Test that all expected functions exist in the Navigation module."""
        expected_functions = [
            'haversine',
            'load_locations',
            'get_nearby_locations',
            'find_starting_location',
            'navigate',
            'start_navigation'
        ]

        for func_name in expected_functions:
            self.assertTrue(hasattr(Navigation, func_name), f"Function '{func_name}' not found in Navigation module")

    def test_haversine(self):
        """Test that haversine function calculates distances correctly."""
        distance = Navigation.haversine(0, 0, 1, 1, 0, 0)
        self.assertAlmostEqual(distance, 157.2, places=1)

    @patch('pandas.read_csv')
    def test_load_locations(self, mock_read_csv):
        """Test that load_locations function loads data correctly."""
        mock_read_csv.return_value = MagicMock()
        locations = Navigation.load_locations("test.csv")
        self.assertIsNotNone(locations)

    @patch('Navigation.load_locations')
    @patch('Navigation.find_starting_location')
    @patch('Navigation.navigate')
    @patch('begin_game.select_initial_encounter')
    @patch('begin_game.encounter')
    @patch('random.random')
    def test_start_navigation(self, mock_random, mock_encounter, mock_select_encounter, mock_navigate, mock_find_starting, mock_load_locations):
        """Test that start_navigation function starts the navigation process."""
        mock_load_locations.return_value = MagicMock()
        mock_find_starting.return_value = {"name": "Starting Location"}
        mock_navigate.side_effect = [{"name": "Next Location"}, None]
        mock_select_encounter.return_value = ({"name": "Test Monster"}, "Test Location")
        mock_encounter.return_value = True
        mock_random.return_value = 0.4  # Ensure an encounter happens
        
        Navigation.start_navigation("test.csv", 50, {"name": "Test Character"})
        
        self.assertTrue(mock_navigate.called)
        self.assertTrue(mock_encounter.called)

if __name__ == '__main__':
    unittest.main()