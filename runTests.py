import unittest
from stringUtils import StringUtils as su

class TestStringUtils(unittest.TestCase):
    def test_concatenate(self):
        self.assertEqual(su.concatenate("James", "Richmond"), "JamesRichmond")

    def test_extract_substring(self):
        self.assertEqual(su.extract_substring("Rocky Mountain Reserve", 6, 14), "Mountain")

    def test_capitalize(self):
        self.assertEqual(su.capitalize("clickup"), "Clickup")

if __name__ == "__main__":
    unittest.main()