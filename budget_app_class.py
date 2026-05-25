class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}"
        items = ""

        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f"{desc:<23}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total

def create_spend_chart(categories):
    spent = []
    total_spent = 0

    for category in categories:
        cat_spent = 0
        for t in category.ledger:
            if t["amount"] < 0:
                cat_spent += -t["amount"]
        spent.append(cat_spent)
        total_spent += cat_spent

    percentages = []
    for s in spent:
        if total_spent > 0:
            percent = (s / total_spent) * 100
            percentages.append(int(percent // 10) * 10)
        else:
            percentages.append(0)

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        line = f"{str(level).rjust(3)}|"
        for p in percentages:
            if p >= level:
                line += " o "
            else:
                line += "   "
        
        line += " "
        lines.append(line)

  
    lines.append("    " + "-" * (len(categories) * 3 + 1))

   
    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    
    return "\n".join(lines)


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
