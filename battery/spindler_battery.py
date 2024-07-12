from datetime import datetime, timedelta
from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date + timedelta(days=365*2)
        return datetime.today().date() > service_threshold_date
