# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

# Derived Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)
        self.gpu_power = gpu_power
    
    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with GPU power {self.gpu_power}!")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB")
phone2 = GamingSmartphone("Asus", "ROG Phone 7", "512GB", "High-End")

# Using methods
phone1.call("123-456-7890")
phone2.call("987-654-3210")
phone2.play_game("PUBG Mobile")

