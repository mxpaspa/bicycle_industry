class Bicycle(object):
    """
    Bicycles have a model name, a weight, and a cost to produce.
    """
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):# represents a printable version of the init method
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)
            
if __name__ == '__main__':

    """Create 6 different bicycle models"""
    bike1 = Bicycle("Trek", 20, 200)#refers to the __init__ method
    bike2 = Bicycle("Kono", 40, 300)
    bike3 = Bicycle("Speacialized", 35, 400)
    bike4 = Bicycle("Schwinn", 20, 500)
    bike5 = Bicycle("Cannon", 45, 600)
    bike6 = Bicycle("Giant", 30, 700)



class BikeShop(object):
    """
    Bike Shops have a name and an inventory.
    """
    def __init__(self, shop_name, shop_inventory):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        
        
        
"""Create a bicycle shop that has six different bicycle models in stock"""
inventory_list = [
    bike1, bike2, bike3, bike4, bike5, bike6
]

bike_shop = BikeShop("Fun Cycles", inventory_list)
print bike_shop.shop_name

"""Print the initial inventory of the bike shop for each bike it carries."""
print "\nInventory"
print "-" * 20# prints dashes
for bike in range(len(inventory_list)):
    print inventory_list[bike]#refers back to the customer class, the output of the keys are "trek weighs..."
    





        

    
