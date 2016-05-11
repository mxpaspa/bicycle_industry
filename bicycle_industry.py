




class bicycle(object):
   
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):# represents a printable version of the init method
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)
            
if __name__ == '__main__':

    """ bike models """
    bike1 = bicycle("Trek", 20, 200)#refers to the __init__ method
    bike2 = bicycle("Kono", 40, 300)
    bike3 = bicycle("Speacialized", 35, 400)
    bike4 = bicycle("Schwinn", 20, 500)
    bike5 = bicycle("Cannon", 45, 600)
    bike6 = bicycle("Giant", 30, 700)








#------------------------------------------------------------------#





  
class BikeShop(object):
   
    def __init__(self, shop_name, shop_inventory, bike_markup):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        self.bike_markup = bike_markup
        self.profit_amount = 0
        
inventory_list = [
    bike1, bike2, bike3, bike4, bike5, bike6
]

bike_shop = BikeShop("Fun Cycles", inventory_list, .20)


"""Print the initial inventory of the bike shop for each bike it carries."""
print "Bike Shop Inventory" #/n adds a blank line
print "-" * 20
for bike in range(len(inventory_list)):
    print inventory_list[bike]


            
sale_price=[]
profit_amount=[]  
print '\nSale Price After Markups'
print '-' * 20
for bike in range(len(inventory_list)):
    sale_price = inventory_list[bike].cost_to_produce + inventory_list[bike].cost_to_produce * .20
    profit_amount=sale_price-inventory_list[bike].cost_to_produce  
    
    print("{} has an msrp is ${} and {} makes ${} off each sale.".format(inventory_list[bike].model_name, sale_price, bike_shop.shop_name, profit_amount))

 




    
    
#-------------------------------------------------------------#








class Customer(object):
    def __init__(self, customer_name, customer_funds, bicycle=0):
        self.customer_name = customer_name
        self.customer_funds = customer_funds
        self.bicycle=bicycle
        
    def __repr__(self):
        return "{0} has ${1}.".format(
            self.customer_name, self.customer_funds)
            

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




answers=[]
print raw_input("what is your name")
answers.append(raw_input)



for a in answers:
    if a == customer_list[customer].customer_name:
        print raw_input("do you want to buy a bike?")





    
def purchase_bicycle(self, bicycle, sale_price):
    """Customer purchases bicycle and reduces purchase fund"""
    self.bicycle = bicycle
    self.customer_funds -= sale_price
    # Confirmation message
    print "Congratulations {}, you purchased a {} for ${}.  You have ${} remaining of your bike purchase fund.".format(self.customer_name, bicycle.model_name, sale_price, self.customer_funs)
    
