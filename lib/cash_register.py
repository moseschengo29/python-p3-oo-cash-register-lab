#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    
    
  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total - (self.discount/100 * self.total)
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.') 
      
  def void_last_transaction(self):
        pass    
           

cash_register = CashRegister()
cash_register_with_discount = CashRegister(20)


cash_register_with_discount.add_item('macbook', 1000)
cash_register_with_discount.apply_discount()

cash_register.apply_discount()

new_register = CashRegister()
new_register.add_item("eggs", 1.99)
new_register.add_item("tomato", 1.76)
new_register.void_last_transaction()

print(new_register.total)
print(new_register.items)

# print(cash_register_with_discount.total)