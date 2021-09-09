import unittest
from DataUtil import DataUtil as DUtil


class TestComponent(unittest.TestCase):
    def test_get_temperature(self):
        """
        test if api is working correctly
        """
        self.assertIsInstance(
            DUtil.get_temperature_from_city_name("DUBLIN"), float)
        self.assertIsNone(
            DUtil.get_temperature_from_city_name("Fultter"))

    def test_get_note(self):
        """
        test if a function which decide note is working correctly
        """
        self.assertEqual(DUtil.get_note_from_temperature(4), "so cold")
        self.assertEqual(DUtil.get_note_from_temperature(26),
                         "let's go for a pint")
        self.assertEqual(DUtil.get_note_from_temperature(11), "normal")
        x = ['09.09.2021', '06:35', 'TEL AVIV',
             '3V 4848\nairborne', '', '', '', '', '']


if __name__ == '__main__':
    unittest.main()
