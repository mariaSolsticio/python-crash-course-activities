# Restaurant class I had created
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThe restaurant is named " + self.name.title() + ",")
        print("and it specializes in " + self.type.title() + " cuisine.")
    
    def open_restaurant(self):
        print("\nThe restaurant is now open!")
        
    def set_number_served(self, served):
        self.number_served = served
        
    def increment_number_served(self, daily_served):
        self.number_served += daily_served
    
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'rainbow']
        
    def display_flavors(self):
        # Displaying ice cream flavors
        print("\nFlavors we have: ")
        for flavor in self.flavors:
            print(flavor.title())
