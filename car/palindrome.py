from car.car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car):
    def __init__(self, warning_light_on, last_service_date):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        super().__init__("Palindrome", engine, battery)
