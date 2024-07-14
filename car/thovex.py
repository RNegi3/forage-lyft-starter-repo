from car.Cars import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from tires.carriganTires import CarriganTires

class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = CarriganTires(tire_wear_array)
        super().__init__(engine, battery, tires)