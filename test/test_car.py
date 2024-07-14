import unittest
from datetime import datetime, timedelta
from car.calliope import Calliope
from car.glissade import Glissade
from car.palindrome import Palindrome
from car.rorschach import Rorschach
from car.thovex import Thovex

class TestCar(unittest.TestCase):
    def test_calliope(self):
        current_mileage = 35000
        last_service_mileage = 0
        last_service_date = datetime.today().date() - timedelta(days=365*4)  
        tire_wear_array = [0.8, 0.7, 0.6, 0.9]  
        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_wear_array)
        self.assertTrue(car.needs_service())  

    def test_glissade(self):
        current_mileage = 65000
        last_service_mileage = 0
        last_service_date = datetime.today().date() - timedelta(days=365*4)  
        tire_wear_array = [0.8, 0.7, 0.6, 0.9]  
        car = Glissade(current_mileage, last_service_mileage, last_service_date, tire_wear_array)
        self.assertTrue(car.needs_service())  

    def test_palindrome(self):
        warning_light_is_on = True  # Engine needs service
        last_service_date = datetime.today().date() - timedelta(days=365*4)
        tire_wear_array = [0.8, 0.7, 0.6, 0.5] 
        car = Palindrome(warning_light_is_on, last_service_date, tire_wear_array)
        self.assertTrue(car.needs_service())

    def test_rorschach(self):
        current_mileage = 75000
        last_service_mileage = 0
        last_service_date = datetime.today().date() - timedelta(days=365*4)  
        tire_wear_array = [0.8, 0.7, 0.6, 0.9]  
        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_wear_array)
        self.assertTrue(car.needs_service())  

    def test_thovex(self):
        current_mileage = 85000
        last_service_mileage = 0
        last_service_date = datetime.today().date() - timedelta(days=365*4)  
        tire_wear_array = [0.8, 0.7, 0.6, 0.9]  
        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_wear_array)
        self.assertTrue(car.needs_service())  

if __name__ == '__main__':
    unittest.main()
