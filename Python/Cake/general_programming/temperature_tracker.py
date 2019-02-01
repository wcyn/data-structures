# https://www.interviewcake.com/question/python/temperature-tracker?course=fc1&section=general-programming
# You decide to test if your oddly-mathematical heating
# company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.
#
# Write a class TempTracker with these methods:
#
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean ↴ of all temps we've seen so far
# get_mode()—returns a mode ↴ of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods get_max(),
# get_min(), get_mean(), and get_mode() over speeding up the insert() method.
#
# get_mean() should return a float, but the rest of the getter methods can return integers.
# Temperatures will all be inserted as integers.
# We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.
#
# If there is more than one mode, return any of the modes.
import unittest


class TempTracker:
    _lowest_temperature = 0
    _highest_temperature = 110

    def __init__(self):
        self.temperature_occurrences = [0] * ((self._highest_temperature - self._lowest_temperature) + 1)
        self.total_count = 0
        self.minimum_temperature = self._highest_temperature + 1
        self.maximum_temperature = self._lowest_temperature - 1
        self.max_occurrences = 0
        self.mode_temperature = 0
        self.cumulative_temperature = 0

    def insert(self, value):
        if self._lowest_temperature <= value <= self._highest_temperature:
            self.temperature_occurrences[value] += 1
            if self.temperature_occurrences[value] > self.max_occurrences:
                self.mode_temperature = value
                self.max_occurrences = self.temperature_occurrences[value]

            self.total_count += 1
            self.cumulative_temperature += value
            self.minimum_temperature = min(self.minimum_temperature, value)
            self.maximum_temperature = max(self.maximum_temperature, value)
        else:
            raise Exception("Temperature out of valid range")

    def _temperatures_available(self):
        if self.total_count < 1:
            print("No temperatures recorded yet")
            return False
        return True

    def get_max(self):
        if self._temperatures_available():
            return self.maximum_temperature

    def get_min(self):
        if self._temperatures_available():
            return self.minimum_temperature

    def get_mean(self):
        if self._temperatures_available():
            return self.cumulative_temperature / self.total_count

    def get_mode(self):
        if self._temperatures_available():
            return self.mode_temperature


class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)

