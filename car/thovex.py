from car.car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery

class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__("Thovex", CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))

