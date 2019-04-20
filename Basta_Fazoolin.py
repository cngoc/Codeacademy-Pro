class Menu ():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time    
    
  def __repr__(self):
    return self.name + " menu available from "+ self.start_time + " to " + self.end_time
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

class Franchise ():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address

  def available_menus(self,time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu
  
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, '11', '16')
    
early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, '15', '18')
    
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, '17', '23')
    
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, '11', '21')

all_menus = [brunch, early_bird, dinner, kids]

arepas_menu = Menu("arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [arepas_place])
#print(brunch)
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli']))
#print(new_installment)
#print(new_installment.available_menus(20))
print(business.name + " has the following franchises " + str(business.franchises))
