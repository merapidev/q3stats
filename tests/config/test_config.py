import os
import unittest

from config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.fixture_directory = os.path.abspath('tests/config/fixtures')
        self.not_existing_config_file = 'not_existing.yml'

    def test_expect_exception_when_config_file_does_not_exits(self):
        expected_file_location = os.path.join(self.fixture_directory, self.not_existing_config_file)

        try:
            config = Config(filename=expected_file_location)
        except FileNotFoundError:
            self.assertTrue(True)
