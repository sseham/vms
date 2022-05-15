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

        def __str__(self):
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


def start_Screen(name, model, carType):
    #initializes the start screen to enter vehicle TYPE
    carType = input("Please enter vehicle type: ")

def car_info(mileage, prev_mileage, prev_oil_change, prev_filter_change, prev_gen_maintenance):
    #gets car info from the user. basically input
    mileage = input(float("Enter current car mileage: "))
    prev_mileage = input(float("Enter any previous car mileage: "))
    prev_oil_change = input("Enter any oil change done to car: ")
    prev_filter_change = input("Enter any filter change done to car: ")
    prev_gen_maintenance = input("Enter last mileage maintenance done to car: ")

    return mileage, prev_mileage, prev_oil_change, prev_filter_change, prev_gen_maintenance
    

def maintenance_record(mile, prev_mil, prev_oil, prev_filter, prev_gen):
    return 

"""
def maintenance(self, mile_diff, mileage, prev_mileage, main_type):
    car_info(mileage, prev_mileage)
    main_type = "None"
    mile_diff = self.mile_diff
    diff = mileage - prev_mileage #mileage and prev_mileage NOT defined

    if diff >= 5000:
        if diff >=  5000 and diff < 16000:
            print("Oil maintenance required")
            main_type = "Oil"
            #Call function to provide instructions for Oil maintenance
        elif diff >= 16000 and diff < 30000:
            print("Air filter change needed")
            main_type = "Air filter"
            #Call function to provide instructions for Air filter change
        elif diff >= 30000:
            print("General maintenance needed")
            main_type = "General"
            #Call function to direct user to nearest service centre 
    else:
        print("No maintenance needed")
        mile_need = 5000 - diff
        print("")

        print(f"Check back after {mile_need} km")

def procedures():
"""
