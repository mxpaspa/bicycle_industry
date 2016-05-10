

class Bicycle(object):
   
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):# represents a printable version of the init method
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)
            
if __name__ == '__main__':

    """ bike models """
    bike1 = Bicycle("Trek", 20, 200)#refers to the __init__ method
    bike2 = Bicycle("Kono", 40, 300)
    bike3 = Bicycle("Speacialized", 35, 400)
    bike4 = Bicycle("Schwinn", 20, 500)
    bike5 = Bicycle("Cannon", 45, 600)
    bike6 = Bicycle("Giant", 30, 700)





  
class BikeShop(object):
   
    def __init__(self, shop_name, shop_inventory):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        
"""inventory list"""
inventory_list = [
    bike1, bike2, bike3, bike4, bike5, bike6
]

bike_shop = BikeShop("Fun Cycles", inventory_list)
print bike_shop.shop_name

"""Print the initial inventory of the bike shop for each bike it carries."""
print "Inventory" #/n adds a blank line
print "-" * 20# prints dashes
for bike in range(len(inventory_list)):
    print inventory_list[bike]#refers back to the customer class, the output of the keys are "trek weighs..."






class Customer(object):
    """
    Customer attributes.
    """
    def __init__(self, customer_name, customer_funds):
        self.customer_name = customer_name
        self.customer_funds = customer_funds

    def __repr__(self):
        return "{0} has ${1}.".format(
            self.customer_name, self.customer_funds)
            
"""Create three customers"""
customer1 = Customer("Joe", 200)
customer2 = Customer("Bill", 500)
customer3 = Customer("Dave", 1000)

customer_list = [customer1, customer2, customer3]

print '\nCustomers'
print '-' * 20
for customer in range(len(customer_list)):
    print customer_list[customer]

"""
Print the name of each customer
and a list of the bikes offered by the bike
shop that they can afford given their budget.
Make sure you price the bikes in such a way
that each customer can afford at least one.
"""

print '\nWhich bikes can they afford?'
for customer in range(len(customer_list)):
    print '-' * 20
    for bike in range(len(inventory_list)):
        if inventory_list[bike].cost_to_produce <= \
                customer_list[customer].customer_funds:
            print "{0} can afford the {1}".format(
                customer_list[customer].customer_name,
                inventory_list[bike].model_name
            )
print '-' * 20




        

    
