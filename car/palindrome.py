from car.Cars import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from tires.carriganTires import CarriganTires

class Palindrome(Car):
    def __init__(self, warning_light_is_on, last_service_date, tire_wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear_array)
        super().__init__(engine, battery, tires)