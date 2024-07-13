from car.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        super().__init__("Rorschach", engine, battery)
