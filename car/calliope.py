from car.car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__("Calliope", CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))
