class car:
    def __init__(self, colour, brand, make, name, year, curr_mileage, prev_mileage, category):
        self.colour = colour
        self.brand = brand #toyota
        self.make = make #corolla
        self.name = name #name of the car owner
        self.year = year
        self.curr_mileage = curr_mileage
        self.prev_mileage = prev_mileage
        self.category = category

        def __string__(self):
            return f"{self.colour}, {self.brand}, {self.make}, {self.name}, {self.year}, {self.curr_mileage}, {self.prev_mileage}"
        
        def mileage_diff(self, curr_mileage, prev_mileage):
            assert curr_mileage < prev_mileage, "Current mileage can NOT be less than previous mileage."
            mileage = curr_mileage - prev_mileage
            return mileage

        def five_k_maint(self):
        #30k air filter 
        #15k windshield wipers, coolant
        #5k oil filter, brake pads, tires, battery
            oil_filter = "Oil Filter"
            brake_pads = "Brake Pads"
            tires = "Tires"
            battery = "Battery"
            return oil_filter, brake_pads, tires, battery

        def fifteen_k_maint(self):
            windshield = "Windsheild Wipers"
            coolant = "Coolant (AntiFreeze)"
            return windshield, coolant
        
        def thirty_k(self):
            air_filter = "Air Filter"
            return air_filter

        def vehicle_maintenance_type(self, mileage, oil_filter, brake_pads, tires, battery,
        windshield, coolant, air_filter):
            five_k = 5000
            fifteen_k = 15000
            thirty_k = 30000
            if mileage < five_k_maint:
                print("Nothing needs to be done. Too soon!")
            elif mileage >= five_k and mileage < fifteen_k:
                print(f"It's time to change {oil_filter}, check your {brake_pads}, pressure level of {tires}, and {battery} quality.")
                return
            elif fifteen_k >= mileage and mileage < thirty_k:
                print(f"It's time to change your {windshield} and {coolant}.")
            elif mileage >= thirty_k:
                print(f"It's time to change your {air_filter}.")
            return
            
