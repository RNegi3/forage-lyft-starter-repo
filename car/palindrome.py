from car.car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car):
    def __init__(self, warning_light_is_on, last_service_date):
        super().__init__("Palindrome", SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date))
