import unittest
from datetime import datetime, timedelta

from car.calliope import Calliope
from car.glissade import Glissade
from car.palindrome import Palindrome
from car.rorschach import Rorschach
from car.thovex import Thovex


class TestCar(unittest.TestCase):
    def test_callipse(self):
        # Engine needs service?
        calliope = Calliope(current_mileage=35000, last_service_mileage=0, last_service_date=datetime.today().date())
        self.assertTrue(calliope.needs_service())
        #Battery needs service?
        calliope = Calliope(current_mileage=20000, last_service_mileage=10000, last_service_date=(datetime.today() - timedelta(days=365*3)).date())
        self.assertTrue(calliope.needs_service())
        #Battery or Engine doesn't need service
        calliope = Calliope(current_mileage=10000, last_service_mileage=5000, last_service_date=datetime.today().date())
        self.assertFalse(calliope.needs_service())

    def test_glissade(Self):
        # willbroguhEngine and splinderBattery
        glissade = Glissade(current_mileage=65000, last_service_mileage=0, last_service_date=datetime.today().date())
        Self.assertTrue(glissade.needs_service())

        glissade = Glissade(current_mileage=40000, last_service_mileage=20000, last_service_date=(datetime.today() - timedelta(days=365*3)).date())
        Self.assertTrue(glissade.needs_service())

        glissade = Glissade(current_mileage=10000, last_service_mileage=5000, last_service_date=datetime.today().date())
        Self.assertFalse(glissade.needs_service())
    
    def test_palindrome(self):
        palindrome = Palindrome(warning_light_is_on=True, last_service_date=datetime.today().date())
        self.assertTrue(palindrome.needs_service())

        palindrome = Palindrome(warning_light_is_on=False, last_service_date=(datetime.today() - timedelta(days=365*5)).date())
        self.assertTrue(palindrome.needs_service())

        palindrome = Palindrome(warning_light_is_on=False, last_service_date=datetime.today().date())
        self.assertFalse(palindrome.needs_service())

    def test_rorchach(self):
        rorschach = Rorschach(current_mileage=70000, last_service_mileage=0, last_service_date=datetime.today().date())
        self.assertTrue(rorschach.needs_service())

        rorschach = Rorschach(current_mileage=50000, last_service_mileage=20000, last_service_date=(datetime.today() - timedelta(days=365*5)).date())
        self.assertTrue(rorschach.needs_service())

        rorschach = Rorschach(current_mileage=10000, last_service_mileage=5000, last_service_date=datetime.today().date())
        self.assertFalse(rorschach.needs_service())

    def test_thovex(self):
        thovex = Thovex(current_mileage=35000, last_service_mileage=0, last_service_date=datetime.today().date())
        self.assertTrue(thovex.needs_service())

        thovex = Thovex(current_mileage=20000, last_service_mileage=10000, last_service_date=(datetime.today() - timedelta(days=365*5)).date())
        self.assertTrue(thovex.needs_service())

        thovex = Thovex(current_mileage=10000, last_service_mileage=5000, last_service_date=datetime.today().date())
        self.assertFalse(thovex.needs_service())

if __name__ == '__main__':
    unittest.main() 
