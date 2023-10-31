from datetime import date
import sys

import numpy as np


class VisitSensor:
    """
    Simulates a sensor at the entrance of a mall.
    Takes a mean and a standard deviation
    and returns the number of visitors that passed through
    a particular door on a given date
    """
    def __init__(self, avg_visit: int, std_visit: int) -> None:
        """Intialize sensor"""
        self.avg_visit = avg_visit
        self.std_visit = std_visit

    def simulate_visit(self, business_date: date) -> int:
        """Simulate the number of person detected by the sensor
        during the day"""

        # Ensure reproducibility of measurements
        np.random.seed(seed=business_date.toordinal())

        # Find out which day the business_date corresponds to: Monday = 0, Sunday = 6
        week_day = business_date.weekday()


        visit = np.random.normal(self.avg_visit, self.std_visit)
        # More traffic on Wednesdays (2), Fridays (4) and Saturdays (5)
        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.25
        if week_day == 5:
            visit *= 1.35

        # If the business_date is a sunday the store is closed
        if week_day == 6:
            visit = -1

        # Return an integer
        return np.floor(visit)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day = 2023, 10, 25
    queried_date = date(year, month, day)

    capteur = VisitSensor(1500, 150)
    print(capteur.simulate_visit(queried_date))
