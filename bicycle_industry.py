class Bicycle(object):
   
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self): # represents a printable version of the init method
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




#------------------------------------------------------------------#



  
class BikeShop(object):
   
    def __init__(self, shop_name, shop_inventory, bike_markup):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        self.bike_markup = bike_markup
        self.profit_amount = 0

    def print_inventory(self):
        """Print the initial inventory of the bike shop for each bike it carries."""
        print "{} Inventory".format(self.shop_name)
        print "-" * 20
        for bike in self.shop_inventory: # bike will be set to the items in the array
            print bike

    def profit(self, bike):
        if not bike in self.shop_inventory:
            return None
        return bike.cost_to_produce * self.bike_markup

    def sale_price(self, bike):
        if not bike in self.shop_inventory:
            return None
        return bike.cost_to_produce + self.profit(bike)

    def print_markup(self):
        print '\nSale Price After Markups'
        print '-' * 20
        for bike in self.shop_inventory:
            profit_amount = self.profit(bike)
            sale_price = self.sale_price(bike)
            print("{} has an msrp is ${} and {} makes ${} off each sale.".format(bike.model_name, sale_price, self.shop_name, profit_amount))


inventory_list = [
    bike1, bike2, bike3, bike4, bike5, bike6
]
bike_shop = BikeShop("Fun Cycles", inventory_list, .20)
bike_shop.print_inventory()

expensive_shop = BikeShop("Expensive Cycles", inventory_list, .50)




    
#-------------------------------------------------------------#




class Customer(object):
    def __init__(self, customer_name, customer_funds):
        self.customer_name = customer_name
        self.customer_funds = customer_funds

    def __repr__(self):
        return "{0} has ${1}.".format(
            self.customer_name, self.customer_funds)

    def can_afford(self, shop, bike):
        bike_price = shop.sale_price(bike)
        return self.customer_funds >= bike_price

    def print_affordable_bikes(self, shop):
        for bike in shop.shop_inventory:
            if self.can_afford(shop, bike):
                print "{0} can afford the {1}".format(self.customer_name, bike.model_name)

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
for customer in customer_list:
    customer.print_affordable_bikes(bike_shop)
    print '-' * 20

print '-' * 20
    
class Bicycle_Manufacturers(object):
    def __init__(self, manu_name, manu_model, manu_cost_to_produce, manu_margin_amount):
        self.manu_name = manu_name
        self.manu_modle = manu_model
        self. manu_margin_amount = manu_margin_amount
        
        
     

    Bike_produced1 = Bicycle_Manufacturers("Trek", "Trek1", 850, .10)
    Bike_produced2 = Bicycle_Manufacturers("Trek", "Trek2", 870, .10)
    Bike_produced3 = Bicycle_Manufacturers("Trek", "Trek3", 890, .10)
    
model_range = [Bike_produced1, Bike_produced2, Bike_produced3]
    def manu_sale_price(self,)