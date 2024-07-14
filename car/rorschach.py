from car.Cars import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from tires.octoprimeTires import OctoprimeTires

class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tire_wear_array)
        super().__init__(engine, battery, tires)