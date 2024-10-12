import unittest
from bot.weather import get_weather


class TestWeather(unittest.TestCase):

    def test_get_weather_valid_city(self):
        response = get_weather("Moscow")
        self.assertEqual(response['name'], "Moscow")
        self.assertIn('main', response)

    def test_get_weather_invalid_city(self):
        response = get_weather("InvalidCity")
        self.assertEqual(response['cod'], '404')


if __name__ == '__main__':
    unittest.main()
