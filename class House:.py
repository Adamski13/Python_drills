class House:
    def __init__(self, roof_type, glazed):
        self.roof = roof_type
        self.double.glazed = glazed
        self.floors = 2

    def get_roof_type(self):
        print(self.roof)

    def buid_extension_floor(self):
        if self.roof != "thatch":
            self.floor += 1

class HousingEstate:
    def __init__(self, current_list_of_houses):
        self.houses = current_list_of_houses

    def add_new_built_house_to_estate(self, new_house):
        self.houses.append(new_house)
        
    def build_house_and_it(self):
        h = House("paper", True)
        self.add_new_built_house_to_estate(h)


h1 = House("thatch", False)
h2 = House("slate", True)
estate = HousingEstate(h1, h2)

