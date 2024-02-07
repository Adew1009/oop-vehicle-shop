class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, id, make, model, year, mileage, services):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.total_cars += 1
        CarManager.all_cars.append(self._id)
        
        


my_car = CarManager(12345678,"Toyota", "Camry", 2021, 16543, ["Onstar", "Free Oil Change"])
print(CarManager.all_cars)
print(CarManager.total_cars)
your_car = CarManager(13245678,"Ford", "Focus", 2019, 24325, ["Powertrain Warranty", "Free Oil Change"])
print(CarManager.all_cars)
print(CarManager.total_cars)


