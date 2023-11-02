import unittest
from datetime import date

from fake_data_app.store import StoreSensor


class TestStore(unittest.TestCase):
    def test_get_all_traffic(self):
        lille_store = StoreSensor("Lille", 1200, 300)
        visits = lille_store.get_all_traffic(date(2023, 9, 13))
        self.assertEqual(visits, 758)

    def test_get_sensor_traffic(self):
        lille_store = StoreSensor("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 13))
        self.assertEqual(visits, 15)

    def test_sunday_closed(self):
        lille_store = StoreSensor("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 17))
        self.assertEqual(visits, -1)


if __name__ == "__main__":
    unittest.main()
