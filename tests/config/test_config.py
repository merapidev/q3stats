import os
import unittest

from config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.fixture_directory = os.path.abspath("tests/config/fixtures")

    def test_expect_exception_when_config_file_does_not_exits(self):
        expected_file_location = os.path.join(self.fixture_directory, "not_existing.yml")

        try:
            config = Config(filename=expected_file_location)
        except FileNotFoundError:
            self.assertTrue(True)

    def test_expect_mongodb_configuration(self):
        expected_file_location = os.path.join(self.fixture_directory, "config.yml")

        config = Config(filename=expected_file_location)

        self.assertEqual('localhost', config.mongodb['host'])
        self.assertEqual(27017, config.mongodb['port'])
        self.assertEqual('q3stat', config.mongodb['db'])

    def test_expect_files_directory_configuration(self):
        expected_file_location = os.path.join(self.fixture_directory, "config.yml")

        config = Config(filename=expected_file_location)

        self.assertEqual('files/', config.files_directory)
