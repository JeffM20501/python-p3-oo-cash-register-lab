#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount=0):
    self.total=0
    self.discount=discount
    self.items= []
    self.last_transaction=0
  
  def add_item(self, title="", price="", quantity=1):
    self.title=title
    self.price=price
    self.quatity=quantity
    trasactional_total=price*quantity
    for _ in range(quantity):
      self.items.append(self.title)
    self.total+=trasactional_total
    self.last_transaction=trasactional_total
    
  
  def apply_discount(self):
    if self.discount:
      dicounted_price=self.total*self.discount/100
      self.total = self.total-dicounted_price
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print(f"There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total-=self.last_transaction
