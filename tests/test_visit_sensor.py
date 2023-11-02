import unittest
from datetime import date

from fake_data_app.sensor import VisitSensor


class TestVisitSensor(unittest.TestCase):
    def test_weekdays_open(self):
        for test_day in range(11, 17):
            with self.subTest(i=test_day):
                visit_sensor = VisitSensor(1200, 300)
                visit_count = visit_sensor.simulate_visit_count(date(2023, 9, test_day))
                self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2023, 9, 17))
        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(1200, 300, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(2023, 10, 22))
        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        visit_sensor = VisitSensor(1200, 300, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(2023, 11, 28))
        self.assertEqual(visit_count, 238)


if __name__ == "__main__":
    unittest.main()
