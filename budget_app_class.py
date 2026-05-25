class Category:
    def __init__(self,ledger):
      self.ledger = ledger
    
    def deposit(self, amount,description=""):
      self.amout = amount
      self.description = description

      self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=""):
      
      self.ledger.append({"amount": -amount, "description": description})
      return True
        
    def get_balance(self):
      return sum(item["amount"] for item in self.ledger)

    def transfer
def create_spend_chart(categories):
    pass
