from car.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        super().__init__("Glissade", engine, battery)
