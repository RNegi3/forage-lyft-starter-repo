class Car:
    def __init__(self, model, engine, battery):
        self.model = model
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
